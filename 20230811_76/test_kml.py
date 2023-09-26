
from multiprocessing import Process, JoinableQueue, Queue
from engine.geo_engine import parse_kml

import os
from threading import Thread
from time import ctime, sleep, time

from consumer import consumer
from models import HttpFileDataUnit
from producer import producer
from shared_variable import data_unit_q, write_q
from writer import writer


def consumer_test():
    print("这把执行了")
    consumers = (Thread(target=consumer, args=(data_unit_q, write_q)))
    consumers.start()
    print("写入者这把执行了")
    writers = Thread(target=writer, args=(write_q,))
    writers.start()
    consumers.join()
    writers.join()
if  __name__=="__main__":
    # # lf = "24f579f2d3267e9df6786bd725c03886467bfb8e_193.62.193.138_80_39.170.42.70_6832.log"
    # lf="6f758fc3316de3018039a0b2860df68e6524ea61_43.154.211.119_80_223.220.167.110_54393.log"
    # log_file_path= f"./test/watching_file/log/{lf}.tmp"
    # ld_file= "./test/watching_file/file"
    # # 创建队列以及生产者进程
    # # 使用共享的队列
    # p=Process(target=producer,args=(data_unit_q,"./test/watching_file/log"))
    # # 启动生产者等待完成
    # p.start()
    # #执行改名
    # try:
    #     os.rename(os.path.join(ld_file, lf[:-4] + ".tmp"),
    #               os.path.join(ld_file, lf[:-4]) + '.' + "kml")  # 将xxx.tmp变成xxx
    #     os.rename(log_file_path, log_file_path[:-4])  # 将xxx.log.tmp 变成xxx.log
    #     print(ctime(), "重命名大文件成功")
    #     consumer_test()
    #     print("执行")
    #
    # except Exception as e:
    #     print(ctime(), "重命名大文件出现错误", lf[:-4], "错误，代码为：", e)
    # # 处理的必须放在生产者之前要不然就容易报错
    # p.join()


    if __name__ == '__main__':
        f = open("test/test_kml_file/kml_create.txt", "r")
        res = f.read()
        f.close()
        # print(bytes.fromhex(res))
        result = parse_kml(res)
        print("return value geo engine match result:{}".format(result))
