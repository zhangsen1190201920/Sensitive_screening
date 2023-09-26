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
from threading import Thread
from tools.log_untils import setup_logging
from tools.out_text_utils import out_txt_dic
from multiprocessing import Process, JoinableQueue, Queue

# TODO 两层压缩 解压之后可能带文件夹和多个文件, 层数不定, 需要处理
# 输出到ftp_clent.log
ftp_log=setup_logging("ftp")

class FtpProcessor(threading.Thread):
    bio_types = ['fastq', 'fasta', "vcf", "sam", "gtf", "gff"]
    file_types = ["doc", "docx", "xls", "xlsx", "ppt", "pptx", "pdf", "txt", "kml", "dcm", 'zip', "gzip"]

    def __init__(self, host, port, username, password, local_dir, fileq: JoinableQueue, interval=3):
        super().__init__()
        self.ftp = FTP()
        self.host = host
        self.port=port
        self.username=username
        self.password=password
        self.ftp.connect(host=host, port=port)
        self.ftp.login(username, password)
        self.ftp.set_pasv(False)
        self.local_dir = local_dir
        self.ld_file = "{}/file".format(self.local_dir)
        self.ld_log = "{}/log".format(self.local_dir)
        self.ld_error = "{}/error".format(self.local_dir)
        self.fileq = fileq
        self.ensure_local_directories_exist()
        self.interval = interval
        # ToDo:统计总类型
        self.type_count = {}
        # print(self.ftp.welcome)
        logging.info(f"self.ftp.welcome： {self.ftp.welcome}")

    def fetch_file(self, remote_file, local_file):
        """
        工具: 获取远程文件并且写入到本地中
        """
        with open(local_file,"wb+") as  file_handle:
            self.ftp.retrbinary("RETR {}".format(remote_file), file_handle.write)

    def update_date(self,remote_dir):
        """
        更新日期
        """
        
        if remote_dir not in self.local_dir:
            self.local_dir = "/home/k1816/hzh/big_file_store"+remote_dir
            self.ld_file = "{}/file".format(self.local_dir) # 表示将file文件放在self.local_dir目录中。
            self.ld_log = "{}/log".format(self.local_dir)
            if not os.path.exists(self.local_dir):
                os.makedirs(self.local_dir) # 创建本地目录
                os.makedirs(self.ld_file)
                os.makedirs(self.ld_log)

    def check_ftp_connection(self):
        try:
            # 发送简单命令，检查链接是否有效
            self.ftp.connect(host=self.host, port=self.port)
            self.ftp.login(self.username, self.password)
            self.ftp.set_pasv(False)
            self.ftp.voidcmd("NOOP")
            self.ftp.pwd()
            ftp_log.info("检测是否ftp连接状态")
            return
        except (EOFError,error_perm):
            ftp_log.error(f"连接出错，{EOFError}")
            return
    def connect_to_ftp(self):
        """
        重新连接ftp
        """
        # 必须重新创建一个ftp对象
        self.ftp=FTP()
        self.ftp.connect(host=self.host, port=self.port)
        self.ftp.login(self.username, self.password)
        self.ftp.set_pasv(False)
    def ensure_local_directories_exist(self):
        """
        确保本地目录以及相关的文件和日志目录存在，如果不存在，则创建它们
        """
        for directory in [self.ld_file,self.ld_log,self.ld_error]:
            if not os.path.exists(directory):
                ftp_log.info(f"{directory}路径不存在创建路径")
                os.makedirs(directory)

    def is_log_failed(self, remote_file):
        """
        检查日志文件是否有错误
        """
        error_file = os.path.join(self.ld_error, "error_reasons.txt")
        if os.path.exists(error_file):
            with open(error_file, "r") as f:
                for line in f:
                    if remote_file in line:
                        return True
        return False

    def write_error_reason(self, remote_file, error_reason):
        """
        写入错误原因
        """
        error_file = os.path.join(self.ld_error, "error_reasons.txt")
        with open(error_file, "a") as f:
            f.write("{} --- {}\n".format(remote_file, error_reason))

    def is_log_downloaded(self, remote_file):
        """
        函数用于检查指定的远程日志文件是否已经被下载到本地的日志目录中
        """
        return os.path.exists("{}/{}".format(self.ld_log, remote_file))

    def is_tmp_file_downloaded(self, remote_file):
        """
        函数用于检查指定的远程日志文件对应的临时文件是否已经被下载到本地的日志目录中。
        """
        return os.path.exists("{}/{}".format(self.ld_log, remote_file + ".tmp"))

    # def extract_file_type(self, local_tmp_log_path):
    #     """
    #     函数用于从指定的本地临时日志文件中提取文件类型。
    #     """
    #     with open(local_tmp_log_path, "r") as log_file:
    #         log_file.readline()
    #         file_type = log_file.readline().split("\t")[19]
    #     return file_type

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

    def increment_type_count(self, file_type):
        if file_type in self.type_count:
            self.type_count[file_type] += 1
        else:
            self.type_count[file_type] = 1

    def cleanup_failed_log_download(self, local_tmp_log_path):
        """
        它的作用是清理下载失败的临时日志文件。
        """
        if os.path.exists(local_tmp_log_path):
            dest = os.path.join(self.ld_error, os.path.basename(local_tmp_log_path)) #os.path.basename()函数用于获取指定路径的文件名（不包含目录部分）
            shutil.move(local_tmp_log_path, dest)
            # os.remove(local_tmp_log_path)
    def cleanup_failed_large_file_download(self, remote_file):
        os.remove(os.path.join(self.ld_log, remote_file + ".tmp"))
        if os.path.exists("{}/{}".format(self.ld_file, remote_file[:-4] + ".tmp")):
            # os.remove(os.path.join(self.ld_file, remote_file[:-4] + ".tmp"))
            dest = os.path.join(self.ld_error, remote_file[:-4] + ".tmp")
            shutil.move(os.path.join(self.ld_file, remote_file[:-4] + ".tmp"), dest)


    def download_and_process_large_file(self, remote_file, file_type):
        """
        它的作用是下载并处理可能的大文件
        """
        try:
            # print(time.ctime(), )
            ftp_log.info(f"{remote_file[:-4]}大文件开始下载")
            self.fetch_file(remote_file[:-4], os.path.join(self.ld_file, remote_file[:-4] + ".tmp"))
            print(time.ctime(), remote_file[:-4], "-------------------------", "大文件下载成功")
        except Exception as e:
            # print(time.ctime(), "下载大文件失败", remote_file[:-4], "错误，代码为：", e)
            ftp_log.error( f"下载大文件失败{remote_file[:-4]} 错误，代码为：{e}")
            self.cleanup_failed_large_file_download(remote_file)
            return

        self.rename_downloaded_files(remote_file)

    
    def rename_downloaded_files(self, remote_file):
        """
        重命名已下载的文件。
        """
        try:
            file_type=self.extract_file_type(os.path.join(self.ld_log, remote_file + ".tmp"))
            os.rename(os.path.join(self.ld_file, remote_file[:-4] + ".tmp"),
                      os.path.join(self.ld_file, remote_file[:-4]+"."+file_type))
            os.rename(os.path.join(self.ld_log, remote_file + ".tmp"), os.path.join(self.ld_log, remote_file))
            # print(time.ctime(), "重命名大文件成功")
            ftp_log.info(f"{remote_file[:-4]+file_type}重命名大文件成功")
        except Exception as e:
            # print(time.ctime(), "重命名大文件出现错误", remote_file[:-4], "错误，代码为：", e)
            ftp_log.error(f"重命名大文件出现错误{remote_file[:-4]}错误，代码为：{e}")
            self.cleanup_failed_large_file_download(remote_file)

    def process_remote_log(self, remote_file):
        """
        处理单个远程服务器上的日志文件
        """
        if not self.is_log_downloaded(remote_file) and not self.is_tmp_file_downloaded(remote_file):
            local_tmp_log_path = os.path.join(self.ld_log, remote_file + ".tmp") #生成一个临时日志文件的本地路径local_tmp_log_path，用于在下载日志文件之前先将其下载到临时文件中
            ftp_log.info(f"开始下载日志，将其重命名：{local_tmp_log_path}")
            try:
                self.fetch_file(remote_file, local_tmp_log_path)
                ftp_log.info(f"下载这一步正常执行")
                file_type = self.extract_file_type(local_tmp_log_path)# 方法从本地临时文件中提取文件类型，并打印提示信息。
                ftp_log.info(f"读取log里的内容得到type{remote_file}-------------------------{file_type}")
                self.increment_type_count(file_type)  # 计数器：将文件类型计数器加1。

            except Exception as e:
                ftp_log.error(f"处理日志文件：{remote_file}错误，代码为：{e}", )
                self.cleanup_failed_log_download(local_tmp_log_path)
                self.write_error_reason(remote_file, str(e))
                return

            self.download_and_process_large_file(remote_file, file_type)

    def run(self) -> None:
        #p1=Thread(target=self.command1)
        #p1.start()
        while True:
            ftp_log.info(f"new ftp file will come in!")
            file_content = self.fileq.get()
            remote_dir=file_content["remote_dir"]
            self.check_ftp_connection()
            self.ftp.cwd(remote_dir)
            file=file_content["filename"]
            #self.update_date(remote_dir)
            self.ensure_local_directories_exist() # 确保本地目录以及相关的文件和日志目录存在，如果不存在，则创建它们
            if not self.is_log_failed(file): # 如果log也不在本地的error的日志文件中错误中
                self.process_remote_log(file)
            out_txt_dic("file_type_count.txt", self.type_count)
            self.ftp.quit()

    def command1(self):
        while True:
            self.check_ftp_connection()
            time.sleep(5)