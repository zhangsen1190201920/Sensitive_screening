
def out_txt_dic(file_name,dic):
    """
    将字典类型写出文件
    """
    try:
        with open(file_name,"w") as  f:
            for key,value in dic.items():
                f.write(f"{key}:{value}\n")
        print("写入文件成功")
    except Exception as  e:
        print("写入txt失败",e)


# 写入错误日志
def out_txt_str(file_name,stringArr):
    """
    将字符串数组类型写出文件
    """
    try:
        with open(file_name,"w") as  f:
            for value in stringArr:
                f.write(f"value:{value}\n")
        print("写入文件成功")
    except Exception as  e:
        print("写入txt失败",e)
