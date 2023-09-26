import unittest



def extract_file_type( local_tmp_log_path):
    """
    函数用于从指定的本地临时日志文件中提取文件类型。
    """
    try:
        with open(local_tmp_log_path, "r") as log_file:
            log_file.readline()
            file_type = log_file.readline().split("\t")[19]
        return file_type
    except Exception as err:
       print("err",err)
if __name__ == '__main__':
    file_type=extract_file_type(local_tmp_log_path="test/test_encode_file/846af6e1aa2239de6f92e0352ebd9c13db9deda7_193.62.193.138_80_101.6.120.41_47752.log")
    print(file_type)
