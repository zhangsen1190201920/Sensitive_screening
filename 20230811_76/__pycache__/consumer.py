import mimetypes
import re
import time
import zipfile
from multiprocessing import Process, JoinableQueue, Queue
import dcmdata
# import magic
import chardet

import textract
import os
from textract.exceptions import MissingFileError

# rules 已经细分到行业
import hyperscan
from models import HttpFileDataUnit, FtpFileDataUnit, EmailFileDataUnit, TrxFileDataUnit, SmHitLogDataUnit,GeoHitLogDataUnit
from shared_variable import fs_sm_assc, sensitive_models, file_subscribes
from db_utils import *
from geo_engine import parse_kml
def consumer(data_unit_q: JoinableQueue, write_q: JoinableQueue,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18):
    while True:
        data_unit = data_unit_q.get()
        if data_unit is None:
            print("consumer got None")
            continue
        #rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18=consume_test(data_unit,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18)
       # print(data_unit)
        #results = consume_sm(data_unit)
        #print("sm final results:{}".format(results))
        #for res in results:
            # 将命中的结果日志绑定到数据单元上
           # sm_hit_log = SmHitLogDataUnit(res)
            #data_unit.sm_hit.append(sm_hit_log)
        
        results = consume_geo(data_unit)
        print("geo final results:{}".format(results))
        for res in results:
            # 将geo命中的结果日志绑定到数据单元上
            geo_hit_log = GeoHitLogDataUnit(res)
            data_unit.geo_hit.append(geo_hit_log)
        
       # results=consume_dcm(data_unit)
        #print("dcm final results:{}".format(results))
        # 将geo命中的结果日志绑定到数据单元上
        #med_hit_log = GeoHitLogDataUnit(results)
        #data_unit.geo_hit.append(med_hit_log)
        write_q.put(data_unit)
def consume_test(data_unit,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18):
   if str(data_unit.c_event_id)=="10030003327" :
     rule1 +=1
     print(data_unit.c_event_id)
   elif str(data_unit.c_event_id)=="10030003324":
     rule2 +=1
     print(data_unit.c_event_id)
   elif str(data_unit.c_event_id)=="10030003329":
     rule3 +=1
     print(data_unit.c_event_id)
   elif str(data_unit.c_event_id)=="10030003330":
     rule4 +=1
     print(data_unit.c_event_id)
   elif str(data_unit.c_event_id)=="10030003328":
     rule5 +=1
     print(data_unit.c_event_id)
   elif str(data_unit.c_event_id)=="10030003325":
     rule6 +=1
     print(data_unit.c_event_id)
     print(data_unit.c_event_id)
   elif str(data_unit.c_event_id)=="10030003331":
     rule7 +=1
     print(data_unit.c_event_id)
   elif str(data_unit.c_event_id)=="10030003332":
     rule8 +=1
     print(data_unit.c_event_id)
   elif str(data_unit.c_event_id)=="10030003333":
     rule9 +=1
     print(data_unit.c_event_id)
   elif str(data_unit.c_event_id)=="10030003334":
     rule10 +=1
     print(data_unit.c_event_id)
   elif str(data_unit.c_event_id)=="10030002920":
     rule11 +=1
     print(data_unit.c_event_id)
   elif str(data_unit.c_event_id)=="10030002903":
     rule12+=1
     print(data_unit.c_event_id)
   elif str(data_unit.c_event_id)=="10030003335":
     rule13 +=1
     print(data_unit.c_event_id)
   elif str(data_unit.c_event_id)=="10030003336":
     rule14 +=1
     print(data_unit.c_event_id)
   elif str(data_unit.c_event_id)=="10030003337":
     rule15 +=1
     print(data_unit.c_event_id)
   elif str(data_unit.c_event_id)=="10030003338":
     rule16 +=1
     print(data_unit.c_event_id)
   elif str(data_unit.c_event_id)=="10030003201":
     rule17 +=1
     print(data_unit.c_event_id)
   elif str(data_unit.c_event_id)=="10030003339":
     print(data_unit.c_event_id)
     rule18 +=1
   print("##############")
   print(str(rule1))
   print(str(rule2))
   print(str(rule3))
   print(str(rule4))
   print(str(rule5))
   print(str(rule6))
   print(str(rule7))
   print(str(rule8))
   print(str(rule9))
   print(str(rule10))
   print(str(rule11))
   print(str(rule12))
   print(str(rule13))
   print(str(rule14))
   print(str(rule15))
   print(str(rule16))
   print(str(rule17))
   print(str(rule18))
   print("##############")
   return rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18
def consume_sm(data_unit):
    final_result = []
    # print("got data_unit! filepath:{}".format(data_unit.filepath))
    print("got data_unit!")
    if isinstance(data_unit, (HttpFileDataUnit, FtpFileDataUnit, EmailFileDataUnit)):
        # 如果是报文引擎的数据，默认都需要进行敏感甄别
        extract_content(data_unit, file_type=data_unit.c_file_type)
        print("extracted content：{}".format(data_unit.content))
        result = hyperscan.match(data_unit.content)
        print("match result:{}".format(result))
        for res in result:
            if res['content'] == '':
                continue
            model_id = int(res["model_id"])
            sm = sensitive_models[model_id]
            file_types = sm.file_type.split(";")
            # 根据文件类型以及fs——sm关联表过滤匹配结果
            if data_unit.c_file_type not in file_types:
                # print("file type not match! data_unit.c_file_type:{}".format(data_unit.c_file_type))
                continue
            fs_ids = query_fs_by_model_id(model_id)
            print("fs_ids:{}".format(fs_ids))
            if len(fs_ids) == 0:
                continue
            flag = False
            for fs_id in fs_ids:
                fs = file_subscribes[fs_id[0]]
                if data_unit.c_file_type in fs.file_type.split(";"):
                    flag = True
            if flag is False:
                continue

            # 填写额外的字段
            res["model_name"] = sm.model_name
            res["industry"] = sm.industry
            res["hit_count"] = len(res["content"].split(";"))
            res["master_tablename"] = data_unit.tablename
            final_result.append(res)

    elif isinstance(data_unit, TrxFileDataUnit):
        # 如果是天融信的文件
        extract_content(data_unit)
        print("extracted content：{}".format(data_unit.content))
        result = hyperscan.match(data_unit.content)
        print("match result:{}".format(result))
        model_ids = query_sm_by_csemp_rule_id(data_unit.rule_id)
        for res in result:
            # 过滤掉result中content为空的结果
            if res['content'] == '':
                continue
            # 过滤掉result中未配置规则的匹配结果
            if res['model_id'] not in model_ids:
                continue
            sm = sensitive_models[res['model_id']]
            # 填写额外的字段
            res["model_name"] = sm.model_name
            res["industry"] = sm.industry
            res["hit_count"] = len(res["content"].split(";"))
            res["master_tablename"] = data_unit.tablename
            final_result.append(res)


    elif isinstance(data_unit, RawTrafficDataUnit):
        # 如果是原始流量数据
        result = hyperscan.match(data_unit.block_content)
        print("raw traffic match result:{}".format(result))
        model_ids = query_sm_by_csemp_rule_id(data_unit.rule_id)
        for res in result:
            # 过滤掉result中content为空的结果
            if res['content'] == '':
                continue
            # 过滤掉result中未配置规则的匹配结果
            if res['model_id'] not in model_ids:
                continue
            sm = sensitive_models[res['model_id']]
            # 填写额外的字段
            res["model_name"] = sm.model_name
            res["industry"] = sm.industry
            res["hit_count"] = len(res["content"].split(";"))
            res["master_tablename"] = data_unit.tablename
            final_result.append(res)
    
    elif isinstance(data_unit, ReturnValueDataUnit):
        # 如果是变量返回值
        # 16进制的数据
        result = []
        result = hyperscan.match(bytes.fromhex(data_unit.c_return_info))
        print("return value match result:{}".format(result))
        print(data_unit.c_event_id)
        model_ids = query_sm_by_csemp_rule_id(data_unit.c_event_id)
        model_ids=[x[0] for x in model_ids]
        print(model_ids)
        for res in result:
            # 过滤掉result中content为空的结果
            if res['content'] == '':
                continue
            # 过滤掉result中未配置规则的匹配结果
            if int(res['model_id'] ) not in model_ids:
                continue
            sm = sensitive_models[int(res['model_id'])]
            # 填写额外的字段
            res["model_name"] = sm.model_name
            res["industry"] = sm.industry
            res["hit_count"] = len(res["content"].split(";"))
            res["master_tablename"] = data_unit.tablename
            final_result.append(res)

    return final_result

def consume_geo(data_unit):
    final_result = []
    # print("got data_unit! filepath:{}".format(data_unit.filepath))
    print("got data_unit!")
    if isinstance(data_unit, (HttpFileDataUnit, FtpFileDataUnit, EmailFileDataUnit)):
        # 如果是报文引擎的数据，默认都需要进行敏感甄别
        extract_content(data_unit, file_type=data_unit.c_file_type)
        print("extracted content:{}".format(data_unit.content))
        result = parse_kml(data_unit.content)
        print("geo engine match result:{}".format(result))
        for res in result:
            new_res = {}
            if res['content'] == '*' or res["content"] == "":
                continue
            new_res["long_lati"] = res["content"]
            new_res["geography"] = "地理"
            new_res["geo_type"] = res["geo_type"]
            new_res["fence_province"] = res["fence_province"]
            new_res["fence_city"] = res["fence_city"]
            new_res["fence_name"] = res["fence_fencename"]
            # todo
            new_res["fence_type"] = "unknown"
            new_res["fecne_relation"] = res["fecne_relation"]
            final_result.append(new_res)

    elif isinstance(data_unit, TrxFileDataUnit):
        # 如果是天融信的文件
        extract_content(data_unit)
        print("extracted content：{}".format(data_unit.content))
        result = parse_kml(data_unit.content)
        print("geo engine match result:{}".format(result))
        
        for res in result:
            new_res = {}
            if res['content'] == '*' or res["content"] == "":
                continue
            new_res["long_lati"] = res["content"]
            new_res["geography"] = "地理"
            new_res["geo_type"] = res["geo_type"]
            new_res["fence_province"] = res["fence_province"]
            new_res["fence_city"] = res["fence_city"]
            new_res["fence_name"] = res["fence_fencename"]
            # todo
            new_res["fence_type"] = "unknown"
            new_res["fecne_relation"] = res["fecne_relation"]
            final_result.append(new_res)
        


    elif isinstance(data_unit, RawTrafficDataUnit):
        # 如果是原始流量数据
        final_result = []
        result = parse_kml(data_unit.block_content)
        print("raw traffic geo engine match result:{}".format(result))

        for res in result:
            new_res = {}
            if res['content'] == '*' or res["content"] == "":
                continue
            new_res["long_lati"] = res["content"]
            new_res["geography"] = "地理"
            new_res["geo_type"] = res["geo_type"]
            new_res["fence_province"] = res["fence_province"]
            new_res["fence_city"] = res["fence_city"]
            new_res["fence_name"] = res["fence_fencename"]
            # todo
            new_res["fence_type"] = "unknown"
            new_res["fecne_relation"] = res["fecne_relation"]
            final_result.append(new_res)
    
    elif isinstance(data_unit, ReturnValueDataUnit):
        # 如果是变量返回值
        # 16进制的数据
        #print(data_unit.c_return_info)
        #print(bytes.fromhex(data_unit.c_return_info))
        result=[]
        final_result = []
        print(data_unit.c_event_id)
        if str(data_unit.c_event_id)=="10030002903" or str(data_unit.c_event_id)=="10030002920"  or str(data_unit.c_event_id)=="10030003338" or str(data_unit.c_event_id)=="10030003201":
             result = parse_kml(str(bytes.fromhex(data_unit.c_return_info)))
             #print(format(str(bytes.fromhex(data_unit.c_return_info))))
       # print("return value geo engine match result:{}".format(result))
        str_test="coordinates"
        str_save=str(bytes.fromhex(data_unit.c_return_info))
        if str_save.find(str_test)>=0:
            print(str_save)
            f2=open("kml_create.txt",'w',encoding='UTF-8')
            f2.write(str_save)
            f2.close()
        for res in result:
            new_res = {}
            if res['content'] == '*' or res["content"] == "" or  res["fence_fencename"]=='*'  :
                continue
            new_res["long_lati"] = res["content"]
            new_res["geography"] = "地理"
            new_res["geo_type"] = res["geo_type"]
            new_res["fence_province"] = res["fence_province"]
            new_res["fence_city"] = res["fence_city"]
            new_res["fence_name"] = res["fence_fencename"]
            # todo
            new_res["fence_type"] = "unknown"
            new_res["fecne_relation"] = res["fecne_relation"]
            final_result.append(new_res)
    return final_result
def consume_dcm(data_unit):
    final_result = []
    # print("got data_unit! filepath:{}".format(data_unit.filepath))
    #print("DCM got data_unit!")
    if isinstance(data_unit, (HttpFileDataUnit, FtpFileDataUnit, EmailFileDataUnit)):
        print("Not finish!")
    elif isinstance(data_unit, ReturnValueDataUnit):
        # 如果是变量返回值
        # 16进制的数据
        #print(data_unit.c_return_info)
        #print(bytes.fromhex(data_unit.c_return_info))
        result=[]
        #print(data_unit.c_event_id)
        if str(data_unit.c_event_id)=="10030003331" :
           print("DCM got data_unit!")
           result = parsedata(str(bytes.fromhex(data_unit.c_return_info)))
           print(result)
        return []
def extract_content(data_unit, file_type=None):
    try:
        # TODO 文件内容可能不是utf-8编码
        content = textract.process(data_unit.filepath, extension=file_type).decode("utf-8")
        data_unit.content = content
    except UnicodeDecodeError as ue:
        print(ue)
        print("{}处理出错".format(data_unit.data))
    except LookupError as le:
        print(le)
        print("未知拓展名data:{}\tfile_type:{}".format(data_unit.data, file_type))


def guess_encoding(filename):
    """Returns a tuple of (guessed encoding, confidence).
    :param filename:
    """
    res = chardet.detect(open(filename).read())
    return res['encoding'], res['confidence']


if __name__ == '__main__':
    for root, dirs, files in os.walk("test"):
        for file in files:
            print("filename:{} desc:{}".format(file, magic.from_file(os.path.join(root, file))))
