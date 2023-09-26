# 这个文件用于保存多个模块之间共享的变量,避免循环依赖以及不必要参数传递
import logging
import threading
import os
from typing import List

from flask import Flask, request
from flask_restful import Api, Resource

import ftp_client
from hyperscan import init
from models import FileSubscribeDo, SensitiveModelDo
from flask_sqlalchemy import SQLAlchemy

from multiprocessing import Process, JoinableQueue, Queue

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysql@10.58.46.75:3306/dataprocessor?password=HitK1816@2022'
db = SQLAlchemy(app, engine_options={'pool_recycle': 5, 'pool_size': 50})

# 保存在内存中的文件订阅规则,key为id,value为文件订阅规则对象
file_subscribes = {}

# 保存在内存中的csemp监测规则，key为monitor_id，value为csemp规则对象
csemps = {}

# 保存在内存中的敏感模型
sensitive_models = {}

# 敏感模型与文件订阅规则关联表,元组列表 todo 暂时直接查数据库
fs_sm_assc = []

data_unit_q = JoinableQueue()
write_q = JoinableQueue()

ftp_fileq_http = JoinableQueue()
ftp_fileq_email = JoinableQueue()
ftp_fileq_ftp = JoinableQueue()


# 用来保存文件的根目录
ld_root = "/var"

# ftp_clients = []
ftp_processors = []

# 应用于file_subscribes和sensitive_models的锁
lock_sm = threading.Lock()
lock_fs = threading.Lock()

# 天融信的ftp传输目录
trx_root = "/home/surfilter_file/topsec"
# trx_root = "/var/trx"
# 保存的生产者，消费者，写入者
consumer_num = 1
producers = {}  # tag:producer
consumers = {}
writers = {}

# 本节点能够处理的所有文件类型, 从配置文件中读取
file_types = []

def need_to_handle(filename):
    return os.path.splitext(filename)[-1] in file_types

# 生物文件种类
bio_types=["fastq","fasta"]
# 地理引擎能处理的文件种类
kml_file_types = ["doc", "docx", "xls", "xlsx", "ppt", "pptx", "pdf", "txt", "kml",'zip', "gzip"]
#  医疗引擎能处理的文件种类
dcm_file_types = ["doc", "docx", "xls", "xlsx", "ppt", "pptx", "pdf", "txt", "kml",'zip', "gzip"]
# ToDo: 20230410 截止到目前为止生产者能处理的文件类型
able_deal_file_type=["kml","dcm","doc", "docx", "xls", "xlsx", "ppt", "pptx", "pdf", "txt"]
type_industry={"dicm":"medical","fastq":"biology","kml":"geography","fasta":"biology","xls":"usual","pdf":"usual","doc":"usual"}