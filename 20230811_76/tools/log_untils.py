"""
为想要的python文件输出日志
"""
import logging


def setup_logging(logger_name):
    logger=logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    format =logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
    # 将日志文件输出到文件
    file_handler=logging.FileHandler(f'{logger_name}.log')
    file_handler.setFormatter(format)
    logger.addHandler(file_handler)
    return logger