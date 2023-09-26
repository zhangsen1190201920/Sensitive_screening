import codecs
import logging
import shutil
import traceback
from multiprocessing import Process, JoinableQueue, Queue
from time import ctime

import textract
import os

from tools.log_untils import setup_logging
from tools.out_text_utils import out_txt_dic
from uncompress import uncompress
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, PatternMatchingEventHandler

from models import HttpFileDataUnit, EmailFileDataUnit, FtpFileDataUnit, TrxFileDataUnit
from shared_variable import bio_types, able_deal_file_type, file_types,need_to_handle

#输出到 producer.log
logger=setup_logging("producer")
type_count={}
class MyHandler(PatternMatchingEventHandler):
    """
    用于监控文件系统事件
    q：用于生产者跟消费者的通信通道
    patterns：指定要匹配的文件名模式
    ignore_patterns：忽略匹配的
    ignore_directories：是否忽略目录事件
    case_sensitive：文件匹配是否需要大小写
    """

    def __init__(self, q: JoinableQueue, patterns=None, ignore_patterns=None,
                 ignore_directories=False, case_sensitive=False):
        super().__init__(patterns=patterns, ignore_patterns=ignore_patterns,
                         ignore_directories=ignore_directories, case_sensitive=case_sensitive)
        self.q = q

    # def on_created(self, event):
    #     if event.src_path.endswith(".tmp"):
    #         return
    #     print("got file:{}".format(event.src_path))
    #     filepath = os.path.abspath(event.src_path)
    #     dir_path = os.path.dirname(filepath)
    #     filename = os.path.basename(filepath)
    #     deal_file(self.q, dir_path, filename)

    def on_moved(self, event):
        """
        文件被移动或者是重命名时有用，目前来看
        """
        # print("检测本地执行了移动或者改名")
        # print("got file:{}".format(event.dest_path))
        logger.info("========================开始==========================================检测本地执行了移动或者改名,got file:{}".format(event.dest_path))
        filepath = os.path.abspath(event.dest_path)
        dir_path = os.path.dirname(filepath)
        filename = os.path.basename(filepath)
        deal_file(self.q, dir_path, filename)




def producer(q: JoinableQueue, path):
    # 处理已经存在的数据
    # print("开始监听{}".format(path))
    logger.info("开始监听{}".format(path))
    print("开始监听{}".format(path))
    filenames = os.listdir(path)
    # for filename in filenames:
    #     if not need_to_handle(filename):
    #         continue
    #     deal_file(q, path, filename)

    event_handler = MyHandler(q=q, ignore_directories=True)
    observer = Observer()
    # 将事件增加   recursive=False是否递归监视
    observer.schedule(event_handler, path=path, recursive=False)
    observer.start()
    observer.join()
    logger.info("关闭监听")


def deal_file(q, path, log_file):
    """
    处理日志文件，将处理好的数据放入队列
    """
    try:
        # path 为log_file的路径
        logger.info(f"处理{log_file}")
        lines=get_lines(os.path.join(path, log_file))
        if len(lines) == 0:
            return
        log_type = "bw"  # 标志这个log是哪个接口产生的，报文引擎(bw)或者天融信(trx)，
        if not lines[0].startswith("#"):  # 报文引擎第一行是标题行，以#开头，如果日志文件不是# 那就是trx给的如果不是就是bw给的
            log_type = "trx"
        if log_type == "bw":
            # 报文引擎一个log文件里只有一个文件日志
            #Change: 如此判断不正确
            # file_type = os.path.splitext(raw_filename)
            file_type=lines[1].split("\t")[19]
            file_name = lines[1].split("\t")[21]
            increment_type_count(file_type)
            out_txt_dic("file_name_count.txt", type_count)
            logger.info(f"切割之前的内容{lines[1]},{file_type}")
            raw_filename = log_file[:-4]+'.'+file_type  # 获取原始文件名,得到的是 xxxx.zip 或者xxx。kml
            logger.info(f"解压之前文件类型：{file_type}")

            raw_file_path = os.path.join(path.replace("log", "file"), raw_filename) # 原始文件路径 raw_file_path： xxxx/xxxx/xxxx.zip 或者xxx。kml
            # 如果是压缩文件先解压
            if file_type in ["zip","rar","7z","gzip","gz"]:
                logger.info(f"{raw_file_path}是压缩文件!进入解压过程")
                date = raw_file_path.split("/")[-4]
                sendtype=raw_file_path.split("/")[-3]
                # print("raw_file_path::",raw_file_path)
                dest_dir = '/home/k1816/hzh/uncompressed/{}/{}/{}'.format(date,sendtype,raw_filename) # dest_dir：/home/k1816/hzh/uncompressed/{日期}/http/{}
                # print("dest_dir",dest_dir)
                logger.info(f"解压到的路径：{dest_dir}")
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                uncompress(raw_file_path,dest_dir)
                # TODO 暂定压缩文件内只有一个文件
                files = os.listdir(dest_dir)
                logger.info(f"解压后的文件名称{files}")
                if len(files) != 1:
                    logger.error(f"解压后的多个文件{files}")
                    return
                # 以下三个函数，类似于  raw_filename_in_log：AADYUZ01.cds.gz file_type_in_log_last：gz
                raw_filename_in_log = lines[1].split("\t")[21]  # 取出来原始文件名
                file_type_in_log_last = raw_filename_in_log.split(".")[-1]
                file_type_in_log = raw_filename_in_log.split(".")[-2]
                # 判断到底是不是需要二次解压，只有文件名与本身的文件名相同才需要解压
                # if files[0] == log_file[:-4]:
                #     logger.info(f"{files}进入二次解压")
                #     raw_filename = lines[1].split("\t")[21]  # 取出来原始文件名
                #     file_type = raw_filename.split(".")[-1]
                #     two_uncompress(files,raw_file_path,raw_filename,file_type)
                #     logger.info(f"{files}二次解压结束")
                # 解压后的文件类型
                type_file=os.path.splitext(files[0])[-1].split(".")[-1] #os.path.splitext(files[0])[-1]得到的都是.doc,得到的是.split(".")[-1]，doc
                logger.info(f"解压后处理前的文件类型{type_file}")
                if 'fasta.gz' in file_name and 'fasta' not in type_file:
                    os.rename(os.path.join(dest_dir,files[0]),os.path.join(dest_dir,files[0]+".fasta"))
                    files[0]=os.path.join(dest_dir,files[0]+".fasta")
                elif "fastq.gz" in file_name and 'fastq' not in type_file:
                    os.rename(os.path.join(dest_dir, files[0]), os.path.join(dest_dir,files[0] + ".fastq"))
                    files[0] = os.path.join(dest_dir, files[0] + ".fastq")
                elif "fq.gz" in file_name :
                    os.rename(os.path.join(dest_dir, files[0]), os.path.join(dest_dir,files[0] + ".fastq"))
                    files[0] = os.path.join(dest_dir, files[0] + ".fastq")
                elif "txt.gz" in file_name and 'txt' not in type_file:
                    os.rename(os.path.join(dest_dir, files[0]), os.path.join(dest_dir, files[0] + ".txt"))
                    files[0] = os.path.join(dest_dir, files[0] + ".txt")
                type_file = os.path.splitext(files[0])[-1].split(".")[-1]  # os.path.splitext(files[0])[-1]得到的都是.doc,得到的是.split(".")[-1]，doc
                logger.info(f"解压后处理后的文件类型{type_file}")

                    #ToDo 如果是word pdf txt 以及没有的后缀名，暂时不处理
                #
                # if(type_file not in file_types and  raw_filename_in_log=="NULL"): #若得到的类型不在当前能处理的类型中丢弃,
                #     logger.info(f"该文件类型为 {type_file}")
                #     # ToDo:删除本地文件的操作
                #     return
                # if (file_type_in_log_last =="gz" and file_type_in_log not in file_types):  # 对应第二种情况,
                #     logger.info(f"第二种情况：该文件名称为 {raw_filename_in_log}处理不了即将删除")
                #     shutil.rmtree(dest_dir)  # 删除解压目录,可以非空
                #     # ToDo:删除本地文件的操作
                #     return
                raw_file_path = os.path.join(dest_dir,files[0]) #解压之后文件的真实路径
                logger.info(f"解压之后文件的真实路径{raw_file_path}")
                os.remove(os.path.join(path.replace("log", "file"), raw_filename))
            old_path=os.path.join(path.replace("log", "file"), raw_filename)
            logger.info(f"解压之前文件路径：{old_path}")
            logger.info(f"要处理的大文件文件路径 {raw_file_path}")
            log_line = lines[1]  # 第二行才是真正的日志
            data_unit = None

            # ToDo:在真正执行时打开下边注释
            if "http" in path:
                data_unit = HttpFileDataUnit(log_line, raw_file_path)
                logger.info(f"解析http主表内容为{vars(data_unit)}")
                logger.info("=================================结束=====================================================")
            elif "email" in path:
                data_unit = EmailFileDataUnit(log_line, raw_file_path)
            elif "ftp" in path:
                data_unit = FtpFileDataUnit(log_line, raw_file_path)
                logger.info(f"解析ftp主表内容为{vars(data_unit)}")
                logger.info("=================================结束=====================================================")
            q.put(data_unit)
        elif log_type == "trx":
            # 天融信每个日志里会包含多个文件的日志
            for line in lines:
                raw_filename = line.split("\t")[6]
                file_type = os.path.splitext(raw_filename)
                raw_file_path = os.path.join(path.replace("log", "file"), raw_filename)
                # 如果是压缩文件先解压
                if file_type in ["zip","rar","7z"]:
                    dest_dir = 'uncompressed/{}'.format(raw_filename)
                    uncompress(raw_file_path,dest_dir)
                    # TODO 暂定压缩文件内只有一个文件
                    files = os.listdir(dest_dir)
                    if len(files) != 1:
                        print("解压之后多个文件!")
                        print(files)
                        return
                    # 如果是生物直接丢弃
                    if(os.path.splitext(files)[-1] in  bio_types):return
                    raw_file_path = os.path.join(dest_dir,files)

                data_unit = TrxFileDataUnit(line, raw_file_path)
                q.put(data_unit)
    except Exception as e:
        # print("Error:处理文件{}出错\n{}".format(f.name, e))
        logger.error("Error:处理文件{}出错\n{}".format(log_file, e))
        logger.error(f"{traceback.print_exc()}")
def get_lines(local_tmp_log_path):
    try:
        with codecs.open(local_tmp_log_path, "r", encoding='utf-8') as log_file:
            lines = log_file.readlines()
    except UnicodeDecodeError:
        with codecs.open(local_tmp_log_path, "r", encoding='gb2312') as log_file:
            lines = log_file.readlines()
    return lines
# 处理二次解压的情况
def two_uncompress(files,raw_file_path,raw_filename,file_type):
    """
    files:解压以后的文件名
    raw_file_path:一次解压以后大文件所在的路径 /home/uncompon/xxxxx
    raw_filename：原始文件名
    file_type:传入文件的真实
    """
    try:
        logger.info(f"{files[0]}的原始文件名：{raw_filename}，解压之前的类型{file_type}")
        if file_type in ["zip", "rar", "7z", "gzip", "gz"]:
            logger.info(f"{raw_file_path}是压缩文件!进入解压过程")
            # print("raw_file_path::",raw_file_path)
            dest_dir = 'uncompressed/{}'.format(raw_filename)  # dest_dir：uncompressed/asdasd.tar.gz
            # print("dest_dir",dest_dir)
            logger.info(f"解压到的路径：{dest_dir}")
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
                uncompress(raw_file_path, dest_dir)
            # TODO 暂定压缩文件内只有一个文件
            files = os.listdir(dest_dir)
            logger.info(f"解压后的文件名称{files}")
            if len(files) != 1:
                logger.error(f"解压后的多个文件{files}")
                return
    except Exception as  err:
        logger.error(f"二次解压失败，原因{err}")



def increment_type_count(file_type):
    if file_type in type_count:
        type_count[file_type] += 1
    else:
        type_count[file_type] = 1





