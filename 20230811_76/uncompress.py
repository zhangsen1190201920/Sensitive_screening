#用于解压文件，暂时没有用
import logging
import os
import shutil

import patoolib

from tools.log_untils import setup_logging


logger=logging.getLogger("producer")
def uncompress(src_file, dest_dir):
    logger.info(f"进入到解压函数处理过程src_file：{src_file}，dest_dir：{dest_dir}")
    print("src_file::",src_file)
    print("dest_dir",dest_dir)
    try:
        # 如果是gz 或者gzip调用系统中的7z进行解压
        if src_file.endswith(".gz") or src_file.endswith(".gzip"):
            try:
                os.system("7z e {} -o{} -y".format(src_file,dest_dir))
            except Exception as e:
                print(e.with_traceback())
                logger.info(f"{e.with_traceback()}")
                logger.info(f"解压函数gz或者gzip失败，错误原因{e}，即将删除目录")
                shutil.rmtree(dest_dir)  # 删除解压目录,可以非空
            return
        #patoolib.extract_archive(src_file,outdir=dest_dir)
    except Exception as e:
        print("解压出错",e)

        logger.info(f"解压函数失败，错误原因{e}，即将删除目录")
        shutil.rmtree(dest_dir)  # 删除解压目录,可以非空
if __name__ == '__main__':
    uncompress("test.gz", "test")
