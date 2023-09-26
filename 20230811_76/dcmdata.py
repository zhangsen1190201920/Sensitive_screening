# -*- coding: utf-8 -*-
# @Author  : Wang Zhenghao
# @Email   : 289410265@qq.com
# @Time    : 2022/11/10 20:36
import json
import os

import unicodedata

taglist = []  # 所需的字段的tag，如patient's的tag值为10001000
tagmap = dict()  # tagfile中tag和name+vr的字典

def detect_small_endian(hexcontext:str):
    """
    用于识别 tag 格式是大端还是小端
    根据00020010查找Transfer Syntax UID的值，该tag格式固定，不因大小端改变
    :param hexcontext:
    :return:
    true 表示小端，识别出是小端或无法判定时，返回true
    false 表示大端
    """
    endian_map = dict()
    small ='small'
    big = 'big'
    endian_map['1.2.840.10008.1.2.1\x00'] = small
    endian_map['1.2.840.10008.1.2.99\x00'] = small
    endian_map['1.2.840.10008.1.2.2\x00'] = big
    tag_vr = '020010005549'
    tag_index = hexcontext.find(tag_vr,0)
    if tag_index == -1 :#该tag无法判定，默认为小端
        return True
    else:
        size_index = tag_index+12
        sizehex = hexcontext[size_index:size_index + 4]
        lowbit = sizehex[0:2]  # 低位
        highbit = sizehex[2:4]  # 高位
        size = int(lowbit, 16) + (int(highbit, 16) << 8)
        dataindex = tag_index+16
        datahex = hexcontext[dataindex:dataindex + size * 2]
        try:
            databytes = bytes.fromhex(datahex)
            data = databytes.decode('utf-8')

        except:
            return True#data无法解码，可能是数据丢失导致，判定为小端
        if data in endian_map.keys():
            if endian_map[data] == 'small':
                return True
            elif endian_map[data] == 'big':
                return False
        else:
            return True#data不在endian中的键中，默认返回小端


def parsedata(hexcontext):
    result = []
    for tag, value in tagmap.items():
        resultitem = dict()  # 返回的一个单元
        name, vr = value
        small_endian = detect_small_endian(hexcontext)

        if small_endian:  # 判定tag是小端模式
            transfer_tag = tag[2:4] + tag[0:2] + tag[6:8] + tag[4:6]  # 转换成小端格式
        else:  # tag是大端模式
            transfer_tag = tag
        tag_vr = transfer_tag + vr.encode('utf-8').hex()
        # print(tag_vr)
        tagindex = hexcontext.find(tag_vr, 0)
        long = 1  # 长标志匹配
        # print(tagindex)
        if tagindex == -1:  # 对长标志匹配失败，证明不包含tag_var字段
            tagindex = hexcontext.find(transfer_tag, 0)
            long = 0  # 短标志匹配
            if tagindex == -1:  # 对短标志匹配失败，证明不包含tag字段
                data = 'not found'
                code = '-1'
                resultitem['code'] = code
                resultitem['name'] = name
                resultitem['data'] = data
                result.append(resultitem)
                continue
        if long == 1:
            sizeindex = tagindex + 12
        elif long == 0:
            sizeindex = tagindex + 8
        sizehex = hexcontext[sizeindex:sizeindex + 4]
        # print('sizehex:'+str(sizehex))
        if small_endian:  # 小端
            lowbit = sizehex[0:2]  # 低位
            highbit = sizehex[2:4]  # 高位
        else:  # 大端
            lowbit = sizehex[2:4]  # 低位
            highbit = sizehex[0:2]  # 高位
        if len(highbit) < 2:  # 高位不足2,说明sizehex及其往后数据全部丢失
            size = 0
            data = 'data lost'
            code = '-3'
        else:
            size = int(lowbit, 16) + (int(highbit, 16) << 8)
            if size == 0:  # tag字段长度为0
                data = ''
                code = '0'
            elif size > 100:  # 长度过大,说明出现数据丢失
                data = 'data lost'
                code = '-3'
            else:
                # print('size:'+str(size))
                dataindex = tagindex + 16
                datahex = hexcontext[dataindex:dataindex + size * 2]
                if len(datahex) < size * 2:  # datahex长度不足，说明data之后数据全部丢失
                    data = 'data lost'
                    code = '-3'
                # print(datahex)
                else:
                    databytes = bytes.fromhex(datahex)
                    try:
                        data = databytes.decode('utf-8')  # 尝试utf8解码
                        if not data.isprintable():  # 如果解码出的字符串包含不可打印字符，则从第一个不可打印字符开始，丢弃后面所有内容
                            for i, ch in enumerate(data):
                                if unicodedata.category(ch) == 'Cc':  # 找到控制类型字符
                                    control = i
                                    break
                            data = data[:control]
                        code = '0'
                    except:  # 包含不满足utf-8编码格式的字符串(可能是由于数据丢失导致，也可能是真正data就是无法utf8解码)
                        # print(f'fail to decode tag{tag},{name}')
                        # print(traceback.format_exc())
                        try:  # 尝试使用gbk解码
                            data = databytes.decode('gbk')  # 尝试gbk解码
                            if not data.isprintable():  # 如果解码出的字符串包含不可打印字符，则从第一个不可打印字符开始，丢弃后面所有内容
                                for i, ch in enumerate(data):
                                    if unicodedata.category(ch) == 'Cc':  # 找到控制类型字符
                                        control = i
                                        break
                                data = data[:control]
                            code = '0'
                        except:  # 非utf8和gbk编码，判定为数据丢失
                            data = datahex
                            code = '-2'

        resultitem['code'] = code
        resultitem['name'] = name
        resultitem['data'] = data.replace("'", ' ').replace('"',' ')
        result.append(resultitem)
    # print(json.dumps(result))
    return json.dumps(result)


def inittaglist(tagfile):
    """
    读取tagfile,初始化所需字段列表
    :param tagfile: 文件名,包含所需字段列表
    :return:
    """
    global taglist, tagmap
    with open(tagfile) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            tag = line.split(',')[0]
            name_vr = line.split(',')[1:]
            tagmap[tag] = name_vr
        # print(tagmap)


if __name__ == '__main__':
    inittaglist(r'taglist.txt')
#    filelist = os.listdir(r'C:\myfile\lab\dcm\file\20221110')
#    for file in filelist:
#        absfile = os.path.join(r'C:\myfile\lab\dcm\file\20221110',file)
#        print(parsedata(absfile))
    print(parsedata(r'C:\myfile\lab\dcm\file\GH364.dcm'))
    # print(parsedata(r'C:\myfile\lab\dcm\bugfile\datalost.dcm'))
    # print(parsedata(r'D:\E\lab\dcm\bugfile\1667485252573-down-287_1.3.46.670589.33.1.63802576699886872600001.4888705277501383874.dcm'))
