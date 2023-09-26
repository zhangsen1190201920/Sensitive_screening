import json
import logging
import os
import requests
from datetime import date, time, datetime
from multiprocessing import JoinableQueue

from db_utils import upsert, query_max_id
from models import HttpFileDataUnit, FtpFileDataUnit, EmailFileDataUnit, TrxFileDataUnit, SmHitLogDataUnit, \
    GeoHitLogDataUnit, MedHitLogDataUnit, RawTrafficDataUnit, ReturnValueDataUnit
from shared_variable import db
from tools import request_untils
from tools.datetime_utils import get_date_time,get_today_str
from tools.log_untils import setup_logging
from shared_variable import type_industry
# 目前写到文件中
# def writer(write_q: JoinableQueue):
#     while True:
#         try:
#             print("writer!")
#             data_unit = write_q.get()
#             # if data_unit.ide_hit is not None and len(data_unit.ide_hit) != 0:
#                 # continue
#             print("writer got data_unit!")
#             # print("888")
#             master_tablename = data_unit.tablename
#             #print("tablename:{}".format(master_tablename))
#             attrs = vars(data_unit)
#             attrs = {key: attrs[key] for key in attrs if
#                 key != "filepath" and key != "content" and key != "sm_hit" and key != "geo_hit" and key != "bio_hit" and key !="dcm_hit" and key !="ide_hit" and key !="jt808_hit" and key !="carvin_hit"}  # 过滤出需要写入到数据库的字段
#             sql = upsert(master_tablename, attrs)
# 			# 这里需要先执行插入业务日志
# 			#print("#######################")
# 			#print(sql)
# 			#print("#######################")
#             session = db.session()
#             session.execute(sql)
#             max_id = query_max_id(master_tablename)
# 			# print("max_id:{}".format(max_id))
#             if data_unit.sm_hit is not None and len(data_unit.sm_hit) != 0:
#                 for sm_hit in data_unit.sm_hit:
#                         sm_hit.id = max_id
#                         sm_hit.master_tablename = master_tablename
#                         attrs = vars(sm_hit)
#                         attrs = {key: attrs[key] for key in attrs if key != "filepath" and key != "content"}
#                         attrs["hit_content"]=base64.b64encode(attrs["hit_content"].encode()).decode()
#                         sql = upsert(sm_hit.tablename, attrs)
#                         #print("smhit#######################")
#                         #print("sm_hit_sql:{}".format(sql))
#                         # print("smhitsql#######################")
#                         session.execute(sql)
#             if data_unit.geo_hit is not None and len(data_unit.geo_hit) != 0:
#                     for geo_hit in data_unit.geo_hit:
#                         geo_hit.id = max_id
#                         geo_hit.master_tablename = master_tablename
#                         attrs = vars(geo_hit)
#                         # attrs = {key: attrs[key] for key in attrs if key != "filepath" and key != "content"}
#                         sql = upsert(geo_hit.tablename, attrs)
#                         print("geo_hit_sql:{}".format(sql))
#                         session.execute(sql)
#             if data_unit.dcm_hit is not None and len(data_unit.dcm_hit) != 0:
#                     for dcm_hit in data_unit.dcm_hit:
#                         dcm_hit.id = max_id
#                         dcm_hit.master_tablename = master_tablename
#                         attrs = vars(dcm_hit)
#                         # attrs = {key: attrs[key] for key in attrs if key != "filepath" and key != "content"}
#                         sql = upsert(dcm_hit.tablename, attrs)
#                         print("dcm_it_sql:{}".format(sql))
#                         session.execute(sql)
#             if data_unit.ide_hit is not None and len(data_unit.ide_hit) != 0:
#                 for ide_hit in data_unit.ide_hit:
#                     ide_hit.id = max_id
#                     ide_hit.master_tablename = master_tablename
#                     attrs = vars(ide_hit)
#                     attrs = {key: attrs[key] for key in attrs if key != "filepath" and key != "content"}
#                     sql = upsert(ide_hit.tablename, attrs)
#                     print("ide_it_sql:{}".format(sql))
#                     session.execute(sql)
#             if data_unit.jt808_hit is not None and len(data_unit.jt808_hit) != 0:
#                 for jt808_hit in data_unit.jt808_hit:
#                     jt808_hit.id = max_id
#                     jt808_hit.master_tablename = master_tablename
#                     attrs = vars(jt808_hit)
#                     attrs = {key: attrs[key] for key in attrs if key != "filepath" and key != "content"}
#                     sql = upsert(jt808_hit.tablename, attrs)
#                     print("jt808_hit_sql:{}".format(sql))
#                     session.execute(sql)
#             if data_unit.carvin_hit is not None and len(data_unit.carvin_hit) != 0:
#                 for carvin_hit in data_unit.carvin_hit:
#                     carvin_hit.id = max_id
#                     carvin_hit.master_tablename = master_tablename
#                     attrs = vars(carvin_hit)
#                     attrs = {key: attrs[key] for key in attrs if key != "filepath" and key != "content"}
#                     sql = upsert(carvin_hit.tablename, attrs)
#                     print("carvin_hit_sql:{}".format(sql))
#                     session.execute(sql)
#             session.commit()
#         except Exception as e:
#                 f2=open("errorlog_write.txt",'a',encoding='UTF-8')
#                 print("write extension %s",e)
#                 f2.write(str(e))
#                 f2.write(str(get_date_time()))
#                 f2.close()

# 输出到writer.log
writer_logger = setup_logging("writer")
sql_logger=setup_logging("errorfile")


def writer(write_q: JoinableQueue):
    while True:
        try:
            data_unit = write_q.get()
            # print("sender got data_unit!")

            filepath_on_s3 = ""
            localfilepath=data_unit.filepath
            if isinstance(data_unit, (HttpFileDataUnit, FtpFileDataUnit, EmailFileDataUnit, TrxFileDataUnit)):
                #riter_logger(f"{data_unit.filepath}")
                filepath_on_s3 = upload_file_to_s3(data_unit.filepath)
            if filepath_on_s3 != "":
                data_unit.filepath = filepath_on_s3
            else:
                continue

            master_tablename = data_unit.tablename
            writer_logger.info(f"写入者从生产者结果队列中得到内容,主表为{master_tablename}")
            attrs = vars(data_unit)
            # 处理主表中的字段,刨除掉没用的字段

            attrs = {key: attrs[key] for key in attrs if
                     key != "sm_hit" and key != "geo_hit" and key != "bio_hit" and key != "dcm_hit" and key != "content"}  # 过滤出需要写入到数据库的字段
            writer_logger.info(f"过滤之后的主表字段{attrs}")
            sql = upsert(master_tablename, attrs)
            # 这里需要先执行插入业务日志
            # print("#######################")
            writer_logger.info(f"before sql:{sql}")
            # print("#######################")
            session = db.session()
            session.execute(sql)
            writer_logger.info(f"sql:{sql}")

            son_table_write(data_unit, master_tablename, session)

            # 处理变量返回值发送请求
            variable_value_result_send(data_unit,master_tablename,session)

        except Exception as e:
            writer_logger.error(f"写入表失败,失败原因", e)
            sql_logger.info(f"失败文件路径",localfilepath)


# 处理变量返回值发送请求
def variable_value_result_send(data_unit, master_tablename, session):
    try:
        son_table = ""
        if data_unit.sm_hit is not None and len(data_unit.sm_hit) != 0:
            engine_hit_deal(data_unit.sm_hit,data_unit)
            son_table = "sm_hit"
        # 处理地理发送的字段
        if data_unit.geo_hit is not None and len(data_unit.geo_hit) != 0:
            engine_hit_deal(data_unit.geo_hit,data_unit)
            son_table = "geo_hit"
        # 处理医疗信息
        if data_unit.dcm_hit is not None and len(data_unit.dcm_hit) != 0:
            engine_hit_deal(data_unit.dcm_hit,data_unit)
            son_table = "dcm_hit"
        #处理生物信息
        if data_unit.bio_hit is not None and len(data_unit.bio_hit) != 0:
            engine_hit_deal(data_unit.bio_hit,data_unit)
            son_table = "bio_hit"
        dict_data_unit = vars(data_unit)
        dict_data_unit['eventlog_time'] = get_date_time()
        # ToDo: 主表因为tlv没提供，所以这里是写死的
        #dict_data_unit['c_time'] = get_date_time()
        #dict_data_unit['c_flowid'] = 123
        #dict_data_unit['gbt32960_hit'] = []
        print("{}----------------------------------->{}".format(son_table,
                                                                json.dumps(dict_data_unit, ensure_ascii=False)))
        writer_logger.info(f"{son_table}----------------------------------->{json.dumps(dict_data_unit, ensure_ascii=False)}")

        # 发送请求
        request_untils.send_data(master_tablename, dict_data_unit)
        writer_logger.info("success send!")
    except Exception as err:
        print("变量返回值发送出错", err)


# 处理大文件子表写表
def son_table_write(data_unit, master_tablename, session):
    try:
        # 处理医疗信息
        if data_unit.dcm_hit is not None and len(data_unit.dcm_hit) != 0:
            for dcm_hit in data_unit.dcm_hit:
                max_id = query_max_id(master_tablename)
                dcm_hit.master_tablename = master_tablename
                attrs = vars(dcm_hit)
                attrs["id"] = max_id
                sql = upsert(dcm_hit.tablename, attrs)
                # print("dcm_it_sql:{}".format(sql))
                writer_logger.info(f"dcm_it_sql处理子表插入语句{sql}")
                session.execute(sql)
                session.commit()
                # 处理医疗信息
        if data_unit.geo_hit is not None and len(data_unit.geo_hit) != 0:
            for geo_hit in data_unit.geo_hit:
                max_id = query_max_id(master_tablename)
                geo_hit.master_tablename = master_tablename
                attrs = vars(geo_hit)
                attrs["id"] = max_id
                sql = upsert(geo_hit.tablename, attrs)
                writer_logger.info(f"gep处理子表插入语句{sql}")
                session.execute(sql)
                session.commit()
        if data_unit.bio_hit is not None and len(data_unit.bio_hit) != 0:
            for bio_hit in data_unit.bio_hit:
                max_id = query_max_id(master_tablename)
                bio_hit.master_tablename = master_tablename
                attrs = vars(bio_hit)
                attrs["id"] = max_id
                sql = upsert(bio_hit.tablename, attrs)
                writer_logger.info(f"bio处理子表插入语句{sql}")
                session.execute(sql)
                session.commit()

    except Exception as error:
        writer_logger.error(f"写入子表失败，原因：{error}")


# 处理从表之间的字段转成字典
def engine_hit_deal(engine_hit_arr,dataunit):
    index = 0
    for engine_hit in engine_hit_arr:
        attrs = vars(engine_hit)
        print("用来查看是否有file、输出之前的内容：", attrs)
        # ToDo：目前这个是否需要为违规比对字段是
        attrs['need_irregular_judge'] = False
        attrs['c_flowid'] = dataunit.c_flowid
        engine_hit_arr[index] = attrs
        index = index + 1


def upload_file_to_s3(filepath):
    # 设置请求头中用户名密码
    headers = {
        "Username": "u_wa_yj2s_sjcj_hsoft",
        "Password": "CA388EsvrC7kQ"
    }
    try:
        filename = os.path.basename(filepath)
        dirname = os.path.dirname(filepath)
        newfilename = datetime.now().strftime("%Y%m%d%H%M%S") + '_'+filename
        os.rename(filepath, os.path.join(dirname, newfilename))
        type_file= filename.split(".")[-1]
        sendtype = filepath.split("/")[-3]
        localfilepath=os.path.join(dirname, newfilename)
        newfilepath=os.path.join(type_industry[type_file],type_file,get_today_str(),sendtype,newfilename)
        # 远程服务器URL0212
        remote_url = "http://10.58.136.36:80/wa_yj2s_sjcj_db_b_sjcj_file/" + newfilepath
        writer_logger.info(f"发送地址{remote_url}，原文件路径{filepath},新文件路径{newfilepath}")

        # 发送PUT请求上传文件
        with open(localfilepath, "rb") as file:
            writer_logger.info("文件打开成功")
            response = requests.put(remote_url, headers=headers, data=file)

        # 检查响应状态码
        if response.status_code == requests.codes.ok:
            print("文件上传成功")
            writer_logger.info("文件上传成功")
            os.remove(localfilepath)
            return remote_url
        else:
            print("文件上传失败")
            return ""
    except Exception as error:
        writer_logger.error(f"上传s3子表失败，原因：{error}")
        writer_logger.error(f"消费者报错{traceback.format_exc()}")
    return ""
