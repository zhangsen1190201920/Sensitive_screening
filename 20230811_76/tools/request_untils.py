import json
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import urllib
from models import IDeHitLogDataUnit
from tools.log_untils import setup_logging
# 定义远端接口地址
api_url = "http://10.58.46.9:8894/api/"
# api_url = "http://127.0.0.1:4523/m1/2237065-0-default/api/"
# 表1接口
api_url_one_table = api_url + "sendData1ToKafka"
# 表2接口
api_url_tow_table = api_url + "sendData2ToKafka"
# 表3接口
api_url_three_table = api_url + "sendData3ToKafka"
request_logger=setup_logging("request")
# 判断将要请求哪个接口
def decideUrl(master_tablename):
    """判断是哪个表 进行数据发送"""
    # 表1 以及所属从表 /api/sendData1ToKafka
    if master_tablename == "fs_http" or master_tablename == "fs_ftp" or master_tablename == "fs_email" or master_tablename == "fs_monitor":
        print("发送请求一！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！")
        return api_url_one_table
    if master_tablename == "content_subscribe_result":
        print("发送请求二！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！")
        return api_url_tow_table
    if master_tablename == "variable_value_result":
        print("发送请求三！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！")
        return api_url_three_table

def send_data(master_tablename, attrs):
        try:
            #
           if master_tablename=="variable_value_result":
                url = decideUrl(master_tablename)
                print("本次请求的地址为：",url)
                heards = {'Content-Type': 'application/json'}
                req = Request(url=url, data=json.dumps(attrs, ensure_ascii=False).encode('utf-8'),
                              headers=heards)
                response = urllib.request.urlopen(req)
                status_code=response.status

                if status_code!= 200:
                    # 请求失败打印错误信息
                    print("请求失败 错误信息:", response.text)
                else:
                    print("请求成功")
                response.close()
           if master_tablename == "fs_http" or master_tablename == "fs_ftp" or master_tablename == "fs_email" or master_tablename == "fs_monitor":
                url = decideUrl(master_tablename)
                print("本次请求的地址为：",url)
                request_logger.info(f"本次请求的地址为：{url}")
                heards = {'Content-Type': 'application/json'}
                req = Request(url=url, data=json.dumps(attrs, ensure_ascii=False).encode('utf-8'),
                              headers=heards)
                response = urllib.request.urlopen(req)
                status_code=response.status
                request_logger.info(f"{status_code}")
                if status_code!= 200:
                    # 请求失败打印错误信息
                    print("请求失败 错误信息:", response.text)
                else:
                    print("请求成功")
                response.close()
        except Exception as err:
            print("请求错误信息",err)

# def testPost():
# data={
# "master_tablename":"fs_ftp",
# "model_id":1,
# "model_name":"BIO002-SFSB_SFZ_stream",
# "industry":"个人信息",
# "idcard":"421221198911112627",
# "host":"127.0.01",
# "user_agent":"test",
# "name":"测试姓名",
# "phone":"1367620145",
# "address":"山东省",
# "bankcard":"123465789",
# "password":"qwe1111111",
# "hit_count":"10"}
# aa['identity_hit'].append(data)
# attrs=IDeHitLogDataUnit(data)
# # 将dict转换成json string
# #json_object = {"data": aa}
# #转换成字节流
# #data=urllib.parse.urlencode(json_object).encode('utf-8')
# print( "转换成字节流", aa)
# req=Request(url=api_url_three_table,data=json.dumps(aa).encode('utf-8'))
# rep=urllib.request.urlopen(req)
# print( "rep", dict(rep))
# response=rep.read().decode("utf-8")
# print("response",response)
# if response!=None or response.status_code!=200:
# #请求失败打印错误信息
# print("请求失败 错误信息:",response.text)
# else:
# print("请求成功")

# testPost()
