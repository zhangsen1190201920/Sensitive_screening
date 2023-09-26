import threading
import time

from flask import Flask, request
from flask_restful import Api, Resource

import initializer
from hyperscan import init
from models import FileSubscribeDo, SensitiveModelDo, RawTrafficDataUnit, ReturnValueDataUnit
from flask_sqlalchemy import SQLAlchemy
from db_utils import *
from shared_variable import file_subscribes, sensitive_models, api, app, data_unit_q,ftp_fileq_email,ftp_fileq_http,ftp_fileq_ftp
import json

# 接受原始流量的接口
class RawTraffic(Resource):
    def post(self):
        rt = request.json
        data_unit = RawTrafficDataUnit(rt)
        data_unit_q.put(data_unit)
        # todo
        return {"msg": "ok"}

# 接受ftp文件拉取请求的接口
class FtpFile(Resource):
    def post(self):
        rt = request.json
        rt_dict=json.loads(rt)
        #data={"filename":file,"remote_dir":self.remote_dir}
        remote_dir = rt_dict["remote_dir"]
        if "http" in remote_dir:
            ftp_fileq_http.put(rt_dict)
        elif "ftp" in remote_dir:
            ftp_fileq_ftp.put(rt_dict)
        else:
            ftp_fileq_email.put(rt_dict)
        # todo
        return {"msg": "ok"}

# 接收变量返回值的接口
class ReturnValue(Resource):
    def post(self):
        rv = request.json
        #f = open("log.txt","w+")
        #f.write(str(rv))
        #print(str(rv))

        data_unit = ReturnValueDataUnit(rv)
        print(data_unit.c_event_id)
        biolist=["10030003327","10030003324","10030003329","10030003330","10030003328","10030003325"]
        if str(data_unit.c_event_id) in biolist:
            print("bio_engine event id")
            print(str(data_unit.c_event_id))
            print("initial request:")
            print(str(rv))
            print("c_return_info:")
            print(str(bytes.fromhex(data_unit.c_return_info)))
            f=open("bio"+str(data_unit.c_event_id)+".txt",'a')
            f.write("bio_engine event id\n")
            f.write(str(data_unit.c_event_id)+'\n')
            f.write("initial request:\n")
            f.write(str(rv)+'\n')
            f.write("c_return_info:\n")
            f.write(str(bytes.fromhex(data_unit.c_return_info))+'\n')
        data_unit_q.put(data_unit)
        # todo
        return {"msg": "ok"}


if __name__ == '__main__':
    api.add_resource(RawTraffic, "/raw_traffic")
    api.add_resource(FtpFile, "/ftp_file")
    api.add_resource(ReturnValue, "/return_value")
    initializer.initialize()
    app.run(host="0.0.0.0")
