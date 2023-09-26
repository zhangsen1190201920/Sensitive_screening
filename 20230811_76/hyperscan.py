# 调用hyperScan
from ctypes import cdll
from ctypes import *
import json

hyperscan = cdll.LoadLibrary("./libhyper.so")
hyperscan.get_match_result.restype = c_char_p


def init(id_list, regex_list):
    len_for_c = c_int(len(id_list))
    id_list_for_c = c_int * len(id_list)
    tmp = id_list_for_c()
    for i in range(len(id_list)):
        tmp[i] = id_list[i]
    regex_list_for_c = ((c_char * 1000) * len(id_list))(*[create_string_buffer(s.encode(), 1000) for s in regex_list])
    print("tmp")
    print(tmp)
    print("regex_list_for_c:")
    print(regex_list_for_c)
    print("len_for_c")
    print(len_for_c)
    hyperscan.hyperscan_init(tmp, regex_list_for_c, len_for_c)
    print("hyperscan finish!")


def match(str):
    str_for_c = c_char_p(str)
    res = json.loads(hyperscan.get_match_result(str_for_c).decode())
    result = []
    for key, value in res.items():
        result.append(value)
    return result
