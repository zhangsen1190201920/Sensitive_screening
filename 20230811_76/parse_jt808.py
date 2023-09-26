# -*- coding: utf-8 -*-
import re
import sys
import binascii
import os

mess_id = '0200'
# mess_ids = sys.argv[1]

# fr_path = r'%s'%(sys.argv[2])
# fr = open(fr_path, 'r')
fw_erro = open('/home/k1816/fs/erro.txt','a') # TODO 修改一下日志目录
len_error = open('/home/k1816/fs/lenerro.txt','a') # TODO 修改一下日志目录

def alarm_type_value(vals):
    out_res = ''
    vals = '0' * (32 - len(vals)) + vals
    val = ''
    for i in range(len(vals)-1,-1,-1):
        val += vals[i]
    print
    ls = ['确认紧急告警', '', '', '确认危险预警', '', '', '', '', '', '',
          '', '', '', '', '', '', '', '', '', '', '确认进出区域报警', '确认进出路线报警',
          '确认路段行驶时间不足或过长告警', '', '', '', '', '确认车辆非法点火报警', '确认车辆非法位移报警', '', '', '']
    for l1, l2 in zip(val, ls):
        if l1 == '0' and l2 != '':
            out_res += '正常\t'
        elif l2 == '':
            continue
        elif l1 == '1':
            out_res += (l2 + '\t')

    return out_res[:-1]


def bjbz_value(vals):
    out_res = ''
    vals = '0' * (32 - len(vals)) + vals
    val = ''
    for i in range(len(vals)-1,-1,-1):
        val += vals[i]

    ls = ['紧急告警', '超速报警', '疲劳驾驶', '危险驾驶', 'GNSS模块发生故障', 'GNSS天线未接获被剪断', 'GNSS天线短路', '终端主电源欠压', '终端主电源掉电', '终端LCD或显示器故障',
          'TTS模块故障', '摄像头故障', '道路运输证IC卡模块故障', '超速预警', '疲劳驾驶', '', '', '', '当天累计驾驶超时', '超时停车', '进出区域', '进出路线',
          '路段行驶时间不足或过长', '路线偏离报警', '车辆VSS故障', '车辆油量异常', '车辆被盗', '车辆非法点火', '车辆非法位移', '碰撞预警', '侧翻预警', '非法开门报警']
    for l1, l2 in zip(val, ls):
        if l1 == '0' and l2 != '':
            out_res += '正常\t'
        elif l2 == '':
            continue
        elif l1 == '1':
            out_res += (l2 + '\t')

    return out_res[:-1]


def stuat_value(vals):
    out_res = ''
    vals = '0' * (32 - len(vals)) + vals
    val = ''
    for i in range(len(vals)-1,-1,-1):
        val += vals[i]
    #print(val)
    ls1 = [{'0': '关', '1': '开'}, {'0': '未定位', '1': '定位'}, {'0': '北纬', '1': '南纬'}, {'0': '东经', '1': '西经'},
           {'0': '运营', '1': '停运'}, {'0': '否', '1': '是'}, '', '',
           {'00': '空车', '01': '半载', '10': '保留', '11': '满载'}, '', {'0': '正常', '1': '断开'},
           {'0': '正常', '1': '断开'}, {'0': '解锁', '1': '加锁'}, {'0': '关', '1': '开'},
           {'0': '关', '1': '开'}, {'0': '关', '1': '开'}, {'0': '关', '1': '开'},
           {'0': '关', '1': '开'}, {'0': '未使用', '1': '使用'},
           {'0': '未使用', '1': '使用'}, {'0': '未使用', '1': '使用'},
           {'0': '未使用', '1': '使用'}, '', '', '', '', '', '', '', '', '', '']

    for i in range(0, 32):
        if i == 2:
            lat_diredction = ls1[i][val[i]]
        if i == 3:
            long_diredction = ls1[i][val[i]]
        if i == 8:
            v = val[i:i + 2]
        elif i == 9:
            continue
        else:
            v = val[i]
        if ls1[i] != '':
            out_res += (str(ls1[i][v]) + '\t')

    return out_res[:-1], lat_diredction, long_diredction


def date_value(val, start_time):
    year = '20' + val[0:2] + '-' + val[2:4] + '-' + val[4:6]
    mother = val[6:12]
    time_tf = 'T'
    if year == start_time[0:8]:
        for i in mother:
            if int(i, 16) <= 0 and int(i, 16) >= 9:
                time_tf = 'F'

    if time_tf == 'T':
        alarm_date = '20' + val[0:2] + '-' + val[2:4] + '-' + val[4:6] + ' ' + val[6:8] + ':' + val[8:10] + ':' + val[
                                                                                                                  10:12]
    else:
        alarm_date = ''

    return alarm_date

def parse_8203(cc):
    alarm_mess_number = cc[0:4]
    alarm_type = tuat_value(bin(int(cc[4:12], 16))[2:])

    message_body = '\t' + alarm_mess_number + '\t' + alarm_type

    return message_body


def parse_8202(cc):
    date_interval = cc[0:4]
    date_validity = cc[4:12]

    message_body = '\t' + date_interval + '\t' + date_validity

    return message_body


def parse_0201(cc):
    response_number = cc[0:4]
    response_num = int(cc[4:6],16)
    val_ls = cc[6:]
    xjm = cc[-2:]

    num = 0
    cs_dict = {}
    if response_num != '':
        for i in range(0, len(val_ls)):
            if len(cs_dict) != response_num:
                cs_id = val_ls[i:i + 4]
                cs_length = val_ls[i + 4:i + 4 + 2]
                if cs_length == '':
                    cs_length = '0'
                try:
                    cs_dict[cs_id].append(val_ls[i + 4 + 2:i + 4 + 2 + (int(cs_length, 16) * 2)])
                except:
                    cs_dict[cs_id] = list()
                    cs_dict[cs_id].append(val_ls[i + 4 + 2:i + 4 + 2 + (int(cs_length, 16) * 2)])
                i = i + 8 + 2 + (int(cs_length, 16) * 2)
            else:
                break
    cs_neirong = {}
    for item in cs_dict:
        ts_val = ''
        for val in cs_dict[item]:
            ts_val += val
        cs_neirong[item] = ts_val
    if cs_dict == {}:
        cs_neirong = ''    

    if response_num == '':
        response_num = '*'

    message_body = '\t' + response_number + '\t' + str(response_num) + '\t' + str(cs_neirong).replace('{','').replace('}','').replace(' ','').replace("'",'') + '\t' +xjm

    return message_body



def parse_0200(cc, start_time,val_line):
    bjbz = bjbz_value(bin(int(cc[0:8], 16))[2:])
    #print(cc)
    stuat, lat_diredction, long_diredction = stuat_value(bin(int(cc[8:16], 16))[2:])
    latitude = str(float(int(cc[16:24], 16)) / 1000000)
    longitude = str(float(int(cc[24:32], 16)) / 1000000)
    altitude = str(int(cc[32:36], 16))
    speed = str(int(cc[36:40], 16))
    direction = str(int(cc[40:44], 16))
    alarm_date = date_value(cc[44:56], start_time)
    xjm = cc[-2:]

    if lat_diredction == '南纬':
        latitude = '-' + latitude
    if long_diredction == '西经':
        if float(longitude) < 180:
            longitude = '-' + longitude
        elif float(longitude) > 180 and float(longitude) <= 360:
            longitude = longitude
    i = 56
    add_message = ''
    while True:
        add_message_id = cc[i:i + 2]
        if add_message_id == '01' or add_message_id == '02' or add_message_id == '03' or add_message_id == '04' or add_message_id == '11' or add_message_id == '12' or add_message_id == '13' or add_message_id == '25' or add_message_id == '2A' or add_message_id == '2B' or add_message_id == '30' or add_message_id == '31' or add_message_id == 'E0':
            if len(cc[56:]) > i + 4:
                add_message_length = str(int(cc[i + 2:i + 4], 16))

                if cc[i + 4:i + 4 + (int(add_message_length) * 2)] != '':
                    add_message_cont = str(int(cc[i + 4:i + 4 + (int(add_message_length) * 2)], 16))
                else:
                    add_message_cont = '*'
                i = i + 4 + (int(add_message_length) * 2)
                add_message = add_message + add_message_id + ',' + add_message_cont + ';'

            else:
                break
        else:
            break

    if add_message == '':
        add_message = '*'
    if int(altitude) <= 5000 and int(speed) <= 400 and int(direction) <= 359 and alarm_date != '':
        message_body = '\t' + bjbz + '\t' + stuat + '\t' + latitude + '\t' + longitude + '\t' + altitude + '\t' + speed + '\t' + direction + '\t' + alarm_date + '\t' + str(
            add_message) + '\t' + str(xjm)
    else:
        fw_erro.write(str(val_line)+'\n')
        fw_erro.write(cc+'\n')
        fw_erro.write(altitude+' '+speed+' '+direction+' '+alarm_date+'\n')
        message_body = ''
    return message_body


def message_hand(cc):
    message_id = cc[0:4]
    message_type = {"message_body_length":"%s" % (str(int(('0' * (16 - len(bin(int(cc[4:8], 16))[2:])) + bin(int(cc[4:8], 16))[2:])[6:],2))),
                "encryption_method":"%s" % (('0' * (16 - len(bin(int(cc[4:8], 16))[2:])) + bin(int(cc[4:8], 16))[2:])[3:6]),
                "subpackage": "%s" %(('0' * (16 - len(bin(int(cc[4:8], 16))[2:])) + bin(int(cc[4:8], 16))[2:])[2])}
    message_body_length = int(('0' * (16 - len(bin(int(cc[4:8], 16))[2:])) + bin(int(cc[4:8], 16))[2:])[6:],2)
    iphone = cc[8:20]
    message_number = str(int(cc[20:24], 16))
    #print(message_type)
    if message_type['subpackage'] == "1":
        mess_b_all = str(int(cc[24:28], 16))
        if cc[28:32] != '':
            b_number = str(int(cc[28:32], 16))
        else:
            b_number = '*'
        mess_last = str(cc[32:])
    elif message_type['subpackage'] == '0':
        mess_b_all = '*'
        b_number = '*'
        mess_last = cc[24:]

    fw_line = message_id + '\t' + str(
        message_type).replace('{','').replace('}','').replace("'",'').replace(' ','') + '\t' + iphone + '\t' + message_number + '\t' + mess_b_all + '\t' + b_number

    return fw_line, mess_last, message_id, message_body_length


def main(mess_id, fw):
    pattern = re.compile(r'7e(.*)7e')

    for line in fr.readlines():
        line = line.strip().split('\t')
        fr_f = line[0] + '\t' + line[1] + '\t' + line[2] + '\t' + line[3] + '\t' + line[4] + '\t' + line[5] + '\t' + \
               line[6] + '\t' + line[7] + '\t' + line[8] + '\t' + line[9].split('__')[1] + '\t'
        fr_l = '\t' + str(line[12]) + '\t' + str(line[13]) + '\t' + str(line[14]) + '\t' + line[15] + '\t' + line[
            16] + '\t' + str(line[17]) + '\t' + str(line[18]) + '\t' + str(line[19]) + '\t' + str(line[20]) + '\t' + \
               line[21] + '\t' + line[22] + '\t' + str(line[23]) + '\t' + str(line[24])
        val_line = line
        len_line = line[9].split('__')[0]
        line = line[9].split('__')[2] # eth_payload
        payload_len = int(len_line)
        value = re.findall(pattern, line)
        if len(value) != 0:
            cc = value[0]
            if '7e' not in cc and len(cc) >= 24:
                fw_save = ''
                fw_line, mess_last, message_id,message_body_length = message_hand(cc)
                if mess_id == message_id and mess_id == '0200' and int(payload_len)-15 == len(mess_last)/2-1:
                    if message_body_length != 0:
                        if (len(mess_last)-2)/2 == message_body_length:
                            message_body = parse_0200(mess_last, line[5],val_line)
                            fw_save = fr_f + fw_line + message_body + fr_l
                            if message_body != '':
                                fw.write(fw_save)
                                fw.write('\n')
                if mess_id == message_id and mess_id == '8201':
                    message_body = '*'
                    fw_save = fr_f + fw_line + message_body + fr_l
                    fw.write(fw_save)
                    fw.write('\n')
                if mess_id == message_id and mess_id == '0201' and int(payload_len)-15 == len(mess_last)/2-1:
                    if (len(mess_last)-2)/2 >= message_body_length:
                        message_body = parse_0201(mess_last)
                        fw_save = fr_f + fw_line + message_body + fr_l
                        
                        fw.write(fw_save)
                        fw.write('\n')
                        fw.write('\n')
                if mess_id == message_id and mess_id == '8202':
                    if len(mess_last) >= 12:
                        message_body = parse_8202(mess_last)
                        fw_save = fr_f + fw_line + message_body + fr_l
                        fw.write(fw_save)
                        fw.write('\n')
                if mess_id == message_id and mess_id == '8203':
                    if len(mess_last) >= 12:
                        message_body = parse_8203(mess_last)
                        fw_save = fr_f + fw_line + message_body + fr_l
                        fw.write(fw_save)
                        fw.write('\n')

pattern = re.compile(r'7e(.*)7e')

def parse_jt808(line):
    line = jt808_preprocess(line)
    print("###########after preprocess line $###########")
    print(line)
    if line is None or len(line)==0 :
        return ""
    line=line+"\t*\t*\t巴基斯坦\t伊斯兰堡\t伊斯兰堡\t埃文\t*\t已路由-未使用\t中国\t广东省\t深圳市\t信联\t阿里云计算有限公司\t数据中心\t流入\tjt808202303010900090480\t*"
    print("###########before process line $###########")
    print(line)
    line = line.strip().split('\t')
    print(len(line))
    print(line[9].split('__'))
    fr_f = line[0] + '\t' + line[1] + '\t' + line[2] + '\t' + line[3] + '\t' + line[4] + '\t' + line[5] + '\t' + \
            line[6] + '\t' + line[7] + '\t' + line[8] + '\t' + line[9].split('__')[1] + '\t'
    fr_l = '\t' + str(line[12]) + '\t' + str(line[13]) + '\t' + str(line[14]) + '\t' + line[15] + '\t' + line[
        16] + '\t' + str(line[17]) + '\t' + str(line[18]) + '\t' + str(line[19]) + '\t' + str(line[20]) + '\t' + \
            line[21] + '\t' + line[22] + '\t' + str(line[23]) + '\t' + str(line[24])
    val_line = line
    len_line = line[9].split('__')[0]
    line = line[9].split('__')[2] # eth_payload
    payload_len = int(len_line)
    value = re.findall(pattern, line)
    if len(value) != 0:
        cc = value[0]
        if '7e' not in cc and len(cc) >= 24:
            fw_save = ''
            fw_line, mess_last, message_id,message_body_length = message_hand(cc)
            if mess_id == message_id and mess_id == '0200' and int(payload_len)-15 == len(mess_last)/2-1:
                if message_body_length != 0:
                    if (len(mess_last)-2)/2 == message_body_length:
                        message_body = parse_0200(mess_last, line[5],val_line)
                        fw_save = fr_f + fw_line + message_body + fr_l
                        if message_body != '':
                            return fw_save
            if mess_id == message_id and mess_id == '8201':
                message_body = '*'
                fw_save = fr_f + fw_line + message_body + fr_l
            if mess_id == message_id and mess_id == '0201' and int(payload_len)-15 == len(mess_last)/2-1:
                if (len(mess_last)-2)/2 >= message_body_length:
                    message_body = parse_0201(mess_last)
                    fw_save = fr_f + fw_line + message_body + fr_l
                    return fw_save
            if mess_id == message_id and mess_id == '8202':
                if len(mess_last) >= 12:
                    message_body = parse_8202(mess_last)
                    fw_save = fr_f + fw_line + message_body + fr_l
                    return fw_save
            if mess_id == message_id and mess_id == '8203':
                if len(mess_last) >= 12:
                    message_body = parse_8203(mess_last)
                    fw_save = fr_f + fw_line + message_body + fr_l
                    return fw_save

# 读取源文件到list
def line_to_list(line):
    line = line[:-1] if '\n' in line else line
    src_ip = line.split('\t')[1]  # 源ip
    dst_ip = line.split('\t')[2]  # 目的ip
    src_port = line.split('\t')[3]
    dst_port = line.split('\t')[4]
    data_time = line.split("\t")[6]
    # print(data_time)

    payload_len = -1
    protocol = 6
    payload = line.split('\t')[7]

    event_name = line.split('\t')[0]
    
    # print(src_ip, dst_ip, src_port, dst_port, protocol, payload_len, payload, data_time)
    try:
        if 'payload_len=' in  payload.split(';')[0]:
            len_payload = payload.split(';')[0].replace('tcp.payload_len=','')
        else:
            len_payload = '0'
    except:
        len_payload = '0'
    if payload == '':
        return []
    if payload.find('len=') is 0:
        payload_len = int(payload[payload.index('len=') + 4: payload.index(';')])
    if payload.find('proto=') != -1:
        if payload[payload.index('proto=') + 6: payload.index('payload')][:-1] == '':
            protocol = 0
        else:
            protocol = int(payload[payload.index('proto=') + 6: payload.index('payload')][:-1])
    payload = payload[payload.index('payload=') + 8:] if payload.find('payload') != -1 else payload
    
    if src_ip != "源IP":
        return [src_ip, dst_ip, src_port, dst_port, protocol, payload_len, payload, data_time, event_name, len_payload]
def parse_0200_preprocess(cc):
        is_true = False
        print(cc[16:24])
        latitude = str(float(int(cc[16:24], 16)) / 1000000)
        print("longitutde")
        print(cc[24:32])
        longitude = str(float(int(cc[24:32], 16)) / 1000000)
        print("altitude")
        print(cc[32:36])
        altitude = str(int(cc[32:36], 16))
        print("speed")
        print(cc[36:40])
        speed = str(int(cc[36:40], 16))
        print("direction")
        print(cc[40:44])
        direction = str(int(cc[40:44], 16))
    
        if int(altitude) <= 5000 and int(speed) <= 400 and int(direction) <= 359:
            is_true = True
        return is_true


def get_payload_byte_2_hex(log_info, msg_id):
    pattern1 = r"7e%s(.*)7e"%(msg_id)
    pattern2 = r"7e(.*7e.*)7e"
    payload = get_hex_payload(log_info[6])
    print(pattern1)
    res_origin_payload = re.findall(pattern1, str(payload))
    print("res_origin_payload")
    print(res_origin_payload)
    if len(res_origin_payload) != 0:
        #print('====================',i)  
        res_7e = "7e%s"%(msg_id) + res_origin_payload[0] + "7e"
        print("res_7e")
        print(res_7e)
        res2 = re.findall(pattern2, res_7e)
        if len(res2) == 0:
            # f.write(payload + "\n")
            print("in")
            # [src_ip, dst_ip, src_port, dst_port, protocol, payload_len, payload, data_time]
            print("res_7e[26:]")
            print(res_7e[26:])
            if parse_0200_preprocess(res_7e[26:]) == True:
                return log_info[8] + '\t' + log_info[0] + '\t' + log_info[1] + '\t' + log_info[2] + '\t' + log_info[3] + '\t' + log_info[7] + '\t'+log_info[7] + '\t'+"fake\tfake\t" + log_info[9]+'__'+log_info[6]+'__'+'eth_payload=%s' % (payload)     
    return ""
            
# 获取 16进制 payload
def get_hex_payload(payload):
    payload = payload.replace('\\\\', 'NULL')
    try:
        if payload.find('\\') is 0:
            return ''.join(list(map(packet_data, payload[1:].split('\\'))))
        else:
            payload_start = binascii.hexlify(payload[0: payload.index('\\')].encode()).decode()
            payload_rest = list(map(packet_data, payload[payload.index('\\') + 1:].split('\\')))
            payload_rest.insert(0, payload_start)
            return ''.join(payload_rest)
    except Exception as ex:
        print(ex)
        pass
    
def packet_data(data_item):
    data_item = data_item.replace('NULL', '\\')
    if len(data_item) is 0:
        return binascii.hexlify('\\'.encode()).decode()
    if len(data_item) is 1:
        return binascii.hexlify(data_item.encode()).decode()
    data = data_item[:2]
    if len(data_item) is 2:
        return data
    data += binascii.hexlify(data_item[2:].encode()).decode()
    return data

def jt808_preprocess(line):
    log_info = line_to_list(line)
    print("log info")
    print(log_info)
    # TODO msg_id 暂定0200
    return get_payload_byte_2_hex(log_info,mess_id)

