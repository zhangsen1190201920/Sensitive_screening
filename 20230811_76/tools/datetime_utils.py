# 处理时间相关的工具函数
from datetime import date,time,datetime
import time

# 20220702
def get_today_str():
    return date.today().strftime("%Y%m%d")
#返回
def get_date_time():

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def is_count_time():
    """
    是否在统计的时间段内,想看时间改时间就可以
    """
    # 获取当前时间
    now=datetime.now()
    now_timestamp=time.mktime(now.timetuple())
    # 记录统计时间
    day_start_time=datetime(now.year,now.month,day=14,hour=0,minute=0,second=0)
    # 获取时间戳
    start_timestamp=time.mktime(day_start_time.timetuple())
    # 记录结束统计时间
    day_end_time=datetime(now.year,now.month,day=14,hour=23,minute=59,second=59)
    # 获取时间戳
    end_timestamp=time.mktime(day_end_time.timetuple())

    if start_timestamp<=now_timestamp<=end_timestamp:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!===在时间段中”！！！！！！！！！！！！！！！！！！！！")
        return True
    else:
        return  False

