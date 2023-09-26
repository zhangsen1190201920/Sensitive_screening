import os

from consumer import consumer
from tools.datetime_utils import get_today_str
from writer import writer

from producer import producer
from threading import Thread
from shared_variable import data_unit_q, write_q, ftp_processors, trx_root, \
    producers, consumer_num, consumers, writers
from tools.log_untils import setup_logging
processor_logger=setup_logging("processor")
def start_process():

    for client in ftp_processors:
        # 每个ftp——client对应一个目录，每个目录应该有一个生产者
        tag = client.local_dir.split('/')[-1]  # tag = http email ftp
        processor_logger.info(f"tag{tag},{client.local_dir}")
        producers[tag] = Thread(target=producer, args=(data_unit_q, client.ld_log))

    # 对应天融信的ftp目录
    log_path = "{}/{}/log".format(trx_root,get_today_str())
    file_path = "{}/{}/file".format(trx_root,get_today_str())
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    producers["trx"] = Thread(target=producer, args=(data_unit_q, "{}/{}/log".format(trx_root, get_today_str())))
    try:
        for i in range(consumer_num):
            consumers["c{}".format(i)] = (Thread(target=consumer, args=(data_unit_q, write_q)))
            writers["w1"] = (Thread(target=writer, args=(write_q,)))
            # writers["w2"] = (Thread(target=sender, args=(write_q,)))
            for _, w in writers.items():
                w.start()
            for _, c in consumers.items():
                c.start()
            for _, p in producers.items():
                p.start()
            print("all process started!")

    except Exception as  err:
        print("启动会出错errerrerrerrerrerrerrerrerrerrerrerrerr",err)

