# todo 初始化
from time import ctime

from tools.datetime_utils import get_today_str
from db_utils import query_all_sm, query_all_fs, query_all_csemp
# from ftp_client import FtpClient
from ftp_processor import FtpProcessor
from shared_variable import file_subscribes, sensitive_models, csemps, ftp_processors,ftp_fileq_http,ftp_fileq_ftp,ftp_fileq_email,file_types
import processor
import dcmdata

def initialize():
    """

    """
    read_file_types()
    print("======加载需要解析的文件类型======")
    query_all_rules()
    print("======获取数据库数据======")
    query_all_rules()
    print("======启动数据库监听器======")
    #start_schedule_task()
    print("======初始化ftp客户端======")
    init_ftp()

    print("======初始化hyperscan======")
    hyperscan_init()
    print("======启动文件解析模块======")

    start_processor()

    print("======初始化dcm解析模块=====")
    dcmdata.inittaglist(r'./taglist.txt') #调用dcndata.py初始化

# 获取所有rules
def query_all_rules():
    sensitive_models.update(query_all_sm()) 
    print(sensitive_models)
    file_subscribes.update(query_all_fs())
    print(file_subscribes)
    csemps.update(query_all_csemp())


# 初始化自动机
def hyperscan_init():
    id_list = []
    regex_list = []
    for sm_id,sm in sensitive_models.items():
        print("sm_id:")
        print(sm_id)
        id_list.append(sm.model_id)
        regex_list.append(sm.sensitive_rule)
    print("id list regex_list:")
    print(id_list,regex_list)
    #hyperscan.init(id_list, regex_list)


# 启动ftp_processpr去处理ftp文件请求
def init_ftp():
    print("===========================文件解析模块启动成功,正在拉取大文件=======================================")
    today_str = get_today_str()
    #today_str="20230628"
    print(format(today_str))
    # 创建ftpc_http线程
    ftp_pro_http = FtpProcessor("10.62.19.145", 21, "user_download", "ftp_user_2022", "/home/k1816/hzh/big_file_store/{}/http".format(today_str),ftp_fileq_http)
    ftp_pro_ftp = FtpProcessor("10.62.19.145", 21, "user_download", "ftp_user_2022", "/home/k1816/hzh/big_file_store/{}/ftp".format(today_str),ftp_fileq_ftp)
    # ftp_pro_email = FtpProcessor("10.62.19.145", 21, "user_download", "ftp_user_2022", "/home/k1816/hzh/big_file_store/{}/email".format(today_str),ftp_fileq_email)
    
    ftp_processors.extend([ftp_pro_http,ftp_pro_ftp])
    #ftp_processors.extend([ftp_pro_http,ftp_pro_email,ftp_pro_ftp])
    ftp_pro_http.start()
    ftp_pro_ftp.start()
    # ftp_pro_email.start()
    
    #ftpc_email = FtpClient("10.62.19.145", 21, "user_download", "ftp_user_2022"
    #                      , "/{}/email".format(today_str)
    #                      , "{}/files/{}/email".format(ld_root, today_str))
    #ftpc_ftp = FtpClient("10.62.19.145", 21, "user_download", "ftp_user_2022"
    #                     , "/{}/ftp".format(today_str)
    #                     , "{}/files/{}/ftp".format(ld_root, today_str))

    #ftp_clients.extend([ftpc_ftp, ftpc_http, ftpc_email])
    #ftpc_ftp.start()
    # ftpc_http.start()
    # ftpc_email.start()
def read_file_types():
    with open("./file_types.txt","r") as f:
        file_types = f.readline().split(",")
        print("本节点能够处理的文件类型为:")
        print(file_types)
        

# 启动文件解析
def start_processor():

    processor.start_process()
