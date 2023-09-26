import threading
from multiprocessing import Process

from tools.datetime_utils import get_today_str
from db_utils import db
from producer import producer
from shared_variable import file_subscribes, producers, data_unit_q, \
    trx_root, ld_root
from models import FileSubscribeDo, SensitiveModelDo
import schedule
import os

def watch_sm():
    print("watch_sm")
    sql = "select * from sensitive_model where process_state!=4"
    results = list(db.session.execute(sql))
    for res in results:
        print(res)
        process_state = res[8]
        if process_state == 1 or process_state == 2:  # 界面添加修改

            file_subscribes[res[0]] = SensitiveModelDo(res)

            sql = "update sensitive_model set process_state=4 where model_id={}".format(res[0])
            db.session.execute(sql)
            db.session.commit()
            # sql = "select * from file_model_assc where filesubscribe_id={}".format(res[0])

            # asscs = list(db.session.excute(sql))
            # for assc in asscs:
            #     fs_sm_assc[assc[1]] = assc[0]
            #     fs_sm_assc.remove()

        elif process_state == 3:  # 界面删除

            file_subscribes.pop(res[0])

            sql = "delete from sensitive_model where model_id={}".format(res[0])
            db.session.excute(sql)
    db.session.close()


def watch_fs():
    # print("watch_fs")
    sql = "select * from file_subscribe where process_state!=4"
    results = list(db.session.execute(sql))
    for res in results:
        process_state = res[6]
        if process_state == 1 or process_state == 2:  # 界面添加修改
            file_subscribes[res[0]] = FileSubscribeDo(res)
            sql = "update file_subscribe set process_state=4 where filesubscribe_id={}".format(res[0])
            db.session.execute(sql)
            db.session.commit()
            print("修改fs状态成功")
            # sql = "select * from file_model_assc where filesubscribe_id={}".format(res[0])
            # asscs = list(db.session.excute(sql))
            # for assc in asscs:
            #     fs_sm_assc[assc[1]] = assc[0]
            #     fs_sm_assc.remove()

        elif process_state == 3:  # 界面删除
            file_subscribes.pop(res[0])
            sql = "delete from file_subscribe where filesubscribe_id={}".format(res[0])
            db.session.excute(sql)
    db.session.close()


# 每天需要生产者的监听的目录
def update_producer():
    today_str = get_today_str()
    for tag, p in producers:
        if tag == "trx":
            log_path = "{}/{}/log".format(trx_root,get_today_str())
            file_path = "{}/{}/file".format(trx_root,get_today_str())
            if not os.path.exists(log_path):
                os.makedirs(log_path)
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            producers[tag] = Process(target=producer, args=(data_unit_q, "{}/{}/log".format(today_str, trx_root)))
            if p.is_alive():
                p.kill()
            producers[tag].start()
        elif tag in ["email", "http", "ftp"]:
            path = "{}/files/{}/{}".format(ld_root, today_str, tag)
            if not os.path.exsits(path):
                os.makedirs(path)
            producers[tag] = Process(target=producer,
                                     args=(data_unit_q, path))
            if p.is_alive():
                p.kill()
            producers[tag].start()
        else:
            print("未知tag的producer")
    print("{}：已成功更新producer监听目录".format(today_str))


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


# 多一层为了确保调用者不会阻塞
def start_schedule_task():
    threading.Thread(target=start_all).start()


def start_all():
    # todo 间隔时间待定
    schedule.every(3).seconds.do(run_threaded, watch_fs)
    #schedule.every(1).seconds.do(run_threaded, watch_sm)
    schedule.every().day.at("00:00:03").do(run_threaded, update_producer)
    while True:
        schedule.run_pending()
        # time.sleep(1)
