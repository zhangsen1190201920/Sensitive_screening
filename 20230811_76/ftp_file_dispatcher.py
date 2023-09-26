import logging
import os.path
import shutil
import threading
import time
import  codecs
from ftplib import FTP, error_perm
from datetime import date
import re
from tools.datetime_utils import get_today_str
import requests
import json
import traceback
from threading import Thread
from multiprocessing import Process, JoinableQueue, Queue



def setup_logging(logger_name):
    logger=logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    format =logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
    # 将日志文件输出到文件
    file_handler=logging.FileHandler(f'{logger_name}.log')
    file_handler.setFormatter(format)
    logger.addHandler(file_handler)
    return logger
def out_txt_dic(file_name,dic):
    """
    将字典类型写出文件
    """
    try:
        with open(file_name,"w") as  f:
            for key,value in dic.items():
                f.write(f"{key}:{value}\n")
        print("写入文件成功")
    except Exception as  e:
        print("写入txt失败",e)
        
# TODO 两层压缩 解压之后可能带文件夹和多个文件, 层数不定, 需要处理
# 输出到ftp_clent.log
ftp_log=setup_logging("ftp")
worker = {}
def read_worker_server_info():
    with open("./worker_server_info.txt",'r') as f:
        for line in f:
            items = line.strip().split(":")
            worker[items[1]] = items[0]
        ftp_log.info(worker)
file_types = ["gzip","fasta","fastq","dicm"] # 在这里配置所有需要处理的文件类型
class FtpFileDispatcher(threading.Thread):

    def __init__(self, host, port, username, password, remote_dir, interval=3):
        super().__init__()
        self.ftp = FTP()
        self.host = host
        self.port=port
        self.username=username
        self.password=password
        self.ftp.connect(host=host, port=port)
        self.ftp.login(username, password)
        self.ftp.set_pasv(False)
        self.remote_dir = remote_dir
        self.work_server = []
        self.server_index = 0
        self.server_num = len(self.work_server)
        self.dispatch_retries = 5
        self.last_remote_files = []
        #ftp_log.info(f"远程 remote_dir：{remote_dir}")
        self.ftp.cwd(remote_dir)
        self.interval = interval
        # ToDo:统计总类型
        self.type_count = {}
        # print(self.ftp.welcome)
        #ftp_log.info(f"self.ftp.welcome： {self.ftp.welcome}")

    def run(self) -> None:
        print(self.remote_dir)
        time.sleep(2)
        while True:
            try:
                print("重新获取大文件"+self.remote_dir)
                # ftp_log.info("重新获取大文件。。。")
                if not self.check_ftp_connection():
                    # ftp_log.info("ftp断开连接，正在重新连接...")
                    self.connect_to_ftp()
                    # ftp_log.info("ftp已重新连接")
                self.fetch_dir()
                time.sleep(self.interval)
                #out_txt_dic("file_type_count.txt", self.type_count)
            except Exception as e:
                # ftp_log.error(f"消费者报错{e}")
                # ftp_log.error(f"消费者报错{traceback.format_exc()}")
                print(traceback.format_exc())

    def fetch_dir(self):
        """
        获取指定远程目录下的所有文件并进行处理
        """
        remote_files = [x for x in self.ftp.nlst() if os.path.splitext(x)[-1] == ".log"]
        # print(self.remote_dir)
        # time.sleep(5)
        # 选择新的文件
        new_files = [x for x in remote_files if x not in self.last_remote_files]
        for file in new_files:
            self.process_remote_log(file)
                
            # count = 0
            # # 如果不成功并且还有重试次数,则继续选择下一个服务
            # while(not self.dispatch_file(self.work_server[self.server_index],file) and count<self.dispatch_retries):
            #     self.server_index = (self.server_index+1)%self.server_num
            #     count+=1
        self.last_remote_files = remote_files

    def process_remote_log(self, remote_file):
        """
        处理单个远程服务器上的日志文件
        """
        local_tmp_log_path = "./logtmp/"+remote_file #生成一个临时日志文件的本地路径local_tmp_log_path，用于在下载日志文件之前先将其下载到临时文件中
        #ftp_log.info(f"开始下载日志，将其重命名：{local_tmp_log_path}")
        try:
            self.fetch_file(remote_file, local_tmp_log_path)
        except:
            #ftp_log.info("获取文件出错")
            return
        #ftp_log.info(f"下载这一步正常执行")
        try:
            file_type = self.extract_file_type(local_tmp_log_path)# 方法从本地临时文件中提取文件类型，并打印提示信息。
        except:
            return
        #ftp_log.info(f"读取log里的内容得到type{remote_file}-------------------------{file_type}")
        # self.increment_type_count(file_type)  # 计数器：将文件类型计数器加1。
        # if file_type not in file_types:
        #     #ftp_log.info(f"读取log里的内容得到type{remote_file}-------------------------{file_type},不在file_types中删除log")
        #     os.remove(local_tmp_log_path)
        #     return
        if file_type != 'gzip':
            self.dispatch_file(remote_file,file_type,"*")
        else:
            try:
                file_name = self.extract_file_name(local_tmp_log_path)  # 方法从本地临时文件中提取文件类型，并打印提示信息。
            except:
                #ftp_log.error(f"读取名称错误位于136行！")
                return
            if 'fasta.gz' in file_name:
                #ftp_log.info(f"filename{file_name}")
                self.dispatch_file(remote_file, file_type,'fasta.gz')
                time.sleep(5)
            elif 'fastq.gz' in file_name:
                #ftp_log.info(f"filename{file_name}")
                self.dispatch_file(remote_file, file_type,'fastq.gz')
                time.sleep(5)
            elif 'fq.gz' in file_name:
                #ftp_log.info(f"filename{file_name}")
                self.dispatch_file(remote_file, file_type, 'fq.gz')
                time.sleep(5)
            elif 'txt.gz' in file_name:
                #ftp_log.info(f"filename{file_name}")
                self.dispatch_file(remote_file, file_type, 'txt.gz')
                time.sleep(1)
    def extract_file_type(self, local_tmp_log_path):
        """
       备用!!! 函数用于从指定的本地临时日志文件中提取文件类型。
        """
        try:
            with codecs.open(local_tmp_log_path, "r", encoding='utf-8') as log_file:
                log_file.readline()
                file_type = log_file.readline().split("\t")[19]
        except UnicodeDecodeError:
            with codecs.open(local_tmp_log_path, "r", encoding='gb2312') as log_file:
                log_file.readline()
                file_type = log_file.readline().split("\t")[19]
        return file_type
    def extract_file_name(self, local_tmp_log_path):
        """
       备用!!! 函数用于从指定的本地临时日志文件中提取文件名称。
        """
        try:
            with codecs.open(local_tmp_log_path, "r", encoding='utf-8') as log_file:
                log_file.readline()
                file_name = log_file.readline().split("\t")[21]
        except UnicodeDecodeError:
            with codecs.open(local_tmp_log_path, "r", encoding='gb2312') as log_file:
                log_file.readline()
                file_name = log_file.readline().split("\t")[21]
        return file_name
    
    def fetch_file(self, remote_file, local_file):
        """
        工具: 获取远程文件并且写入到本地中
        """
        with open(local_file,"wb+") as  file_handle:
            self.ftp.retrbinary("RETR {}".format(remote_file), file_handle.write)
            
    def dispatch_file(self,file,file_type,file_name):
        data={"filename":file,"remote_dir":self.remote_dir}
        #ftp_log.info("成功加载data")
        #ftp_log.info(data)
        print(data)
        try:
            #ftp_log.info(f" 测试转发程序")
            key= file_type+" "+file_name
            if key not in worker:
                return False
            value= worker[key].split("@")
            ip, port = value[0],value[1]
            res = requests.post('http://'+ip+":"+port+"/ftp_file",json=json.dumps(data))
            if res.text == "ok":
                #ftp_log.info("dispatch请求成功")
                return True
            return False
        except:
            #ftp_log.info("dispatch请求失败")
            print("dispatch请求失败")
            #ftp_log.error(f"消费者报错{traceback.format_exc()}")
            return False
    def check_ftp_connection(self):
        try:
            # 发送简单命令，检查链接是否有效
            self.ftp.voidcmd("NOOP")
            self.ftp.pwd()
            #ftp_log.info("检测是否ftp连接状态")

            return True
        except (EOFError,error_perm):
            #ftp_log.error(f"连接出错，{EOFError}")
            return False
    def connect_to_ftp(self):
        """
        重新连接ftp
        """
        # 必须重新创建一个ftp对象
        self.ftp=FTP()
        self.ftp.connect(host=self.host, port=self.port)
        self.ftp.login(self.username, self.password)
        self.ftp.set_pasv(False)
# def Thread1():
#     today_str = get_today_str()
#     dispatcher_http = FtpFileDispatcher("10.62.19.145", 21, "user_download", "ftp_user_2022",
#                                         "/{}/http".format(today_str))
#     dispatcher_http.start()
#     dispatcher_http.join()
# def Thread2():
#     today_str = get_today_str()
#     dispatcher_ftp = FtpFileDispatcher("10.62.19.145", 21, "user_download", "ftp_user_2022",
#                                        "/{}/ftp".format(today_str))
#     dispatcher_ftp.start()
#     dispatcher_ftp.join()

if __name__ == "__main__":
    # TODO 需要填写参数
    read_worker_server_info()
    today_str = get_today_str()
    #today_str = "20230628"
    dispatcher_http = FtpFileDispatcher("10.62.19.145", 21, "user_download", "ftp_user_2022", "/{}/http".format(today_str))
    dispatcher_ftp = FtpFileDispatcher("10.62.19.145", 21, "user_download", "ftp_user_2022", "/{}/ftp".format(today_str))
    # #dispatcher_email = FtpFileDispatcher(host, port, username, password, remote_dir)
    dispatcher_http.start()
    # #dispatcher_email.start()
    dispatcher_ftp.start()
    #
    # #dispatcher_email.join()
    # dispatcher_ftp.join()
    # dispatcher_http.join()
    # p1=Process(target=Thread1)
    # p2=Process(target=Thread2)
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

