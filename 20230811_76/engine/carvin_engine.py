# -*- coding: utf-8 -*-
import os
import sys
import time
import re
import codecs
import urllib
def checkVIN(sVIN):
    dict_vin = {}
    dict_vin['A'] = 1
    dict_vin['B'] = 2
    dict_vin['C'] = 3
    dict_vin['D'] = 4
    dict_vin['E'] = 5
    dict_vin['F'] = 6
    dict_vin['G'] = 7
    dict_vin['H'] = 8
    dict_vin['J'] = 1
    dict_vin['K'] = 2
    dict_vin['L'] = 3
    dict_vin['M'] = 4
    dict_vin['N'] = 5
    dict_vin['P'] = 7
    dict_vin['Q'] = 8
    dict_vin['R'] = 9
    dict_vin['S'] = 2
    dict_vin['T'] = 3
    dict_vin['U'] = 4
    dict_vin['V'] = 5
    dict_vin['W'] = 6
    dict_vin['X'] = 7
    dict_vin['Y'] = 8
    dict_vin['Z'] = 9
    dict_vin['0'] = 0
    dict_vin['1'] = 1
    dict_vin['2'] = 2
    dict_vin['3'] = 3
    dict_vin['4'] = 4
    dict_vin['5'] = 5
    dict_vin['6'] = 6
    dict_vin['7'] = 7
    dict_vin['8'] = 8
    dict_vin['9'] = 9

    list_vin = []
    list_vin.append(8)
    list_vin.append(7)
    list_vin.append(6)
    list_vin.append(5)
    list_vin.append(4)
    list_vin.append(3)
    list_vin.append(2)
    list_vin.append(10)
    list_vin.append(0)
    list_vin.append(9)
    list_vin.append(8)
    list_vin.append(7)
    list_vin.append(6)
    list_vin.append(5)
    list_vin.append(4)
    list_vin.append(3)
    list_vin.append(2)

    sumvin = 0
    for i in range(0,len(sVIN)):
        sumvin = sumvin + dict_vin[sVIN[i]]*list_vin[i]
    yuNum = sumvin % 11
    if str(yuNum) == sVIN[8]:
        return True
    return False
def bkj_str_th(sdata):
    sredata = sdata.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')
    return sredata

def getYear(ss):
    year = 0
    if ord(ss) >= ord('1') and ord(ss) <= ord('9'):
        year = ord(ss) - ord('1') + 2001
    elif ord(ss) >= ord('A') and ord(ss) <= ord('H'):
        year = ord(ss) - ord('A') + 2010
    elif ord(ss) >= ord('J') and ord(ss) <= ord('N'):
        year = ord(ss) - ord('A') + 2010-1
    elif ord(ss) == ord('P') :
        year = 1993
    elif ord(ss) >= ord('R') and ord(ss) <= ord('T'):
        year = ord(ss) - ord('R') + 1994
    elif ord(ss) >= ord('V'):
        year = ord(ss) - ord('V') + 1997
    else:
        year = 0
    return year
def scCountry(ss):
    country = ''
    if ss=='1' or ss == '4':
        country = '美国'
    elif ss == 'J':
        country = '日本'
    elif ss == '2':
        country = '加拿大'
    elif ss == 'K':
        country = '韩国'
    elif ss == 'T':
        country = '瑞士'
    elif ss == '3':
        country = '墨西哥'
    elif ss == 'L':
        country = '中国'
    elif ss == 'V':
        country = '法国'
    elif ss == 'R':
        country = '台湾'
    elif ss == 'W':
        country = '德国'
    elif ss == '6':
        country = '澳大利亚'
    elif ss == 'Y':
        country = '瑞典'
    elif ss == '9':
        country = '巴西'
    elif ss == 'Z':
        country = '意大利'
    else:
        country = '*'
    return country




def yqVM(sVIN):
    safe = '*'
    pl = '*'
    cartype = ''
    fdjandbsx = ''
    carxing = ''
    year = 0
    zpgc = ''
    if sVIN[3] == 'A':
        safe = '安全带'
    elif sVIN[3] == 'B':
        safe = '安全带+安全气囊'
    elif sVIN[3] == '1':
        pl = 'L<=1.2'
    elif sVIN[3] == '2':
        pl = '1.2<L<=1.6'
    elif sVIN[3] == '3':
        pl = '1.6<L<=2.0'
    elif sVIN[3] == '4':
        pl = '2.0<L<=2.4'
    elif sVIN[3] == '5':
        pl = '2.4<L<=2.8'
    elif sVIN[3] == '6':
        pl = '2.8<L<=3.2'
    elif sVIN[3] == '7':
        pl = '3.2<L<=3.6'
    elif sVIN[3] == '8':
        pl = '3.6<L<=4.0'
    elif sVIN[3] == '9':
        pl = '4.0<L<=4.4'
    else:
        pl = '*'
        safe = '*'
    if sVIN[4] == 'A':
        cartype = '四门阶背'
    elif sVIN[4] == 'B':
        cartype = '四门溜背'
    elif sVIN[4] == 'C':
        cartype = '四门方背'
    else:
        cartype='*'
    if sVIN[5] == '1':
        fdjandbsx = '汽油发动机+手动变速箱'
    elif sVIN[5] == '2':
        fdjandbsx = '汽油发动机+自动变速箱'
    elif sVIN[5] == '3':
        fdjandbsx = '柴油发动机+手动变速箱'
    elif sVIN[5] == '4':
        fdjandbsx = '柴油发动机+自动变速箱'
    elif sVIN[5] == '5':
        fdjandbsx = '两用燃料发动机+手动变速箱'
    elif sVIN[5] == '6':
        fdjandbsx = '两用燃料发动机+自动变速箱'
    else:
        fdjandbsx = '*'
    if sVIN[6:8] == '4B':
        carxing = 'Audi A6'
    elif sVIN[6:8] == '8E':
        carxing = 'Audi A4'
    elif sVIN[6:8] == '1G':
        carxing = 'Jetta'
    elif sVIN[6:8] == '1J':
        carxing = 'Bora'
    elif sVIN[6:8] == '2J':
        carxing = 'Golf'
    elif sVIN[6:8] == '1K':
        carxing = 'Sagitar'
    elif sVIN[6:8] == '2K':
        carxing = 'Caddy'
    elif sVIN[6:8] == '3C':
        carxing = 'Magotan'
    elif sVIN[6:8] == '15':
        carxing = 'New Bora'
    else:
        carxing = '*'
    year = getYear(sVIN[9])
    if sVIN[10] == '3':
        zpgc = '中国长春'
    else:
        zpgc = '*'
    return safe,pl,cartype,fdjandbsx,carxing,zpgc,year

def jkBWM(sVIN):
    cartype = ''
    pl = ''
    fdjandbsx = ''
    carxing = ''
    safe = ''
    zpgc = ''
    year = ''
    year = getYear(sVIN[9])
    if sVIN[3]=='A':
        cartype = '四门轿车'
        if sVIN[4] == 'M':
            fdjandbsx = '六缸发动机'
            if sVIN[5] == '3' or sVIN[5] == '4':
                pl = '2.5L'
                carxing = '323i'
            elif sVIN[5] == '5' or sVIN[5] == '6':
                pl = '2.8L'
                carxing = '328i'
            else:
                pl = '*'
                carxing = '*'
        else:
            fdjandbsx = '*'
            pl = '*'
            carxing = '*'
    elif sVIN[3]=='B':
        cartype = '两门'
        if sVIN[4] == 'E':
            fdjandbsx = '四缸机'
            if sVIN[5] == '7' or sVIN[5] == '8':
                pl = '1.9L'
                carxing = '318is'
            else:
                pl = '*'
                carxing = '*'
        elif sVIN[4] == 'F':
            fdjandbsx = '六缸机'
            if sVIN[5] == '7' or sVIN[5] == '8':
                pl = '2.5L'
                carxing = '323is'
            else:
                pl = '*'
                carxing = '*'
        elif sVIN[4] == 'G':
            fdjandbsx = '六缸机'
            if sVIN[5] == '1' or sVIN[5] == '2':
                pl = '2.8L'
                carxing = '328is'
            elif sVIN[5] == '9':
                carxing = 'M3'
                pl = '2.8L/3.2L'
            else:
                pl = '*'
                carxing = '*'
        elif sVIN[4] == 'H':
            fdjandbsx = '四缸机'
            if sVIN[5] == '7' or sVIN[5] == '8':
                pl = '1.9L'
                carxing = '318ic'
            else:
                pl = '*'
                carxing = '*'
        elif sVIN[4] == 'J':
            fdjandbsx = '六缸机'
            if sVIN[5] == '7' or sVIN[5] == '8':
                pl = '2.5L'
                carxing = '323ic'
            else:
                pl = '*'
                carxing = '*'
        elif sVIN[4] == 'K':
            fdjandbsx = '六缸机'
            if sVIN[5] == '7' or sVIN[5] == '8':
                pl = '2.8L'
                carxing = '328ic'
            if sVIN[5] == '9' or sVIN[5] == '0':
                pl = '3.2L'
                carxing = 'M3'
            else:
                pl = '*'
                carxing = '*'
        elif sVIN[4] == 'M':
            fdjandbsx = '六缸机'
            if sVIN[5] == '3' :
                pl = '2.5L'
                carxing = '323ci'
            elif sVIN[5] == '5' :
                pl = '2.8L'
                carxing = '328ci'
            else:
                pl = '*'
                carxing = '*'
        else:
            fdjandbsx = '*'
            pl = '*'
            carxing = '*'
    elif sVIN[3]=='C':
        if sVIN[4:7] == 'C03' or sVIN[4:7] == 'C93':
            cartype = '四门轿车'
            fdjandbsx = '四缸机'
            pl = '1.9L'
            carxing = '318i'
        elif sVIN[4:7] == 'DO3' :
            cartype = '四门轿车'
            fdjandbsx = '六缸机'
            pl = '2.8L'
            carxing = 'M3'
        elif sVIN[4:7] == 'D13' or sVIN[4:7] == 'D23' or sVIN[4:7] == 'D33':
            cartype = '四门轿车'
            fdjandbsx = '六缸机'
            pl = '2.8L'
            carxing = '328i'
        elif sVIN[4:7] == 'D73' or sVIN[4:7] == 'D83':
            cartype = '四门轿车'
            fdjandbsx = '四缸机'
            pl = '1.9L'
            carxing = '318i'
        elif sVIN[4:7] == 'D93':
            cartype = '四门轿车'
            fdjandbsx = '六缸机'
            pl = '2.8L/3.2L'
            carxing = 'M3'
        elif sVIN[4:7] == 'D03':
            cartype = '四门轿车'
            fdjandbsx = '六缸机'
            pl = '3.2L'
            carxing = 'M3'
        elif sVIN[4:7] == 'G73' or sVIN[4:7] == 'G83':
            cartype = '两门'
            fdjandbsx = '四缸'
            pl = 'Hatchback1.9L'
            carxing = '318ti'
        elif sVIN[4:7] == 'H73':
            cartype = '两门'
            fdjandbsx = '四缸'
            pl = '1.9L'
            carxing = 'Z3Roadster'
        elif sVIN[4:7] == 'H93':
            cartype = '两门'
            fdjandbsx = '四缸'
            pl = '2.5L'
            carxing = 'Z3Roadster'
        elif sVIN[4:7] == 'H33':
            cartype = '两门'
            fdjandbsx = '四缸/四缸机'
            pl = '2.8L'
            carxing = 'Z3Roadster'
        elif sVIN[4:7] == 'J33':
            cartype = '两门'
            fdjandbsx = '六缸'
            pl = '2.8L'
            carxing = 'Z3Roadster'
        elif sVIN[4:7] == 'K53':
            cartype = '两门'
            fdjandbsx = '六缸'
            pl = '2.8L'
            carxing = 'Z3'
        elif sVIN[4:7] == 'K93':
            cartype = '两门'
            fdjandbsx = '六缸'
            pl = '3.2L'
            carxing = 'M Roadster'
        elif sVIN[4:7] == 'M93':
            cartype = '两门'
            fdjandbsx = '六缸'
            pl = '3.2L'
            carxing = 'M Coupe'
        else:
            cartype = '*'
            fdjandbsx = '*'
            pl = '*L'
            carxing = '*'

    elif sVIN[3]=='D':
        cartype = '四门轿车'
        if sVIN[4:7] == 'D53' or sVIN[4:7] == 'D63':
            fdjandbsx = '六缸'
            pl = '2.8L'
            carxing = '528i'
        elif sVIN[4:7] == 'E53' or sVIN[4:7] == 'E63':
            fdjandbsx = '8缸'
            pl = '4.4L'
            carxing = '540i'
        elif sVIN[4:7] == 'M53' or sVIN[4:7] == 'M63':
            fdjandbsx = '六缸'
            pl = '2.8L'
            carxing = '528i'
        elif sVIN[4:7] == 'N53' or sVIN[4:7] == 'N63':
            fdjandbsx = '8缸'
            pl = '4.4L'
            carxing = '540i'
        elif sVIN[4:7] == 'N83' :
            fdjandbsx = '8缸'
            pl = '4.4L'
            carxing = '540i Protection'
        elif sVIN[4:7] == 'P53' or sVIN[4:7] == 'P63':
            fdjandbsx = '六缸'
            pl = '4.4L'
            carxing = '540i Touring'
        elif sVIN[4:7] == 'R63' :
            cartype = '四门旅行车'
            fdjandbsx = '8缸'
            pl = '4.4L'
            carxing = '540i Touring'
        else:
            cartype = '*'
            fdjandbsx = '*'
            pl = '*'
            carxing = '*'
    elif sVIN[3]=='E':
        cartype = '两门'
        if sVIN[4:7] == 'F83':
            fdjandbsx = '8缸'
            pl = '4.4L'
            carxing = '840ci'
        elif sVIN[4:7] == 'G43' :
            fdjandbsx = '12缸'
            pl = '5.4L'
            carxing = '850ci'
    elif sVIN[3]=='G':
        cartype = '四门轿车'
        if sVIN[4:7] == 'F53' or sVIN[4:7] == 'G63':
            fdjandbsx = '8缸'
            pl = '4.4L'
            carxing = '740i'
        elif sVIN[4:7] == 'H83':
            fdjandbsx = '8缸'
            pl = '4.4L'
            carxing = '740iL'
        elif sVIN[4:7] == 'H03':
            fdjandbsx = '8缸'
            pl = '4.4L'
            carxing = '740iL Protection'
        elif sVIN[4:7] == 'J03':
            fdjandbsx = '12缸'
            pl = '5.4L'
            carxing = '740iL'
        elif sVIN[4:7] == 'J83':
            fdjandbsx = '8缸'
            pl = '4.4L'
            carxing = '740iL'
        elif sVIN[4:7] == 'K23' or sVIN[4:7] == 'K93':
            fdjandbsx = '12缸'
            pl = '5.4L'
            carxing = '750i'
        else:
            fdjandbsx = '*'
            pl = '*'
            carxing = '*'
    else:
        cartype = '*'
        fdjandbsx = '*'
        pl = '*'
        carxing = '*'
    if sVIN[7] == '0':
        safe = '手动安全带'
    elif sVIN[7]=='1':
        safe = '手动安全带并带有驾驶员安全气囊'
    elif sVIN[7] == '2' or sVIN[7]=='3':
        safe = '手动安全带并带有驾驶员和乘气囊'
    elif sVIN[7] == '4':
        safe = '手动安全带并有先进的驾驶员和乘客安全气囊'
    else:
        safe = '*'
    if sVIN[10]=='A' or sVIN[10]=='F' or sVIN[10]=='K':
        zpgc = '德国 Munich Germany'
    elif sVIN[10] == 'B' or sVIN[10]=='C' or sVIN[10]=='D' or sVIN[10]=='G':
        zpgc = '德国 Dingolfing'
    elif sVIN[10] == 'E' or sVIN[10] == 'J':
        zpgc = '德国 Rengensburg'
    elif sVIN[10] == 'L':
        zpgc = '美国 Greer,South Carolina'
    elif sVIN[10] == 'Z':
        zpgc = 'Pretona,South Africa'
    else:
        zpgc = '*'
    return safe,pl,cartype,fdjandbsx,carxing,zpgc,year

def jkBENZ(sVIN):
    cartype = '*'
    pl = '*'
    fdjandbsx = '*'
    carxing = '*'
    safe = '*'
    zpgc = '*'
    year = 0
    year = getYear(sVIN[9])
    if sVIN[3:7] == 'AB23':
        cartype = '四门轿车'
        carxing = '240D'
        fdjandbsx = '柴油机'
    elif sVIN[3:7] == 'AB33':
        cartype = '四门轿车'
        carxing = '300CDT'
        fdjandbsx = '增压柴油机'
    elif sVIN[3:7] == 'AB33':
        cartype = '四门轿车'
        carxing = '300CDT'
        fdjandbsx = '增压柴油机'
    elif sVIN[3:7] == 'AB54':
        cartype = '四门多用途车 MPV'
        carxing = 'ML320'
    elif sVIN[3:7] == 'AB53':
        cartype = '二门 Coupe轿车'
        carxing = '300CDT'
        fdjandbsx = '增压柴油机'
    elif sVIN[3:7] == 'AB72':
        cartype = '四门 MPV'
        carxing = 'ML430'
    elif sVIN[3:7] == 'AB93':
        cartype = '四门 Wagon旅行轿车'
        carxing = '300TDT'
        fdjandbsx = '增压柴油机'
    elif sVIN[3:7] == 'BA45':
        cartype = '二门 Coupe轿车'
        carxing = '380SL'
    elif sVIN[3:7] == 'CA32':
        cartype = '四门轿车'
        carxing = '380SE'
    elif sVIN[3:7] == 'CA33':
        cartype = '四门轿车'
        carxing = '380SEL'
    elif sVIN[3:7] == 'CA43':
        cartype = '二门 Coupe'
        carxing = '380SEC'
    elif sVIN[3:7] == 'AB33':
        cartype = '二门 Coupe轿车'
        carxing = '500SEC'
    elif sVIN[3:7] == 'CB20':
        cartype = '四门轿车'
        carxing = '300SD'
        fdjandbsx = '增压柴油机'
    elif sVIN[3:7] == 'DA24':
        cartype = '四门轿车'
        carxing = '190E'
        pl = '2.3L'
    elif sVIN[3:7] == 'DB22':
        cartype = '四门轿车'
        carxing = '190D'
        fdjandbsx = '柴油机'
    elif sVIN[3:7] == 'BA48':
        cartype = '二门 Coupe轿车'
        carxing = '560SL'
    elif sVIN[3:7] == 'CA24':
        cartype = '四门轿车'
        carxing = '300SE'
    elif sVIN[3:7] == 'CA25':
        cartype = '四门轿车'
        carxing = '300SEL'
    elif sVIN[3:7] == 'CA35':
        cartype = '四门轿车'
        carxing = '420SEL'
    elif sVIN[3:7] == 'CA39':
        cartype = '四门轿车'
        carxing = '560SEL'
    elif sVIN[3:7] == 'CA45':
        cartype = '二门 Coupe轿车'
        carxing = '560SEC'
    elif sVIN[3:7] == 'CB25':
        cartype = '四门轿车'
        carxing = '300SDL'
        fdjandbsx = '增压柴油机'
    elif sVIN[3:7] == 'CB34':
        cartype = '四门轿车'
        carxing = '350SD'
        fdjandbsx = '增压柴油机'
    elif sVIN[3:7] == 'CB35':
        cartype = '四门轿车'
        carxing = '350SDL'
        fdjandbsx = '增压柴油机'
    elif sVIN[3:7] == 'DA24' or sVIN[3:7] == 'DA28':
        cartype = '四门轿车'
        carxing = '190E'
        pl = '2.3L'
    elif sVIN[3:7] == 'DA29':
        cartype = '四门轿车'
        carxing = '190E'
        pl = '2.6L'
    elif sVIN[3:7] == 'DA34':
        cartype = '四门轿车'
        carxing = '190E'
        pl = '2.3L16气门'
    elif sVIN[3:7] == 'DB26':
        cartype = '四门轿车'
        carxing = '190D'
        pl = '2.5L'
        fdjandbsx = '柴油机'
    elif sVIN[3:7] == 'DB28':
        cartype = '四门轿车'
        carxing = '190D'
        pl = '2.5L16气门'
        fdjandbsx = '柴油机增压'
    elif sVIN[3:7] == 'EA26':
        cartype = '四门轿车'
        carxing = '260E/300E'
    elif sVIN[3:7] == 'EA28':
        cartype = '四门轿车'
        carxing = '300E'
        pl = '2.8L'
    elif sVIN[3:7] == 'EA30' or sVIN[3:7] == 'EA32':
        cartype = '四门轿车'
        carxing = '300E/E320'
    elif sVIN[3:7] == 'EA34':
        cartype = '四门轿车'
        carxing = 'E420/400E'
    elif sVIN[3:7] == 'EA36':
        cartype = '四门轿车'
        carxing = '500E/E500'
    elif sVIN[3:7] == 'EA50' or sVIN[3:7] == 'EA51' or sVIN[3:7] == 'EA52':
        cartype = '二门 Coupe轿车'
        carxing = '300CE'
    elif sVIN[3:7] == 'EB28':
        cartype = '四门轿车'
        carxing = '300D'
        pl = '2.5L'
        fdjandbsx = '增压柴油机'
    elif sVIN[3:7] == 'EA66':
        cartype = '活动顶轿门二门'
        carxing = '(300CE/CV Convertible)/(E320Convertible)'
    elif sVIN[3:7] == 'EA90':
        cartype = '四门 Wagon 旅行轿车'
        carxing = '300TE'
    elif sVIN[3:7] == 'EA92':
        cartype = '四门 Wagon 旅行轿车/四门 Wagon'
        carxing = '300TB/E320'
    elif sVIN[3:7] == 'EB31':
        cartype = '四门轿车'
        carxing = 'E300DW'
        fdjandbsx = '柴油机'
    elif sVIN[3:7] == 'EB33':
        cartype = '四门轿车'
        carxing = '300DT'
        fdjandbsx = '柴油机增压'
    elif sVIN[3:7] == 'EB93':
        cartype = '四门 Wagon 旅行轿车'
        carxing = '300TDT'
        fdjandbsx = '增压柴油机'
    elif sVIN[3:7] == 'ED30':
        cartype = '四门轿车(4-Matic)'
        carxing = '300E'
    elif sVIN[3:7] == 'ED90':
        cartype = '四门 Wagon(4-Matic)旅行轿车'
        carxing = '300TE'
    elif sVIN[3:7] == 'FA61':
        cartype = '二门 Coupe/Roadster'
        carxing = '300SL'
    elif sVIN[3:7] == 'FA66':
        cartype = '二门 Coupe/Roadster'
        carxing = '500SL'
    elif sVIN[3:7] == 'FA67':
        cartype = '二门 Coupe/Roadster'
        carxing = '500SL/SL500R'
    elif sVIN[3:7] == 'FA68':
        cartype = '二门 Coupe/Roadster'
        carxing = 'SL500R'
    elif sVIN[3:7] == 'FA76':
        cartype = '二门 Coupe/Roadster'
        carxing = '600SL/SL600R'
    elif sVIN[3:7] == 'FA68':
        cartype = '二门 Coupe/Roadster'
        carxing = 'SL500R'
    elif sVIN[3:7] == 'FA76':
        cartype = '二门 Coupe/Roadster'
        carxing = '600SL/SL600R'
    elif sVIN[3:7] == 'GA32':
        cartype = '四门轿车'
        carxing = '300SE/S320W'
    elif sVIN[3:7] == 'GA33':
        cartype = '四门轿车 Sedan'
        carxing = 'S320V'
        pl = '3.2L'
    elif sVIN[3:7] == 'GA42':
        cartype = '四门轿车'
        carxing = '400SE'
        pl = '3.2L'
    elif sVIN[3:7] == 'GA43':
        cartype = '四门轿车'
        carxing = 'S420/S420V/400SEL'
    elif sVIN[3:7] == 'GA51':
        cartype = '四门轿车'
        carxing = 'S500/S500V/500SEL'
    elif sVIN[3:7] == 'GA57':
        cartype = '四门轿车/四门'
        carxing = 'S600/S600V/600SEL'
    elif sVIN[3:7] == 'GA70':
        cartype = '二门/二门轿车'
        carxing = 'CL500C/S500C/500SEL'
    elif sVIN[3:7] == 'GA76':
        cartype = '二门/轿车二门'
        carxing = 'S600C/CL600C/S600'
    elif sVIN[3:7] == 'GB34':
        cartype = '四门轿车'
        carxing = 'S350DW/300SD'
    elif sVIN[3:7] == 'HA23' or sVIN[3:7] == 'HA24':
        cartype = '四门轿车'
        carxing = 'C230W/C230'
    elif sVIN[3:7] == 'HA22':
        cartype = '四门轿车'
        carxing = 'C220'
    elif sVIN[3:7] == 'HA28':
        pl = '2.8L'
        carxing = 'C280'
    elif sVIN[3:7] == 'HA29':
        cartype = '四门轿车'
        carxing = 'C280W'
    elif sVIN[3:7] == 'HA33':
        cartype = '四门轿车'
        carxing = 'C43/C43W'
    elif sVIN[3:7] == 'HA36':
        cartype = '四门轿车'
        carxing = 'C360'
    elif sVIN[3:7] == 'JF20':
        cartype = '四门轿车'
        carxing = 'E300D'
        fdjandbsx = '柴油机'
    elif sVIN[3:7] == 'JF25':
        cartype = '四门轿车'
        carxing = 'E300DT'
        fdjandbsx = '增压柴油机'
    elif sVIN[3:7] == 'JF55':
        cartype = '四门轿车'
        carxing = 'E320'
    elif sVIN[3:7] == 'JF65':
        cartype = '四门轿车'
        carxing = 'E320W'
    elif sVIN[3:7] == 'JF70':
        cartype = '四门轿车'
        carxing = 'E430W'
    elif sVIN[3:7] == 'JF72':
        cartype = '四门轿车'
        carxing = 'E420'
    elif sVIN[3:7] == 'JF74':
        cartype = '四门轿车'
        carxing = 'E55/E55W'
    elif sVIN[3:7] == 'JF82':
        cartype = '四门轿车'
        carxing = 'E320W'
    elif sVIN[3:7] == 'KK47' or sVIN[3:7] == 'KK49':
        cartype = '二门 Roadster Coupe'
        carxing = 'SLK230'
    elif sVIN[3:7] == 'KK65':
        cartype = '二门 Roadster Coupe'
        carxing = 'SLK320'
    elif sVIN[3:7] == 'KK66':
        cartype = '二门 Roadster Coupe'
        carxing = 'SLK230AG'
    elif sVIN[3:7] == 'KK74':
        cartype = '二门 Coupe'
        carxing = 'SLK55AGM'
    elif sVIN[3:7] == 'LJ65':
        cartype = '二门 Coupe'
        carxing = 'CLK320'
    elif sVIN[3:7] == 'LJ70':
        cartype = '二门 Coupe'
        carxing = 'CLK430'
    elif sVIN[3:7] == 'LK65':
        cartype = 'Cabriolet'
        carxing = 'CLK320'
    elif sVIN[3:7] == 'JH65':
        cartype = '四门旅行车'
        carxing = 'E320(S)'
    elif sVIN[3:7] == 'JH82':
        cartype = '四门旅行车 全轮驱动'
        carxing = 'E320(S)'
    elif sVIN[3:7] == 'NG70':
        cartype = '四门轿车'
        carxing = 'S430V/S430'
    elif sVIN[3:7] == 'NG75':
        cartype = '四门轿车'
        carxing = 'S600V/S500'
    elif sVIN[3:7] == 'PJ75':
        cartype = '两门 coupe'
        carxing = 'CL500'
    elif sVIN[3:7] == 'PJ73':
        cartype = '两门 coupe'
        carxing = 'CLK55AMG'
    elif sVIN[3:7] == 'PJ78':
        cartype = '两门 coupe'
        carxing = 'CLK600/CL600'
    elif sVIN[3:7] == 'ABT4':
        cartype = '四门 MPV'
        carxing = 'ML55'
    elif sVIN[3:7] == 'BA4B':
        cartype = '两门 Coupe'
        carxing = '560SL'
    elif sVIN[3:7] == 'DB22':
        cartype = '四门轿车'
        carxing = '190D'
        fdjandbsx = '柴油机'
    elif sVIN[3:7] == 'HA34':
        cartype = '四门轿车'
        carxing = 'C230ML'
    elif sVIN[3:7] == 'LK70':
        cartype = '四门轿车'
        carxing = 'CLK430'
    elif sVIN[3:7] == 'EA33':
        cartype = '四门轿车'
        carxing = '300DT'
    elif sVIN[3:7] == 'GA34':
        cartype = '四门轿车'
        carxing = 'S350'
    elif sVIN[3:7] == 'RF61':
        cartype = '四门轿车'
        carxing = 'C240W'
    elif sVIN[3:7] == 'RF64':
        cartype = '四门轿车'
        carxing = 'C320W'
    elif sVIN[3:7] == 'RH64':
        cartype = '四门旅行轿车'
        carxing = 'C320S'
    elif sVIN[3:7] == 'RN47':
        cartype = '两门 coupe'
        carxing = 'C230'
    elif sVIN[3:7] == 'SK75':
        cartype = '两门 Roadster'
        carxing = 'SL500R'
    elif sVIN[3:7] == 'SF83':
        cartype = '四门轿车'
        carxing = 'E430W4'
    if sVIN[7]=='A':
        safe = '三点式安全带'
    elif sVIN[7]=='B':
        safe = '三点式安全带及驾驶员安全气囊'
    elif sVIN[7]=='C':
        safe = '三点式安全带并装有紧急收缩器装置'
    elif sVIN[7]=='D':
        safe = '带收缩器的三点式安全带驾驶员安全气囊，后排中央腰式安全带'
    elif sVIN[7]=='E' or sVIN[7]=='F' or sVIN[7]=='G':
        safe = '三点式安全带（收紧器）驾驶员乘员前部及侧向安全气囊，后排座中央腰式安全带'
    elif sVIN[7]=='H':
        safe = '三点式安全带（装有收紧器）驾驶员乘员前部气囊（帘幕式）以及侧向安全气囊，后排中央三点式安全带'

    if sVIN[10] == 'A' or sVIN[10] == 'B' or sVIN[10] == 'C' or sVIN[10] == 'D' or sVIN[10] == 'E':
        zpgc = 'Sindelfingen'
    elif sVIN[10] == 'F' or sVIN[10] == 'G' or sVIN[10] == 'H' :
        zpgc = 'Bremen'
    elif sVIN[10] == 'T' :
        zpgc = 'Osnabruck'
    elif sVIN[10] == 'X':
        zpgc = 'Graz'
    return safe, pl, cartype, fdjandbsx, carxing, zpgc, year
def shVM(sVIN):
    cartype = '*'
    pl = '*'
    fdjandbsx = '*'
    carxing = '*'
    safe = '*'
    year = 0
    year = getYear(sVIN[9])
    if sVIN[3]=='A':
        cartype = '四门轿车（折背式车身）'
    elif sVIN[3] == 'B':
        cartype = '四门轿车（直背式车身）'
    elif sVIN[3] == 'C' or sVIN[3] == 'E':
        cartype = '四门加长型轿车（折背式车身）'
    elif sVIN[3] == 'F':
        cartype = '四门轿车（短背式车身）'
    elif sVIN[3] == 'H':
        cartype = '四门加长型折背式轿车'
    elif sVIN[3] == 'K':
        cartype = '两门轿车（短背式车身）'
    if sVIN[6:8] == '33':
        carxing = '桑塔纳轿车/旅行轿车/桑塔纳2000型轿车'
        if sVIN[4]=='A':
            fdjandbsx = 'JV(026A)/AHM'
        elif sVIN[4]=='B':
            fdjandbsx = 'JV(026A) LPG/AHM'
        elif sVIN[4]=='C':
            fdjandbsx = 'JV(026A)/2P'
        elif sVIN[4]=='D':
            fdjandbsx = 'JV(026A) LPG/2P'
        elif sVIN[4]=='E':
            fdjandbsx = 'JV(026A) CNG/2P'
        elif sVIN[4]=='F':
            fdjandbsx = 'AFE(026N) /2P'
        elif sVIN[4]=='G':
            fdjandbsx = 'AYF(050B) LPG/QJ'
        elif sVIN[4] == 'H':
            fdjandbsx = 'AJR(06BC)/2P'
        elif sVIN[4]=='J':
            fdjandbsx = 'AYJ(06BC)/FNV'
        elif sVIN[4]=='K':
            fdjandbsx = 'AFE(026N) LPG/2P'
        elif sVIN[4]=='L':
            fdjandbsx = 'AYF(050B) LPG/QJ'
        elif sVIN[4]=='M':
            fdjandbsx = 'AYJ(06BC) LPG/2P'
    elif sVIN[6:8] == '9F':
        carxing = '帕萨特轿车'
        if sVIN[4]=='A':
            fdjandbsx = 'ANQ(06BH)/DWB(FSN)'
        elif sVIN[4]=='B':
            fdjandbsx = 'ANQ(06BH)/DMU(EPT)'
        elif sVIN[4]=='C':
            fdjandbsx = 'AWL(06BA)/EZS'
        elif sVIN[4]=='D':
            fdjandbsx = 'AWL(06BA)/EMG'
        elif sVIN[4]=='E':
            fdjandbsx = 'BBG(078 2)/EZY'
        elif sVIN[4]=='L':
            fdjandbsx = 'BGC(06BM)/EZS'
        elif sVIN[4]=='M':
            fdjandbsx = 'BGC(06BM)/EMG'
    elif sVIN[6:8] == '9J':
        carxing = '波罗牌轿车'
        if sVIN[4]=='A':
            fdjandbsx = 'BCC(036P)/GET(FCU)'
        elif sVIN[4]=='B':
            fdjandbsx = 'BCC(036P)/GCU(ESK)'
        elif sVIN[4]=='C':
            fdjandbsx = 'BCD(06A6)/GEV(FXP)'
    elif sVIN[6:8] == '5X':
        carxing = '高尔牌轿车'
        if sVIN[4]=='A':
            fdjandbsx = 'BHJ(050C)/GPJ'
    if sVIN[5] == '0':
        safe = '安全带'
    elif sVIN[5] == '1':
        safe = '安全气囊（驾驶员）'
    elif sVIN[5] == '2':
        safe = '安全气囊（驾驶员，前排座乘员，前座侧面）'
    elif sVIN[5] == '3':
        safe = '安全气囊（驾驶员，前排座乘员，前后座侧面）'
    elif sVIN[5] == '4':
        safe = '安全气囊（驾驶员，前排座乘员）'
    elif sVIN[5] == '5':
        safe = '安全气囊（驾驶员，前排座乘员，前后座侧面头部）'
    elif sVIN[5] == '6':
        safe = '安全气囊（驾驶员，前排座乘员，前座侧面头部）'
    zpgc = '上海大众汽车有限公司'
    return safe, pl, cartype, fdjandbsx, carxing, zpgc, year

def jkVM(sVIN):
    cartype = '*'
    pl = '*'
    fdjandbsx = '*'
    carxing = '*'
    safe = '*'
    year = 0
    year = getYear(sVIN[9])
    company = '*'
    cartype_q = '*'
    zpgc = '*'
    if sVIN[1]=='B':
        company = '巴西大众汽车公司'
    elif sVIN[1]=='V':
        company = '德国大众汽车公司'
    if sVIN[2]=='1':
        cartype_q = 'Pickup(轻型客货两用车)'
    elif sVIN[2]=='2' or sVIN[2] == '3':
        cartype_q = 'MPV(多用途车)'
    elif sVIN[2] == 'W':
        cartype_q = '轿车'
    if sVIN[6:8]=='1C':
        carxing = 'New Beetle新甲壳虫'
        if sVIN[3]=='B':
            cartype = '两门 GL'
        elif sVIN[3]=='C':
            cartype = '两门 GLS'
        elif sVIN[3]=='D':
            cartype = '两门 GLX'
    elif sVIN[6:8] == '1E' or sVIN[6:8] == '1V':
        carxing = 'Cabrio轿车'
        if sVIN[3] == 'A':
            cartype = '两门 cabrio/cabrioGL'
        elif sVIN[3] == 'B':
            cartype = '两门 cabrioGLS(Highline)'
        elif sVIN[3] == 'C':
            cartype = '两门cabrio GL'
        elif sVIN[3] == 'D':
            cartype = '两门新型 cabrio GLS'
    elif sVIN[6:8] == '1G' or sVIN[6:8] == '1H' or sVIN[6:8] == '1J' or sVIN[6:8]=='9M':
        carxing = '高尔夫/捷达/新高尔夫/新GTI/新捷达'
        if sVIN[3]=='B':
            cartype = '两门特制型/超豪华型(GL)/运动型'
        elif sVIN[3]=='C':
            cartype = '四门轿车 Sport/GT1'
        elif sVIN[3]=='F':
            cartype = '四门特制型/GL/TDI'
        elif sVIN[3]=='G':
            cartype = '四门 GLS'
        elif sVIN[3]=='H':
            cartype = '两门 GTI,16V,VR6'
        elif sVIN[3]=='K':
            cartype = '四门GOLFIII,基本型/两门基本型'
        elif sVIN[3]=='J':
            cartype = '四门（限量）'
        elif sVIN[3]=='M':
            cartype = '两门特制型'
        elif sVIN[3]=='P':
            cartype = '四门基本型/WolfsburgEdition'
        elif sVIN[3]=='R':
            cartype = '四门特制GL型/carat(金贵型)/经济型/新型 Jetta/四门GL型/增压直喷型'
        elif sVIN[3]=='S':
            cartype = '四门GLS型/特制型'
        elif sVIN[3]=='T':
            cartype = '四门GLI/GL'
        elif sVIN[3]=='V':
            cartype = '四门GT'
        elif sVIN[3]=='Y':
            cartype = '四门 K2'
    elif sVIN[6:8] == '15' or sVIN[6:8] == '17':
        carxing = 'Rabbit/Cabriolet/Golf.GTI'
        if sVIN[3] == 'A':
            cartype = '两门基本型'
        elif sVIN[3] == 'B' or sVIN[3] == 'C':
            cartype = '两门特制型'
        elif sVIN[3] == 'D':
            cartype = '两门金贵型'
        elif sVIN[3] == 'E':
            cartype = '两门 Etienne Aigner'
    elif sVIN[6:8] == '3B' or sVIN[6:8] == '31':
        carxing = 'Passat'
        if sVIN[3] == 'A':
            cartype = '四门 GLS(加拿大)'
        elif sVIN[3] == 'B':
            cartype = '四门 GLS/TDI旅行车（加拿大）/GLX旅行车'
        elif sVIN[3] == 'C':
            cartype = '四门轿车 GLX/四门轿车 GLS，GLS/TDI四门轿车'
        elif sVIN[3] == 'D':
            cartype = '四门旅行轿车 GLS,GLS/TDI四门旅行轿车'
        elif sVIN[3] == 'B':
            cartype = '四门 GLS/TDI旅行车（加拿大）/GLX旅行车'
        elif sVIN[3] == 'C':
            cartype = '四门轿车 GLX/四门轿车 GLS，GLS/TDI四门轿车'
        elif sVIN[3] == 'D':
            cartype = '四门旅行轿车 GLS,GLS/TDI四门旅行轿车'
        elif sVIN[3] == 'E':
            cartype = '四门 GLX/Syncro 旅行轿车（加拿大）'
        elif sVIN[3] == 'F':
            cartype = '四门旅行车 GLX/四门轿车特制GL型/四门 GLS Syncro(加拿大)'
        elif sVIN[3] == 'G':
            cartype = '四门旅行车 GL型/四门 GL Syncro(加拿大)'
        elif sVIN[3] == 'H':
            cartype = '四门基本型轿车/四门 GLX Syncro旅行轿车（加拿大）'
        elif sVIN[3] == 'J':
            cartype = '四门 Deluxe GLX/GLS'
        elif sVIN[3] == 'M':
            cartype = '四门轿车 GLS/TDI'
        elif sVIN[3] == 'N':
            cartype = '四门旅行轿车特制 GLX型/四门旅行轿车，GLS型，GLS/TDI'
        elif sVIN[3] == 'P':
            cartype = '四门轿车 GLX型'
        elif sVIN[3] == 'R':
            cartype = '四门 GLS Syncro 旅行轿车 4WD'
        elif sVIN[3] == 'T':
            cartype = '四门 GLS Syncro/四门旅行轿车 GLS型 Syncro 旅行轿车'
        elif sVIN[3] == 'U':
            cartype = '四门轿车 GLX型 Syncro'
        elif sVIN[3] == 'W':
            cartype = '四门 GLX型 Syncro 旅行轿车'
        elif sVIN[3] == 'V':
            cartype = '四门 GLX型旅行轿车'
    elif sVIN[6:8] == '30':
        carxing = 'Fox'
        if sVIN[3] == 'A':
            cartype = '两门基本型'
        elif sVIN[3] == 'B' :
            cartype = '两门经济型'
        elif sVIN[3] == 'C' :
            cartype = '两门特制型'
        elif sVIN[3] == 'D':
            cartype = '两门旅行轿车'
        elif sVIN[3] == 'G':
            cartype = '四门特制型'
    elif sVIN[6:8] == '50':
        carxing = 'Corraolo'
    elif sVIN[6:8] == '70':
        carxing = 'Euro Van欧洲厢式车'
        if sVIN[3] == 'E':
            cartype = 'Eurovan Panel Van/Eurovan Camper'
        elif sVIN[3] == 'H' or sVIN[3]=='K' :
            cartype = 'Eurovan 三门/EurovanGLS'
        elif sVIN[3] == 'C' :
            cartype = '两门特制型'
        elif sVIN[3] == 'D':
            cartype = '两门旅行轿车'
        elif sVIN[3] == 'G':
            cartype = '四门特制型'
    if sVIN[5]=='0':
        safe = '主动式安全带'
    elif sVIN[5] == '1':
        safe = '驾驶员/乘员，前侧向，前头部安全气囊'
    elif sVIN[5] == '2':
        safe = '被动式腰下膝上手动安全带/主动式安全带，驾驶员/乘员/前侧安全气囊'
    elif sVIN[5] == '3':
        safe = '主动式安全带，驾驶员/乘员/前侧安全气囊'
    elif sVIN[5] == '4':
        safe = '主动式安全带，驾驶员/乘员/前侧/后侧安全气囊/"ELRA"带马达驱动式皮带驾驶员/乘员安全气囊'
    elif sVIN[5] == '5':
        safe = '主动式安全带驾驶员气囊，驾驶员/乘员前侧后侧，帘幕式安全气囊'
    elif sVIN[5] == '6':
        safe = '主动式安全带，驾驶员/乘员/前侧，侧面帘幕式安全气囊'
    elif sVIN[5] == '1':
        safe = '主动式安全带/双安全气囊'
    if sVIN[10]=='J':
        zpgc='Ingoistad'
    elif sVIN[10]=='N':
        zpgc='Neckarsulm'
    elif sVIN[10]=='B':
        zpgc='Brussels'
    elif sVIN[10]=='P':
        zpgc='Brazil'
    elif sVIN[10]=='E':
        zpgc='EMden'
    elif sVIN[10]=='S':
        zpgc='Stuttgart'
    elif sVIN[10]=='G':
        zpgc='Graz'
    elif sVIN[10]=='V':
        zpgc='Westenoreland'
    elif sVIN[10]=='H':
        zpgc='Honover'
    elif sVIN[10]=='W':
        zpgc='Wolfsburg'
    elif sVIN[10]=='K':
        zpgc='Osnabruck'
    elif sVIN[10]=='Y':
        zpgc='Spain(SEAT)'
    elif sVIN[10]=='M':
        zpgc='Mexico'

    return safe, pl, cartype, fdjandbsx, carxing, zpgc, year,company,cartype_q

def jkTOYOTA(sVIN):
    cartype = '*'
    pl = '*'
    fdjandbsx = '*'
    carxing = '*'
    safe = '*'
    year = 0
    year = getYear(sVIN[9])
    company = '日本丰田汽车公司'
    cartype_q = '*'
    zpgc = '*'
    if sVIN[2] == '2' or sVIN[2] == 'D':
        cartype_q = '轿车'
    elif sVIN[2]=='3' or sVIN[2] == '6':
        cartype_q = 'MPV 多用途车'
    elif sVIN[2] == '4':
        cartype_q = '载货汽车'
    elif sVIN[2] == '5':
        cartype_q = '非完整车辆'
    elif sVIN[2] == 'X':
        cartype_q = '(新联合汽车公司)轿车'
    elif sVIN[2] == '1':
        cartype_q = '轿车(美国)(加拿大)'
    elif sVIN[2] == 'A':
        cartype_q = '(美国，TABC公司)货车'
    elif sVIN[2] == 'B':
        cartype_q = '(美国印第安那州)货车'
    elif sVIN[2] == 'E':
        cartype_q = '(美国加州)货车'

    if sVIN[4] == 'A':
        fdjandbsx = '4A FE'
    elif sVIN[4] == 'B':
        fdjandbsx = '7A FE'
    elif sVIN[4] == 'C':
        fdjandbsx = '5E FE'
    elif sVIN[4] == 'D':
        fdjandbsx = '2JZ GE'
    elif sVIN[4] == 'E':
        fdjandbsx = '2TZ GTE'
    elif sVIN[4] == 'F':
        fdjandbsx = '1MZ FE'
    elif sVIN[4] == 'G':
        fdjandbsx = '5S FE'
    elif sVIN[4] == 'J':
        fdjandbsx = '1FE FE'
    elif sVIN[4] == 'K':
        fdjandbsx = '2TZ FZE'
    elif sVIN[4] == 'L':
        fdjandbsx = '2RZ FE'
    elif sVIN[4] == 'M':
        fdjandbsx = '3RZ FE'
    elif sVIN[4] == 'N':
        fdjandbsx = '5VE FE/5S FNE'
    elif sVIN[4] == 'P':
        fdjandbsx = '3S FE'
    elif sVIN[4] == 'R':
        fdjandbsx = '1ZZ FE'
    elif sVIN[4] == 'S':
        fdjandbsx = '1BM'
    elif sVIN[4] == 'T':
        fdjandbsx = '2UZ FE/1NZ FE'

    if fdjandbsx == '*':
        if sVIN[3]=='A':
            fdjandbsx = '4A FE/4A GE/2TZ FE/7A FE/2TZ FZE'
        elif sVIN[3]=='D':
            fdjandbsx = '1FZ FE,J-3E E/5E FE,F/3F E'
        elif sVIN[3]=='G':
            fdjandbsx = '1MZ FE,J-2JZ GE/2JZ GTE'
        elif sVIN[3]=='M':
            fdjandbsx = '7M GE/7M GTE  R-22R E'
        elif sVIN[3]=='S':
            fdjandbsx = '3S GTE/5S FE  U-3RZ FE'
        elif sVIN[3]=='V':
            fdjandbsx = '3VZ E/3VZ FE/VZ FE'
    if sVIN[7] == 'A':
        carxing = 'Supra'
    elif sVIN[7] == 'B':
        carxing = 'Avalon'
    elif sVIN[7] == 'C':
        carxing = 'Sienna'
    elif sVIN[7] == 'D':
        carxing = 'T100'
    elif sVIN[7] == 'E':
        carxing = 'Corolla'
    elif sVIN[7] == 'H':
        carxing = 'Paseo'
    elif sVIN[7] == 'J':
        carxing = 'Land Cruiser'
    elif sVIN[7] == 'K':
        carxing = 'Camry'
    elif sVIN[7] == 'L':
        carxing = 'Tecel'
    elif sVIN[7] == 'M':
        carxing = 'Previa'
    elif sVIN[7] == 'N':
        carxing = 'Tacoma'
    elif sVIN[7] == 'P':
        carxing = 'camry solara'
    elif sVIN[7] == 'R':
        carxing = '4Runner'
    elif sVIN[7] == 'T':
        carxing = 'Celica'
    elif sVIN[7] == 'V':
        carxing = 'RAV4'
    elif sVIN[7] == '0':
        carxing = 'MRZ'
    elif sVIN[7] == '1':
        carxing = 'TUNDRA'
    elif sVIN[7] == '2':
        carxing = 'ECHO'

    if carxing == '*':
        if sVIN[4]=='A':
            carxing = 'Supra'
        elif sVIN[4] == 'B':
            carxing = 'Avalon'
        elif sVIN[4] == 'C':
            carxing = 'Previa'
        elif sVIN[4] == 'D':
            carxing = 'T100'
        elif sVIN[4] == 'E':
            carxing = 'Corolla'
        elif sVIN[4] == 'J':
            carxing = 'Land Cruiser'
        elif sVIN[4] == 'K':
            carxing = 'Camry'
        elif sVIN[4] == 'L':
            carxing = 'Tecel/Paseo'
        elif sVIN[4] == 'N':
            carxing = 'Truck/4-Runner/Cab&chassis/Tacoma'
        elif sVIN[4] == 'T':
            carxing = 'Celica'
        elif sVIN[4] == 'W':
            carxing = 'MRZ'
        elif sVIN[4] == 'X':
            carxing = 'Cressida'
    if sVIN[10] >= '0' and sVIN[10]  <='9':
        zpgc = '日本'
    elif sVIN[10]== 'C':
        zpgc = '加拿大'
    elif sVIN[10]== 'U':
        zpgc = '美国堪萨斯州'
    elif sVIN[10]== 'Z':
        zpgc = '美国加州'
    return safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, cartype_q

def yqTOYOTA(sVIN):
    cartype = '*'
    pl = '*'
    fdjandbsx = '*'
    carxing = '*'
    safe = '*'
    year = 0
    year = getYear(sVIN[9])
    company = '天津丰田汽车有限公司'
    cartype_q = '*'
    zpgc = '*'
    if sVIN[4] == '2':
        pl = '1.1-1.3L'
    elif sVIN[4] == '3':
        pl = '1.4-1.6L'
    elif sVIN[4] == '4':
        pl = '1.7-2.0L'
    if sVIN[5] == 'A':
        fdjandbsx = '前置汽油发动机，前轮驱动 FF'
    elif sVIN[5] == 'B':
        fdjandbsx = '前置汽油发动机，后轮驱动 FR'
    elif sVIN[5] == 'C':
        fdjandbsx = '前置汽油发动机，全轮驱动 AWD'
    if sVIN[6] == 'B' or sVIN[6] == 'L':
        cartype = '四门三厢式车身'
    elif sVIN[6] == 'E' or sVIN[6] == 'H':
        cartype = '四门二厢式车身'
    if sVIN[7] == '1' :
        safe = '手动安全带'
    elif sVIN[7] == '2':
        safe = '手动安全带，驾驶员安全气囊'
    elif sVIN[7] == '3':
        safe = '手动安全带，驾驶员及前座乘员安全气囊'
    elif sVIN[7] == 'A' :
        safe = '自动安全带'
    elif sVIN[7] == 'B':
        safe = '自动安全带，驾驶员安全气囊'
    elif sVIN[7] == 'C':
        safe = '自动安全带，驾驶员及前座乘员安全气囊'
    return safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, cartype_q

def gzBT(sVIN):
    cartype = '*'
    pl = '*'
    fdjandbsx = '*'
    carxing = '*'
    safe = '*'
    year = 0
    year = getYear(sVIN[9])
    company = '中国广州本田汽车有限公司'
    cartype_q = '*'
    zpgc = '*'
    if sVIN[3:6]=='CM4':
        carxing = '雅阁 Accord/K20A7,K20A8'
    elif sVIN[3:6]=='CM5':
        carxing = '雅阁 Accord/K24A4'
    elif sVIN[3:6] == 'CM6':
        carxing = '雅阁 Accord/J30A4'
    if sVIN[6] == '5':
        cartype = '四门轿车'
        fdjandbsx = '五速手动变速器'
    elif sVIN[6] == '6':
        cartype = '四门轿车'
        fdjandbsx = '五速自动变速器'
    if sVIN[10]=='2':
        zpgc = '广州本田汽车有限公司'
    return safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, cartype_q

def bjXD(sVIN):
    cartype = '*'
    pl = '*'
    fdjandbsx = '*'
    carxing = '*'
    safe = '*'
    year = 0
    year = getYear(sVIN[9])
    company = '北京现代汽车有限公司'
    cartype_q = '*'
    zpgc = '*'
    if sVIN[3] == 'S':
        carxing = '索纳塔车型系列'
    if sVIN[5] == 'C':
        cartype = '四门轿车'
    if sVIN[6]=='B':
        fdjandbsx = '2.0L发动机'
    elif sVIN[6] == 'H':
        fdjandbsx = '2.7L汽油发动机'
    elif sVIN[6] == 'L':
        fdjandbsx = '2.0L液化石油气发动机'
    if sVIN[7] == 'C':
        fdjandbsx = fdjandbsx +'/手动变速器'
        safe = '无安全气囊'
    elif sVIN[7] == 'H':
        fdjandbsx = fdjandbsx +'/手动变速器'
        safe = '带安全气囊'
    elif sVIN[7] == 'K':
        fdjandbsx = fdjandbsx +'/自动变速器'
        safe = '带安全气囊'
    if sVIN[10]=='X':
        zpgc = '北京现代汽车有限公司'
    return safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, cartype_q
def mgGM(sVIN):
    cartype = '*'
    pl = '*'
    fdjandbsx = '*'
    carxing = '*'
    safe = '*'
    year = 0
    year = getYear(sVIN[9])
    company = '*'
    cartype_q = '*'
    zpgc = '*'
    if sVIN[1] == 'G':
        company = '通用汽车公司/铃木汽车公司'
    elif sVIN[1] == 'C':
        company = 'CAMI汽车分部'
    elif sVIN[1] == 'L':
        company = '大宇汽车公司'
    elif sVIN[1] == '8':
        company = '五十铃汽车公司'
    elif sVIN[1] == 'Y':
        company = 'NUMMI拉美分部'
    elif sVIN[1] == '0':
        company = '欧宝汽车公司'

    if sVIN[2] == '1':
        if sVIN[3:5] == 'AW':
            carxing = 'Celebrity 名人'
        elif sVIN[3:5] == 'BL':
            carxing = 'Caprice Std 顺风 随想曲标准型'
        elif sVIN[3:5] == 'BN':
            carxing = 'Caprice Classic 古典式顺风随想曲'
        elif sVIN[3:5] == 'BU':
            carxing = 'Caprice Brougham 随想曲布鲁哈姆'
        elif sVIN[3:5] == 'FP':
            carxing = 'Camaro 卡玛洛跑车和活顶汽车'
        elif sVIN[3:5] == 'GW':
            carxing = 'El Camaro 卡玛洛'
        elif sVIN[3:5] == 'GZ':
            carxing = 'Monte Carlo 蒙特卡洛'
        elif sVIN[3:5] == 'JC' or sVIN[3:5] == 'JZ':
            carxing = 'Cavalier 骑士标准型'
        elif sVIN[3:5] == 'JD':
            carxing = 'Cavalier 骑士 CS型'
        elif sVIN[3:5] == 'JE':
            carxing = 'Cavalier 骑士 RS型'
        elif sVIN[3:5] == 'JF':
            carxing = 'Cavalier 骑士 LS,Z24型和活顶汽车'
        elif sVIN[3:5] == 'LD':
            carxing = 'Corsica 柯西佳'
        elif sVIN[3:5] == 'LS':
            carxing = 'Corsica LS型'
        elif sVIN[3:5] == 'LT':
            carxing = 'Corsica LT型'
        elif sVIN[3:5] == 'LV':
            carxing = 'Beretta 贝雷塔'
        elif sVIN[3:5] == 'LW':
            carxing = 'Beretta 贝雷塔 Z26/Beretta GT型'
        elif sVIN[3:5] == 'LZ':
            carxing = 'Beretta GTZ型'
        elif sVIN[3:5] == 'MR':
            carxing = 'Metro or S#print Sted CL 梅特罗和斯普林特标准型，CL'
        elif sVIN[3:5] == 'MS':
            carxing = 'S#print ER 斯普林特 ER'
        elif sVIN[3:5] == 'NE':
            carxing = 'Malibu LS型'
        elif sVIN[3:5] == 'ND':
            carxing = 'Malibu LX型'
        elif sVIN[3:5] == 'RF':
            carxing = 'Spectrum 斯佩克特朗'
        elif sVIN[3:5] == 'SK':
            carxing = 'Nova 诺瓦/Prizm'
        elif sVIN[3:5] == 'TB':
            carxing = 'Chevette 雪维特 CS'
        elif sVIN[3:5] == 'TJ':
            carxing = 'Chevette 雪维特'
        elif sVIN[3:5] == 'WF':
            carxing = 'Impala'
        elif sVIN[3:5] == 'WH':
            carxing = 'Impala LS,LTZ型'
        elif sVIN[3:5] == 'WL':
            carxing = 'Lumina LS型/Lumina 鲁米娜（轿车）'
        elif sVIN[3:5] == 'WM':
            carxing = 'Lumina 鲁米娜跑车（Coupe）'
        elif sVIN[3:5] == 'WN':
            carxing = 'Lumina 鲁米娜 Eurosport/LS /Lumina LTZ'
        elif sVIN[3:5] == 'WP':
            carxing = 'Lumina 鲁米娜 Z34'
        elif sVIN[3:5] == 'WW':
            carxing = 'Monte carlo LS型'
        elif sVIN[3:5] == 'WX':
            carxing = 'Monte carlo SS'
        elif sVIN[3:5] == 'YY':
            carxing = 'Corvette 克尔维特和活顶车/基本型/运动型'
        elif sVIN[3:5] == 'YZ':
            carxing = 'Corvette ZR1 克尔维特 ZR1型'
        elif sVIN[3:5] == 'BJ':
            carxing = 'Tracker 追踪者'
        elif sVIN[3:5] == 'MR':
            carxing = 'Metro Std & LSi 型梅特罗标准型/Metro GSI(加拿大)梅特罗 GSI型'
        elif sVIN[3:5] == 'MS':
            carxing = 'Metro XFi 梅特罗 XFi型'
        elif sVIN[3:5] == 'MT':
            carxing = 'Metro Base(加拿大)梅特罗基本型'
        elif sVIN[3:5] == 'RF':
            carxing = 'Spectrum 斯佩克特朗双门/Storm 斯托姆双门'
        elif sVIN[3:5] == 'RG':
            carxing = 'Spectrum 斯佩克特朗四门'
        elif sVIN[3:5] == 'RT':
            carxing = 'Storm 斯托姆 GSi型'
        elif sVIN[3:5] == 'SK':
            carxing = 'Prizm 普瑞姆 Std LSi 型'
        elif sVIN[3:5] == 'SL':
            carxing = 'Prizm GSi 普瑞姆 GSi 型'
    elif sVIN[2]=='2':
        if sVIN[3:5] == 'AE':
            carxing = 'Pontiac 600 SE 型'
        elif sVIN[3:5] == 'AF':
            carxing = 'Pontiac 600 标准型'
        elif sVIN[3:5] == 'AG':
            carxing = 'Pontiac 600 LE 型'
        elif sVIN[3:5] == 'AJ':
            carxing = 'Pontiac 600 SE(特经济型)'
        elif sVIN[3:5] == 'BL':
            carxing = 'Parisienne 标准型'
        elif sVIN[3:5] == 'FS':
            carxing = 'Firebird 火鸟标准型和活顶车'
        elif sVIN[3:5] == 'FV':
            carxing = 'Firebird 火鸟 Formula,Frans AM 和活顶车'
        elif sVIN[3:5] == 'FW':
            carxing = 'Firebird 火鸟 Trans AM 和活顶车'
        elif sVIN[3:5] == 'GJ':
            carxing = 'Grand Prix 大普里克斯标准型'
        elif sVIN[3:5] == 'GK':
            carxing = 'Grand Prix 大普里克斯LE型'
        elif sVIN[3:5] == 'GP':
            carxing = 'Grand Prix Brougham 大普里克斯布鲁哈姆'
        elif sVIN[3:5] == 'HX':
            carxing = 'Bonneville 邦内维尔标准型及SE型'
        elif sVIN[3:5] == 'HY':
            carxing = 'Bonneville SLE型/Bonneville 邦内维尔 SSEi型'
        elif sVIN[3:5] == 'HZ':
            carxing = 'Bonneville 邦内维尔 SSEI型/Bonneville SSEi型/SSE'
        elif sVIN[3:5] == 'JB':
            carxing = 'Sunbird 太阳鸟标准型和活顶车/基本型 /Sunbird SE太阳鸟标准型和活顶车'
        elif sVIN[3:5] == 'JC':
            carxing = 'Sunbird 基本型/LE型'
        elif sVIN[3:5] == 'JD':
            carxing = 'Sunbird GT型/SE型'
        elif sVIN[3:5] == 'JL':
            carxing = 'Sunbird 太阳鸟 SE 标准型'
        elif sVIN[3:5] == 'JU':
            carxing = 'Sunbird 太阳鸟 GT 标准型'
        elif sVIN[3:5] == 'MR':
            carxing = 'Firefly LE型增压'
        elif sVIN[3:5] == 'MT':
            carxing = 'Firefly Std LE 萤火虫标准型'
        elif sVIN[3:5] == 'NE':
            carxing = 'Grand Am 大艾姆 Std 标准型/SE型'
        elif sVIN[3:5] == 'NG':
            carxing = 'Grand Am 基本型'
        elif sVIN[3:5] == 'NV':
            carxing = 'Grand Am 大艾姆 LE型'
        elif sVIN[3:5] == 'NW':
            carxing = 'Grand Am 大艾姆 SE,GT型'
        elif sVIN[3:5] == 'PE':
            carxing = 'Fiero SE 菲埃罗 SE型'
        elif sVIN[3:5] == 'PF':
            carxing = 'Fiero 菲埃罗运动型'
        elif sVIN[3:5] == 'PG':
            carxing = 'Fiero GT 菲埃罗 GT型'
        elif sVIN[3:5] == 'PM':
            carxing = 'Fiero 菲埃罗标准型'
        elif sVIN[3:5] == 'TL':
            carxing = 'Pontiac 旁蒂克 1000'
        elif sVIN[3:5] == 'TN':
            carxing = 'LeMans 莱曼斯'
        elif sVIN[3:5] == 'TR' or sVIN[3:5] == 'TS' or sVIN[3:5] == 'TX':
            carxing = 'Lemans'
        elif sVIN[3:5] == 'WH':
            carxing = 'Grand Prix LE型'
        elif sVIN[3:5] == 'WJ':
            carxing = 'Grand Prix 大普里克斯 LE型/Grand Prix 大普里克斯 SE型'
        elif sVIN[3:5] == 'WK':
            carxing = 'Grand Prix LE型'
        elif sVIN[3:5] == 'WP':
            carxing = 'Grand Prix 大普里克斯 SE型 /Grand Prix GT /Grand Prix SE型'
        elif sVIN[3:5] == 'WM':
            carxing = 'Grand Prix'
        elif sVIN[3:5] == 'WR':
            carxing = 'Grand Prix GTP'
        elif sVIN[3:5] == 'WT':
            carxing = 'Grand Prix GTE'
    elif sVIN[2] == '3':
        if sVIN[3:5] == 'AG':
            carxing = 'Ciera 锡拉S型'
        elif sVIN[3:5] == 'AJ':
            carxing = 'Ciera SL型/Cutlass Cruiser SL型 /Ciera 锡拉（S型）ES,GT&LS型'
        elif sVIN[3:5] == 'AL':
            carxing = 'Ciera'
        elif sVIN[3:5] == 'AM':
            carxing = 'Ciera Brougham 锡拉布鲁哈姆'
        elif sVIN[3:5] == 'BP':
            carxing = 'Custom Cruiser 卡斯特姆巡航舰'
        elif sVIN[3:5] == 'CV':
            carxing = '98 Touring Sedan 98旅游轿车'
        elif sVIN[3:5] == 'CW':
            carxing = '98 Regency Brougham 98 摄政王朝布鲁哈姆'
        elif sVIN[3:5] == 'CX':
            carxing = '98 Regency 98 摄政王朝/Elite'
        elif sVIN[3:5] == 'EV':
            carxing = 'Toronado Trofeo'
        elif sVIN[3:5] == 'EZ':
            carxing = 'Toronado Brougham 托罗纳多布鲁哈姆'
        elif sVIN[3:5] == 'GK':
            carxing = 'Cutlass Salon & 442 短箭沙龙和 442'
        elif sVIN[3:5] == 'GM':
            carxing = 'Cutlass Supreme Brougham 超级短箭布鲁哈姆'
        elif sVIN[3:5] == 'GR':
            carxing = 'Cutlass Supreme 超级短箭/Aurora'
        elif sVIN[3:5] == 'GS':
            carxing = 'Aurora'
        elif sVIN[3:5] == 'HC':
            carxing = '88Regency/Regency'
        elif sVIN[3:5] == 'HN':
            carxing = 'Delta 88 Royale 德尔塔 88 皇室 /88LS型 /88/Royale'
        elif sVIN[3:5] == 'HY':
            carxing = 'Delta 88 Royale Brougham/LS德尔塔 88 皇室布鲁哈姆/LS型 /88/Royale LS型 /LSS'
        elif sVIN[3:5] == 'JC':
            carxing = 'Firenza 佛罗伦萨标准型和S型'
        elif sVIN[3:5] == 'JD':
            carxing = 'Firenza 佛罗伦萨 GT,LC&LX型'
        elif sVIN[3:5] == 'NG' or sVIN[3:5] == 'NB':
            carxing = 'Cutlass'
        elif sVIN[3:5] == 'NF':
            carxing = 'Achieva 大勋章 SL,SC型 /Alero GLS /Calais 加莱Std,ES & GT型'
        elif sVIN[3:5] == 'NK':
            carxing = 'Alero GX型'
        elif sVIN[3:5] == 'NF':
            carxing = 'Calais 加莱 Std,ES & GT型'
        elif sVIN[3:5] == 'NK':
            carxing = 'Alero GX型'
        elif sVIN[3:5] == 'NL':
            carxing = 'Achieva 大勋章S型 /Achieva SL,SC /Alero GL型'
        elif sVIN[3:5] == 'NK':
            carxing = 'Calais International万国加莱'
        elif sVIN[3:5] == 'NT':
            carxing = 'Calais Supreme 超级加莱'
        elif sVIN[3:5] == 'WH':
            carxing = 'Intrigue GX /Cutlass Supreme 超级短箭/S型'
        elif sVIN[3:5] == 'WR':
            carxing = 'Cutlass Supreme International 超级短箭万国'
        elif sVIN[3:5] == 'WS':
            carxing = 'Cutlass Supreme 超级短箭SL型 /Intrigue GL型'
        elif sVIN[3:5] == 'WT':
            carxing = 'Cutlass Supreme 敞篷型超级短箭活顶车'
        elif sVIN[3:5] == 'WX':
            carxing = 'Intrigue GLS型'
    elif sVIN[2] == '4':
        if sVIN[3:5] == 'AG':
            carxing = 'Century Special(Cpe & Sed)世纪特殊型 /Century Special(SW)世纪特殊型'
        elif sVIN[3:5] == 'AH':
            carxing = 'Century Custom 世纪(特制型)'
        elif sVIN[3:5] == 'AL':
            carxing = 'Century Estate Wagon(SW)世纪旅行轿车 /Century Limited(Cpe & Sed)世纪顶级型 /Roadmaster 路霸轿车'
        elif sVIN[3:5] == 'BN':
            carxing = 'Roadmaster 路霸'
        elif sVIN[3:5] == 'BR':
            carxing = 'LeSabre Estate 旅行轿车 /Roadmaster Wagon 路霸旅行轿车 /Roadmaster 路霸标准型轿车'
        elif sVIN[3:5] == 'BT':
            carxing = 'Roadmaster Limited 路霸顶级型'
        elif sVIN[3:5] == 'BV':
            carxing = 'Electra(依勒克拉)Estate 旅行轿车'
        elif sVIN[3:5] == 'CF':
            carxing = 'Electra(依勒克拉)T型'
        elif sVIN[3:5] == 'CU':
            carxing = 'Park Avenue Ultra 林荫大道（派克大街）'
        elif sVIN[3:5] == 'CW':
            carxing = 'Electra Park Avenue 依勒克特拉林荫大道 /Park Avenue'
        elif sVIN[3:5] == 'CX':
            carxing = 'Electra Limited(380)依勒克特拉顶级型'
        elif sVIN[3:5] == 'EZ':
            carxing = 'Riviera Luxury 里维埃拉（利雅）豪华型'
        elif sVIN[3:5] == 'GD':
            carxing = 'Riviera'
        elif sVIN[3:5] == 'GJ':
            carxing = 'Regal Std 君威标准型'
        elif sVIN[3:5] == 'GM':
            carxing = 'Regal Limited 君威顶级型'
        elif sVIN[3:5] == 'HH':
            carxing = 'LeSabre Std 名使标准型'
        elif sVIN[3:5] == 'HP':
            carxing = 'LeSabr Custom 名使特制型'
        elif sVIN[3:5] == 'HR':
            carxing = 'LeSabr Limited 名使顶级型'
        elif sVIN[3:5] == 'JE':
            carxing = 'Skykawk T型'
        elif sVIN[3:5] == 'JS':
            carxing = 'Skykawk Custom(Cpe,Sed)天鹰定制型/Skykawk Sport(HB)天鹰运动型'
        elif sVIN[3:5] == 'NC' or sVIN[3:5] == 'NJ':
            carxing = 'Skylark Custom 云雀定制型/Skylark Limited 云雀顶级型'
        elif sVIN[3:5] == 'NM':
            carxing = 'Skylark Limited 云雀顶级型(双门跑车)/Somerset Limted 萨默赛特顶级型（双门跑车）/Skylark Gran Sport 云雀运动型（双门跑车）'
        elif sVIN[3:5] == 'NV':
            carxing = 'Skylark Custom 云雀定制型'
        elif sVIN[3:5] == 'WB':
            carxing = 'Regal Custom 君威定制LS型'
        elif sVIN[3:5] == 'WD' or sVIN[3:5] == 'WK':
            carxing = 'Regal Limited 君威顶级型'
        elif sVIN[3:5] == 'WF':
            carxing = 'Regal Gran Sport 君威运动型'
        elif sVIN[3:5] == 'WM':
            carxing = 'Regal Std 君威标准型'
        elif sVIN[3:5] == 'WS':
            carxing = 'Century Custom 世纪特制型'
        elif sVIN[3:5] == 'WY':
            carxing = '世纪顶级型'
    elif sVIN[2] == '6':
        if sVIN[3:5] == 'CB':
            carxing = 'Fleetwood(FWD)佛利特伍德（前轮驱动）'
        elif sVIN[3:5] == 'CD':
            carxing = 'Deville(FWD)帝威（都市）（前轮驱动）'
        elif sVIN[3:5] == 'CG' or sVIN[3:5] == 'CS':
            carxing = 'Fleetwood(FWD)四门 Sedon 佛利特伍德（前轮驱动）'
        elif sVIN[3:5] == 'CT':
            carxing = 'Deville Touring 帝威（都市）旅游观光车'
        elif sVIN[3:5] == 'CZ':
            carxing = 'Commercial Chassis 商用车底盘'
        elif sVIN[3:5] == 'DW':
            carxing = 'Fleetwood Brugham(RWD)佛利特伍德布鲁哈姆（后轮驱动）'
        elif sVIN[3:5] == 'EL':
            carxing = 'ELdorado 埃尔多拉多/EldoradoESC'
        elif sVIN[3:5] == 'ET':
            carxing = 'ELdorado (ETC) 埃尔多拉多/Eldorado,Touring'
        elif sVIN[3:5] == 'JG':
            carxing = 'Cimarron 西马龙'
        elif sVIN[3:5] == 'KD':
            carxing = 'Deville 帝威（都市）'
        elif sVIN[3:5] == 'KE':
            carxing = 'Deville D`Elegance /Deville 高级豪华型'
        elif sVIN[3:5] == 'KF':
            carxing = 'Concours 康克 /Deville(DTS型)'
        elif sVIN[3:5] == 'KS' or sVIN[3:5] == 'KY':
            carxing = 'Seville(SLS)塞维利亚（SLS型）'
        elif sVIN[3:5] == 'KZ':
            carxing = 'Seville(SES)'
        elif sVIN[3:5] == 'VS':
            carxing = 'Allante 阿伦特'
        elif sVIN[3:5] == 'VR':
            carxing = 'Allante 阿伦特 /Catera'

    if sVIN[0:3] == '1G1':
        cartype_q = '雪佛兰轿车'
    elif sVIN[0:3] == '1GD':
        cartype_q = '非完整载货汽车'
    elif sVIN[0:3] == '1G2':
        cartype_q = '旁蒂克轿车'
    elif sVIN[0:3] == '1GE':
        cartype_q = '凯迪拉克非完整汽车'
    elif sVIN[0:3] == '1G3':
        cartype_q = '奥兹莫比尔轿车'
    elif sVIN[0:3] == '1GG':
        cartype_q = '五十铃载货汽车'
    elif sVIN[0:3] == '1G4':
        cartype_q = '别克轿车'
    elif sVIN[0:3] == '1GH':
        cartype_q = '奥兹莫比尔多用途车MPV'
    elif sVIN[0:3] == '1G5':
        cartype_q = '旁蒂克非完整乘用车'
    elif sVIN[0:3] == '1GJ':
        cartype_q = '客车'
    elif sVIN[0:3] == '1G6':
        cartype_q = '凯迪拉克牌轿车'
    elif sVIN[0:3] == '1GK':
        cartype_q = '多用途乘用车MPV'
    elif sVIN[0:3] == '1G7':
        cartype_q = '加拿大生产汽车'
    elif sVIN[0:3] == '1GM':
        cartype_q = '多用途车 MPV(APV)'
    elif sVIN[0:3] == '1G8':
        cartype_q = '土星轿车'
    elif sVIN[0:3] == '1GN':
        cartype_q = '雪佛兰多用途车 MPV'
    elif sVIN[0:3] == '1GA':
        cartype_q = '雪佛兰轿车'
    elif sVIN[0:3] == '1GT':
        cartype_q = 'GMC载货汽车'
    elif sVIN[0:3] == '1GB':
        cartype_q = '非完整载货汽车'
    elif sVIN[0:3] == '1GY':
        cartype_q = '旁蒂克载货汽车'
    elif sVIN[0:3] == '1GC':
        cartype_q = '雪佛兰载货汽车'
    elif sVIN[0:3] == '4G2':
        cartype_q = '旁蒂克轿车'
    elif sVIN[0:3] == '4G3':
        cartype_q = '丰田汽车'
    elif sVIN[0:3] == '4GD':
        cartype_q = '欧宝 APV/MPV'
    elif sVIN[0:3] == '4GL':
        cartype_q = '别克非完整汽车'
    elif sVIN[0:3] == '4GT':
        cartype_q = '五十铃非完整汽车'
    elif sVIN[0:3] == '4G5':
        cartype_q = '电动汽车'
    elif sVIN[0:3] == '4KB':
        cartype_q = '雪佛兰非完整汽车'
    elif sVIN[0:3] == '4KD':
        cartype_q = 'GMC非完整载货起车'
    elif sVIN[0:3] == '4KL':
        cartype_q = '通用公司生产汽车/五十铃非完整汽车'
    elif sVIN[0:3] == '4G1':
        cartype_q = '雪佛兰轿车'
    if sVIN[5]=='1':
        cartype = '双门跑车，轿车Sedan'
    elif sVIN[5]=='2':
        cartype = '双门溜背式，运动型跑车 Coupe'
    elif sVIN[5]=='3':
        cartype = '双门活动顶篷车'
    elif sVIN[5]=='4':
        cartype = '溜背式（舱门式 Hatchback）'
    elif sVIN[5]=='5':
        cartype = '四门轿车Sedan'
    elif sVIN[5]=='6':
        cartype = '四门溜背式'
    elif sVIN[5]=='8' or sVIN[5]=='9':
        cartype = '四门旅行车'
    if sVIN[6] == '1':
        safe = '主动式手动安全带'
    elif sVIN[6] == '2':
        safe = '手动安全带及驾驶员，前排乘员充气式安全保护系统'
    elif sVIN[6] == '3':
        safe = '主动式手动安全带驾驶员前乘员安全气囊及驾驶员侧向气囊'
    elif sVIN[6] == '4':
        safe = '自动安全带'
    elif sVIN[6] == '5':
        safe = '自动安全带及驾驶员充气安全保护系统'
    elif sVIN[6] == '6':
        safe = '手动安全带驾驶员，前乘员前部和侧向安全气囊'
    elif sVIN[6] == '7':
        safe = '手动安全带驾驶员前部侧向安全气囊和候补乘客侧气囊'
    if sVIN[7] == 'A':
        fdjandbsx = '2.3L L4 MFI(LGO)'
    elif sVIN[7] == 'B':
        fdjandbsx = '4.9L V8 SPFI/MFI(L26)'
    elif sVIN[7] == 'C':
        fdjandbsx = '4.0L V8 SFI(L47)'
    elif sVIN[7] == 'D':
        fdjandbsx = '3.1L V6 TBI'
    elif sVIN[7] == 'E':
        fdjandbsx = '3.4L V6MFI(LA1)'
    elif sVIN[7] == 'F':
        fdjandbsx = '5.0L V8 TPI(LB9)'
    elif sVIN[7] == 'G':
        fdjandbsx = '5.7L V8 MFI(LSI)'
    elif sVIN[7] == 'H':
        fdjandbsx = '3.5L V6 MFI(LX5)'
    elif sVIN[7] == 'J':
        fdjandbsx = '3.1L V6 SFI(LG8)'
    elif sVIN[7] == 'K':
        fdjandbsx = '3.8L V6 MFI(L36)'
    elif sVIN[7] == 'L':
        fdjandbsx = '3.8L V6 MFI(L27)'
    elif sVIN[7] == 'M':
        fdjandbsx = '3.1L V6 MFI(L82)'
    elif sVIN[7] == 'N':
        fdjandbsx = '3.3L V6 MFI(LG7)'
    elif sVIN[7] == 'P':
        fdjandbsx = '5.7L V8 MFI(LT1)'
    elif sVIN[7] == 'R':
        fdjandbsx = '3.0L V6 MFI(L32)'
    elif sVIN[7] == 'S':
        fdjandbsx = '5.7L V8 SFI(LSb)'
    elif sVIN[7] == 'T':
        fdjandbsx = '2.4L L4 MFI(LD9)'
    elif sVIN[7] == 'U':
        fdjandbsx = '1.6L L4 TBI(LS5)'
    elif sVIN[7] == 'V':
        fdjandbsx = '3.1L V6 EFI(LG5)'
    elif sVIN[7] == 'W':
        fdjandbsx = '4.3L V8 SPFI'
    elif sVIN[7] == 'X':
        fdjandbsx = '3.4L V6 SPFI(LQ1)'
    elif sVIN[7] == 'Y':
        fdjandbsx = '4.6L V8 MFI(LD8)'
    elif sVIN[7] == 'Z':
        fdjandbsx = '4.3L V6 TBI(LB4)'
    elif sVIN[7] == '0':
        fdjandbsx = '1.8L EFI'
    elif sVIN[7] == '1':
        fdjandbsx = '3.8L(L67)V6 SFI'
    elif sVIN[7] == '2':
        fdjandbsx = '1.3L L4 MFI(LY8)'
    elif sVIN[7] == '3':
        fdjandbsx = '1.3L L4 MFI'
    elif sVIN[7] == '4':
        fdjandbsx = '2.2L(LN2)L4 MFI'
    elif sVIN[7] == '5':
        fdjandbsx = '5.7L V8 MFI(LT4)'
    elif sVIN[7] == '6':
        fdjandbsx = '1.0L L3 TBI(LP2)/1.0L L4 MFI(L01)'
    elif sVIN[7] == '7':
        fdjandbsx = '5.7L V8(LO5)TBI'
    elif sVIN[7] == '8':
        fdjandbsx = '1.8L L4 MFI(LQ6)'
    elif sVIN[7] == '9':
        fdjandbsx = '4.6L V8 MFI(L37)'
    return safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, cartype_q

def dgBSJ(sVIN):
    cartype = '*'
    pl = '*'
    fdjandbsx = '*'
    carxing = '*'
    safe = '*'
    year = 0
    year = getYear(sVIN[9])
    company = '德国波尔舍（保时捷）研究设计开发股份公司'
    cartype_q = '*'
    zpgc = '*'

    if sVIN[1:3]=='P0':
        company = 'F.Porsche AG.'
    if sVIN[3] == 'A':
        cartype = '两门 Coupe 911,928,944,924s,968'
    elif sVIN[3] == 'B':
        cartype = '两门 Targa Carrera 2/4'
    elif sVIN[3] == 'C':
        cartype = 'Carrera 2/4 Cabriolet,944/968 Cabriolet /Boxter,Boxter S型汽车'
    elif sVIN[3] == 'D':
        cartype = '两门 Targa,Carrera 2/4'
    elif sVIN[3] == 'E':
        cartype = '两门 Targa或Cabriolet汽车'
    elif sVIN[3] == 'J':
        cartype = '两门 Coupe 911'

    if sVIN[4] == 'A':
        fdjandbsx = 'Boxster 2.7L 发动机/Carrera 3.4L发动机'
    elif sVIN[4] == 'B':
        fdjandbsx = 'Boxster-S 3.2L 发动机/911 3.6L Carrera'
    elif sVIN[4] == 'C':
        fdjandbsx = '911 Turbo 3.6L 发动机/Turbo 增压型发动机'
    if sVIN[5] == '0':
        safe = '主动式防护系统'
    elif sVIN[5] == '1':
        safe = '被动式防护系统'
    elif sVIN[5] == '2':
        safe = '安全气囊/侧向安全气囊'
    if sVIN[6:8] == '91':
        carxing = '911 Carrera 型汽车'
    elif sVIN[6:8] == '92':
        carxing = '924S 928'
    elif sVIN[6:8] == '93':
        carxing = '911 Turbo(增压型汽车)'
    elif sVIN[6:8] == '94':
        carxing = '944型汽车'
    elif sVIN[6:8] == '95':
        carxing = '944型汽车'
    elif sVIN[6:8] == '96':
        carxing = 'Carrera 2/4 Turbo /968型汽车'
    elif sVIN[6:8] == '98':
        carxing = 'Boster/Boxter S'
    elif sVIN[6:8] == '99':
        carxing = '911 Carrera'
    if sVIN[10] == 'N':
        zpgc = 'Neckarsulm 德国'
    elif sVIN[10] == 'S':
        zpgc = 'Stuttgart 德国'
    elif sVIN[10] == 'U':
        zpgc = 'Unsikaunki 芬兰'
    return safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, cartype_q

def ygLH(sVIN):
    cartype = '*'
    pl = '*'
    fdjandbsx = '*'
    carxing = '*'
    safe = '*'
    year = 0
    year = getYear(sVIN[9])
    company = '联合王国Land Rover公司'
    cartype_q = '*'
    zpgc = '*'
    if sVIN[3:5]=='DH':
        carxing = 'Defender(防御者)'
    elif sVIN[3:5]=='DV':
        carxing = 'Defender(可卸式车顶)'
    elif sVIN[3:5]=='HC':
        carxing = 'Range Rover 轴距 108'
    elif sVIN[3:5]=='HE':
        carxing = 'Range Rover 轴距 100 加州'
    elif sVIN[3:5]=='HF':
        carxing = 'Range Rover 轴距 108 加州'
    elif sVIN[3:5]=='HV':
        carxing = 'Range Rover 轴距 100'
    elif sVIN[3:5]=='JN':
        carxing = 'Discovery(发现牌)加州'
    elif sVIN[3:5]=='JY':
        carxing = 'Discovery'
    elif sVIN[3:5]=='PA':
        carxing = 'Range Rover GEMS Fuel'
    elif sVIN[3:5]=='PC':
        carxing = 'Range Rover Callaway Eng'
    elif sVIN[3:5]=='PE':
        carxing = 'Range Rover 加州'
    elif sVIN[3:5]=='PF':
        carxing = 'Range Rover spec.2/Range Rover spec.1'
    elif sVIN[3:5]=='PV':
        carxing = 'Range Rover (兰治罗孚)'
    elif sVIN[3:5]=='TY':
        carxing = 'Discovery II系列'
    if sVIN[5] == '1':
        cartype = '四门旅行车'
    elif sVIN[5] == '2':
        cartype = '两门 Defender 90'
    if sVIN[6] == '1':
        fdjandbsx = '3.5L V8 电喷（EFI）'
    elif sVIN[6] == '2':
        fdjandbsx = '3.9L 4.0L V8 电喷'
    elif sVIN[6] == '3':
        fdjandbsx = '4.2L V8 电喷'
    elif sVIN[6] == '4':
        fdjandbsx = '4.6L V8 电喷'
    elif sVIN[6] == '5':
        fdjandbsx = '4.0L V8 EFI.LEV'
    elif sVIN[6] == '6':
        fdjandbsx = '4.6L V8 EFI.LEV'
    if sVIN[7]=='4':
        fdjandbsx = fdjandbsx + ' 自动变速器 LHS'
    elif sVIN[7] == '8':
        fdjandbsx = fdjandbsx + ' 五速手动变速器'
    if sVIN[10] == 'A':
        zpgc = 'Solihull 联合王国（UK）'
    return safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, cartype_q
'''ss = 'UU6JA69691D713820'
if checkVIN(ss) == True:
    #print '111111111111111111'''''

def gqcq(sVIN):
    cartype = '*'
    pl = '*'
    fdjandbsx = '*'
    carxing = '*'
    safe = '*'
    year = 0
    year = getYear(sVIN[9])
    company = '广汽乘用车有限公司'
    cartype_q = '*'
    zpgc = '*'
    if sVIN[3] == 'D':
        carxing = 'GS5'
    elif sVIN[3] == 'F':
        carxing = 'GA3'
    elif sVIN[3] == 'A':
        carxing = 'GS4'
    elif sVIN[3] == 'B':
        carxing = 'GA5/GA6'
    elif sVIN[3] == 'G':
        carxing = 'GA5电动'
    if sVIN[4] == 'K':
        fdjandbsx = '4B20K2'
    if sVIN[5] == '1':
        fdjandbsx = fdjandbsx + ' 前轮驱动'
    elif sVIN[5] == '3':
        fdjandbsx = fdjandbsx + ' 四轮驱动'
    if sVIN[6] == '3':
        fdjandbsx = fdjandbsx + ' 手动变速器'
    elif sVIN[6] == 'G':
        fdjandbsx = fdjandbsx + ' 自动变速器' 
    elif sVIN[6] == '7':
        fdjandbsx = fdjandbsx + ' AMT(机械式自动变速器)'   
    elif sVIN[6] == 'C':
        fdjandbsx = fdjandbsx + ' 双离合变速器'    
    elif sVIN[6] == 'S':
        fdjandbsx = fdjandbsx + ' 电动车单速变速箱'    
    return safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, cartype_q

def jl1(sVIN):
    cartype = '*'
    pl = '*'
    fdjandbsx = '*'
    carxing = '*'
    safe = '*'
    year = 0
    year = getYear(sVIN[9])
    company = '*'
    cartype_q = '*'
    zpgc = '*'
    if sVIN[0:3] == 'LB3':
        company = '浙江豪情汽车制造有限公司'
        if sVIN[10] == 'H':
            zpgc = '浙江豪情汽车制造有限公司'
        elif sVIN[10] == 'L':
            zpgc = '浙江豪情汽车制造有限公司第一分公司'
        elif sVIN[10] == 'X':
            zpgc = '浙江豪情汽车制造有限公司湘潭分公司'
        elif sVIN[10] == 'J':
            zpgc = '浙江豪情汽车制造有限公司济南分公司'
        elif sVIN[10] == 'C':
            zpgc = '浙江豪情汽车制造有限公司成都分公司'
        elif sVIN[10] == 'B':
            zpgc = '浙江豪情汽车制造有限公司宝鸡分公司'
        elif sVIN[10] == 'A':
            zpgc = '浙江豪情汽车制造有限公司山西分公司'
    elif (sVIN[0:3] == 'L6T') or (sVIN[0:3] == 'LJU'):
        company = '浙江吉利汽车有限公司'
        if sVIN[10] == 'W' or sVIN[10] == 'D':
            zpgc = '浙江吉利汽车有限公司宁波杭州湾工厂'
        elif sVIN[10] == 'U':
            zpgc = '浙江吉利汽车有限公司春晓工厂'
        elif sVIN[10] == 'L':
            zpgc = '浙江吉利汽车有限公司义乌分公司'
        elif sVIN[10] == 'L':
            zpgc = '浙江吉利汽车有限公司杭州分公司'
        elif sVIN[10] == 'L':
            zpgc = '浙江吉利汽车有限公司余姚工厂'
        elif sVIN[10] == 'L':
            zpgc = '浙江吉利汽车有限公司宁波杭州湾第二分公司'
        elif sVIN[10] == 'L':
            zpgc = '浙江吉利汽车有限公司梅山工厂'
        elif sVIN[10] == 'L':
            zpgc = '浙江吉利汽车有限公司成都分公司'
        elif sVIN[10] == 'L':
            zpgc = '浙江吉利汽车有限公司武汉分公司'
        elif sVIN[10] == 'L':
            zpgc = '浙江吉利汽车有限公司湖北分公司'
    elif sVIN[0:3] == 'LJ2':
        company = '山西新能源汽车工业有限公司'
        if sVIN[10] == 'A':
            zpgc = '山西新能源汽车工业有限公司乘用车生产线'
    elif sVIN[0:3] == 'L10':
        company = '成都高原汽车工业有限公司'
        if sVIN[10] == 'C':
            zpgc = '成都高原汽车工业有限公司'
    if sVIN[3] == '0':
        cartype_q = '底盘（非完整车辆）'
    elif sVIN[3] == '1':
        cartype_q = '载货汽车'
    elif sVIN[3] == '5':
        cartype_q = '专用汽车'
    elif sVIN[3] == '6':
        cartype_q = '客车'
    elif sVIN[3] == '7':
        cartype_q = '乘用车'
    if sVIN[3] == '6' or sVIN[3] == '7':
        if sVIN[4] == '0':
            cartype_q += ' 车长小于等于3.5米'
        elif sVIN[4] == '1':
            cartype_q += ' 车长大于3.5米小于等于3.6米'
        elif sVIN[4] == '2':
            cartype_q += ' 车长大于3.6米小于等于3.7米'
        elif sVIN[4] == '3':
            cartype_q += ' 车长大于3.7米小于等于3.8米'
        elif sVIN[4] == '4':
            cartype_q += ' 车长大于3.8米小于等于4.0米'
        elif sVIN[4] == '5':
            cartype_q += ' 车长大于4.0米小于等于4.2米'
        elif sVIN[4] == '6':
            cartype_q += ' 车长大于4.2米小于等于4.4米'
        elif sVIN[4] == '7':
            cartype_q += ' 车长大于4.4米小于等于4.6米'
        elif sVIN[4] == '8':
            cartype_q += ' 车长大于4.6米小于等于4.8米'
        elif sVIN[4] == '9':
            cartype_q += ' 车长大于等于4.8米'
    if sVIN[3] == '0' or sVIN[3] == '1' or sVIN[3] == '5':
        if sVIN[4] == 'K':
            cartype_q += ' 总质量小于等于1000'
        elif sVIN[4] == 'L':
            cartype_q += ' 总质量大于1000小于等于1500'
        elif sVIN[4] == 'M':
            cartype_q += ' 总质量大于1500小于等于2000'
        elif sVIN[4] == 'N':
            cartype_q += ' 总质量大于2000小于等于2500'
        elif sVIN[4] == 'P':
            cartype_q += ' 总质量大于2500小于等于3000'
        elif sVIN[4] == 'R':
            cartype_q += ' 总质量大于3000小于等于3500'
        elif sVIN[4] == 'S':
            cartype_q += ' 总质量大于3500小于等于4000'
        elif sVIN[4] == 'T':
            cartype_q += ' 总质量大于4000小于等于4500'
        elif sVIN[4] == 'U':
            cartype_q += ' 总质量大于4500小于等于5000'
        elif sVIN[4] == 'V':
            cartype_q += ' 总质量大于等于5000'
    if sVIN[5:7] == '02':
        fdjandbsx = '单燃料 汽油 发动机排量小于等于1'
        cartype = '2厢5门'
    elif sVIN[5:7] == '12':
        fdjandbsx = '单燃料 汽油 发动机排量大于1小于等于1.3'
        cartype = '2厢5门'
    elif sVIN[5:7] == '22':
        fdjandbsx = '单燃料 汽油 发动机排量大于1.3小于等于1.5'
        cartype = '2厢5门'
    elif sVIN[5:7] == '32':
        fdjandbsx = '单燃料 汽油 发动机排量大于1.5小于等于1.7'
        cartype = '2厢5门'
    elif sVIN[5:7] == '42':
        fdjandbsx = '单燃料 汽油 发动机排量大于1.7小于等于1.9'
        cartype = '2厢5门'
    elif sVIN[5:7] == '52':
        fdjandbsx = '单燃料 汽油 发动机排量大于1.9小于等于2.1'
        cartype = '2厢5门'
    elif sVIN[5:7] == '62':
        fdjandbsx = '单燃料 汽油 发动机排量大于2.1'
        cartype = '2厢5门'
    elif sVIN[5:7] == '04':
        fdjandbsx = '单燃料 汽油 发动机排量小于等于1'
        cartype = '3厢4门'
    elif sVIN[5:7] == '14':
        fdjandbsx = '单燃料 汽油 发动机排量大于1小于等于1.3'
        cartype = '3厢4门'
    elif sVIN[5:7] == '24':
        fdjandbsx = '单燃料 汽油 发动机排量大于1.3小于等于1.5'
        cartype = '3厢4门'
    elif sVIN[5:7] == '34':
        fdjandbsx = '单燃料 汽油 发动机排量大于1.5小于等于1.7'
        cartype = '3厢4门'
    elif sVIN[5:7] == '44':
        fdjandbsx = '单燃料 汽油 发动机排量大于1.7小于等于1.9'
        cartype = '3厢4门'
    elif sVIN[5:7] == '54':
        fdjandbsx = '单燃料 汽油 发动机排量大于1.9小于等于2.1'
        cartype = '3厢4门'
    elif sVIN[5:7] == '64':
        fdjandbsx = '单燃料 汽油 发动机排量大于2.1'
        cartype = '3厢4门'
    elif sVIN[5:7] == '07':
        fdjandbsx = '单燃料 汽油 发动机排量小于等于1'
        cartype = '长头厢式专用车'
    elif sVIN[5:7] == '17':
        fdjandbsx = '单燃料 汽油 发动机排量大于1小于等于1.3'
        cartype = '长头厢式专用车'
    elif sVIN[5:7] == '27':
        fdjandbsx = '单燃料 汽油 发动机排量大于1.3小于等于1.5'
        cartype = '长头厢式专用车'
    elif sVIN[5:7] == '37':
        fdjandbsx = '单燃料 汽油 发动机排量大于1.5小于等于1.7'
        cartype = '长头厢式专用车'
    elif sVIN[5:7] == '47':
        fdjandbsx = '单燃料 汽油 发动机排量大于1.7小于等于1.9'
        cartype = '长头厢式专用车'
    elif sVIN[5:7] == '57':
        fdjandbsx = '单燃料 汽油 发动机排量大于1.9小于等于2.1'
        cartype = '长头厢式专用车'
    elif sVIN[5:7] == '67':
        fdjandbsx = '单燃料 汽油 发动机排量大于2.1'
        cartype = '长头厢式专用车'
    elif sVIN[5:7] == '72':
        fdjandbsx = '单燃料 柴油 发动机排量小于等于1'
        cartype = '2厢5门'
    elif sVIN[5:7] == '82':
        fdjandbsx = '单燃料 柴油 发动机排量大于1小于等于1.3'
        cartype = '2厢5门'
    elif sVIN[5:7] == '92':
        fdjandbsx = '单燃料 柴油 发动机排量大于1.3'
        cartype = '2厢5门'
    elif sVIN[5:7] == '74':
        fdjandbsx = '单燃料 柴油 发动机排量小于等于1'
        cartype = '3厢4门'
    elif sVIN[5:7] == 'J2':
        fdjandbsx = '两用燃料 汽油/压缩天然气（CNG） 发动机排量大于等于1.3'
        cartype = '2厢5门'
    elif sVIN[5:7] == 'K2':
        fdjandbsx = '两用燃料 汽油/压缩天然气（CNG） 发动机排量大于1.3小于等于3.0'
        cartype = '2厢5门'
    elif sVIN[5:7] == 'J4':
        fdjandbsx = '两用燃料 汽油/压缩天然气（CNG） 发动机排量大于等于1.3'
        cartype = '3厢4门'
    elif sVIN[5:7] == 'K4':
        fdjandbsx = '两用燃料 汽油/压缩天然气（CNG） 发动机排量大于1.3小于等于3.0'
        cartype = '3厢4门'
    elif sVIN[5:7] == 'J7':
        fdjandbsx = '两用燃料 汽油/压缩天然气（CNG） 发动机排量大于等于1.3'
        cartype = '长头厢式专用车'
    elif sVIN[5:7] == 'K7':
        fdjandbsx = '两用燃料 汽油/压缩天然气（CNG） 发动机排量大于1.3小于等于3.0'
        cartype = '长头厢式专用车'
    elif sVIN[5:7] == 'R2':
        fdjandbsx = '双燃料 甲醇燃料 发动机排量大于等于1.3'
        cartype = '2厢5门'
    elif sVIN[5:7] == 'S2':
        fdjandbsx = '双燃料 甲醇燃料 发动机排量大于1.3小于等于3.0'
        cartype = '2厢5门'
    elif sVIN[5:7] == 'R4':
        fdjandbsx = '双燃料 甲醇燃料 发动机排量大于等于1.3'
        cartype = '3厢4门'
    elif sVIN[5:7] == 'S4':
        fdjandbsx = '双燃料 甲醇燃料 发动机排量大于1.3小于等于3.0'
        cartype = '3厢4门'
    elif sVIN[5:7] == 'R7':
        fdjandbsx = '双燃料 甲醇燃料 发动机排量大于等于1.3'
        cartype = '长头厢式专用车'
    elif sVIN[5:7] == 'S7':
        fdjandbsx = '双燃料 甲醇燃料 发动机排量大于1.3小于等于3.0'
        cartype = '长头厢式专用车'
    elif sVIN[5:7] == 'U2':
        fdjandbsx = '纯电动汽车 驱动电机峰值功率之和150'
        cartype = '2厢5门'
    elif sVIN[5:7] == 'P2':
        fdjandbsx = '纯电动汽车 驱动电机峰值功率之和200'
        cartype = '2厢5门'
    elif sVIN[5:7] == 'V2':
        fdjandbsx = '纯电动汽车 驱动电机峰值功率之和240'
        cartype = '2厢5门'
    elif sVIN[5:7] == 'W2':
        fdjandbsx = '纯电动汽车 驱动电机峰值功率之和350'
        cartype = '2厢5门'
    elif sVIN[5:7] == 'T2':
        fdjandbsx = '纯电动汽车 驱动电机峰值功率之和400'
        cartype = '2厢5门'
    elif sVIN[5:7] == 'X2':
        fdjandbsx = '纯电动汽车 驱动电机峰值功率之和450'
        cartype = '2厢5门'
    elif sVIN[5:7] == 'Y4':
        fdjandbsx = '纯电动汽车 驱动电机峰值功率之和120'
        cartype = '3厢4门'
    elif sVIN[5:7] == 'W5':
        fdjandbsx = '纯电动汽车 驱动电机峰值功率之和350'
        cartype = '3厢5门'
    elif sVIN[5:7] == 'X5':
        fdjandbsx = '纯电动汽车 驱动电机峰值功率之和450'
        cartype = '3厢5门'
    elif sVIN[5:7] == 'Z5':
        fdjandbsx = '纯电动汽车 驱动电机峰值功率之和550'
        cartype = '3厢5门'
    elif sVIN[5:7] == 'E2':
        fdjandbsx = '混合动力电动汽车 发动机排量1.477 驱动电机峰值功率之和50'
        cartype = '2厢5门'
    elif sVIN[5:7] == 'F2':
        fdjandbsx = '混合动力电动汽车 发动机排量1.477 驱动电机峰值功率之和60'
        cartype = '2厢5门'
    elif sVIN[5:7] == 'G2':
        fdjandbsx = '混合动力电动汽车 发动机排量1.477 驱动电机峰值功率之和120'
        cartype = '2厢5门'
    elif sVIN[5:7] == 'F4':
        fdjandbsx = '混合动力电动汽车 发动机排量1.477 驱动电机峰值功率之和60'
        cartype = '3厢4门'
    if sVIN[7] == 'S':
        fdjandbsx += ' 前驱动+手动变速器'
    elif sVIN[7] == 'Z':
        fdjandbsx += ' 前驱动+自动变速器'
    elif sVIN[7] == 'W':
        fdjandbsx += ' 前驱动+无变速器'
    elif sVIN[7] == 'A':
        fdjandbsx += ' 后驱动+手动变速器'
    elif sVIN[7] == 'B':
        fdjandbsx += ' 后驱动+自动变速器'
    elif sVIN[7] == 'N':
        fdjandbsx += ' 后驱动+无变速器'
    elif sVIN[7] == 'C':
        fdjandbsx += ' 四轮驱动+手动变速器'
    elif sVIN[7] == 'D':
        fdjandbsx += ' 四轮驱动+自动变速器'
    elif sVIN[7] == 'E':
        fdjandbsx += ' 四轮驱动+无变速器'
    return safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, cartype_q

def jl2(sVIN):
    cartype = '*'
    pl = '*'
    fdjandbsx = '*'
    carxing = '*'
    safe = '*'
    year = 0
    year = getYear(sVIN[9])
    company = '*'
    cartype_q = '*'
    zpgc = '*'
    typeFlag = -1
    if sVIN[0:3] == 'LB3':
        company = '浙江豪情汽车制造有限公司'
        if sVIN[10] == 'H':
            zpgc = '浙江豪情汽车制造有限公司'
        elif sVIN[10] == 'L':
            zpgc = '浙江豪情汽车制造有限公司第一分公司'
        elif sVIN[10] == 'X':
            zpgc = '浙江豪情汽车制造有限公司湘潭分公司'
        elif sVIN[10] == 'J':
            zpgc = '浙江豪情汽车制造有限公司济南分公司'
        elif sVIN[10] == 'C':
            zpgc = '浙江豪情汽车制造有限公司成都分公司'
        elif sVIN[10] == 'B':
            zpgc = '浙江豪情汽车制造有限公司宝鸡分公司'
        elif sVIN[10] == 'A':
            zpgc = '浙江豪情汽车制造有限公司山西分公司'
    elif (sVIN[0:3] == 'L6T') or (sVIN[0:3] == 'LJU'):
        company = '浙江吉利汽车有限公司'
        if sVIN[10] == 'W' or sVIN[10] == 'D':
            zpgc = '浙江吉利汽车有限公司宁波杭州湾工厂'
        elif sVIN[10] == 'U':
            zpgc = '浙江吉利汽车有限公司春晓工厂'
        elif sVIN[10] == 'L':
            zpgc = '浙江吉利汽车有限公司义乌分公司'
        elif sVIN[10] == 'L':
            zpgc = '浙江吉利汽车有限公司杭州分公司'
        elif sVIN[10] == 'L':
            zpgc = '浙江吉利汽车有限公司余姚工厂'
        elif sVIN[10] == 'L':
            zpgc = '浙江吉利汽车有限公司宁波杭州湾第二分公司'
        elif sVIN[10] == 'L':
            zpgc = '浙江吉利汽车有限公司梅山工厂'
        elif sVIN[10] == 'L':
            zpgc = '浙江吉利汽车有限公司成都分公司'
        elif sVIN[10] == 'L':
            zpgc = '浙江吉利汽车有限公司武汉分公司'
        elif sVIN[10] == 'L':
            zpgc = '浙江吉利汽车有限公司湖北分公司'
    elif sVIN[0:3] == 'LJ2':
        company = '山西新能源汽车工业有限公司'
        if sVIN[10] == 'A':
            zpgc = '山西新能源汽车工业有限公司乘用车生产线'
    elif sVIN[0:3] == 'L10':
        company = '成都高原汽车工业有限公司'
        if sVIN[10] == 'C':
            zpgc = '成都高原汽车工业有限公司'
    if sVIN[3:5] == 'E3':
        typeFlag = 1
        cartype_q = '帝豪 Emgrand'
    elif sVIN[3:5] == 'F7':
        cartype_q = '帝豪 GS Emgrand GS'
        typeFlag = 1
    elif sVIN[3:5] == 'F3':
        typeFlag = 1
        if sVIN[5] == '1':
            cartype_q = '全新帝豪 15L-5MT'
            cartype = '4门普通乘用车车身'
        elif sVIN[5] == '2':
            cartype_q = '全新帝豪 15L-CVT'
            cartype = '4门普通乘用车车身'
        else:
            cartype_q = '全新帝豪'
    elif sVIN[3:5] == 'F5':
        typeFlag = 1
        cartype_q = '帝豪 GL Emgrand GL'
    elif sVIN[3:5] == 'FC':
        typeFlag = 1
        cartype_q = '远景 EC7'
    elif sVIN[3:5] == 'X3':
        typeFlag = 1
        cartype_q = '远景 X3 Emgrand X3'
    elif sVIN[3:5] == 'X7':
        typeFlag = 1
        cartype_q = '远景 SUV Emgrand X7'
    elif sVIN[3:5] == 'F6':
        typeFlag = 1
        cartype_q = '缤瑞 BINRAY'
    elif sVIN[3:5] == 'SX':
        typeFlag = 1
        cartype_q = '缤越 Coolray'
    elif sVIN[3:5] == 'KC':
        typeFlag = 1
        cartype_q = '博瑞 Emgrand GT'
    elif sVIN[3:5] == 'NL':
        typeFlag = 1
        cartype_q = '博越 Emgrand X7 Sport'
    elif sVIN[3:5] == 'N3':
        typeFlag = 1
        cartype_q = '博越 PRO AZKARRA'
    elif sVIN[3:5] == 'S2':
        typeFlag = 1
        cartype_q = 'ICON'
    elif sVIN[3:5] == 'FY':
        typeFlag = 1
        cartype_q = '星越 XingYue'
    elif sVIN[3:5] == 'VF':
        typeFlag = 1
        cartype_q = '嘉际 JiaJi'
    elif sVIN[3:5] == 'CX':
        typeFlag = 2
        if sVIN[5] == '1':
            cartype_q = '领克01 Lynk&co 01 纯 Core'
            cartype = '4门旅行车车身'
        elif sVIN[5] == '2':
            cartype_q = '领克01 Lynk&co01 耀 Louder'
            cartype = '4门旅行车车身'
        elif sVIN[5] == '3':
            cartype_q = '领克01 Lynk&co01 劲 Sport'
            cartype = '4门旅行车车身'
        else:
            cartype_q = '领克'
    elif sVIN[3:5] == 'CC':
        typeFlag = 2
        cartype_q = '领克02 Lynk&co 02'
    elif sVIN[3:5] == 'CS':
        typeFlag = 2
        cartype_q = '领克03 Lynk&co 03'
    elif sVIN[3:5] == 'CY':
        typeFlag = 2
        cartype_q = '领克05 Lynk&co 05'
    elif sVIN[3:5] == 'BX':
        typeFlag = 2
        cartype_q = '领克06 Lynk&co 06'
    elif sVIN[3:5] == 'GA':
        typeFlag = 3
        cartype_q = '几何A Geometry A'
    elif sVIN[3:5] == 'GC':
        typeFlag = 3
        cartype_q = '几何C Geometry C'
    if sVIN[6] == 'A' or sVIN[6] == 'R':
        safe = '仅安全带'
    elif sVIN[6] == 'B' :
        safe = '安全带和驾驶员安全气囊'
    elif sVIN[6] == 'C':
        safe = '安全带和前排正面安全气囊'
    elif sVIN[6] == 'D' :
        safe = '安全带和前排正、侧安全气囊'
    elif sVIN[6] == 'E':
        safe = '安全带和前排正、侧面和前后排头部安全气囊'
    elif sVIN[6] == 'F' :
        safe = '安全带和前排正面、前后排侧面安全气囊'
    elif sVIN[6] == 'G':
        safe = '安全带和前排正面、前后排侧面和头部安全气囊'
    elif sVIN[6] == 'S' :
        safe = '出口海湾国家'
    elif sVIN[6] == '0':
        safe = '占位符'
    if typeFlag == 1:
        if sVIN[7] == '1':
            fdjandbsx = '汽油(Gas),GEELY 10TD(0.998L,100kw),6MT,FWD'
        elif sVIN[7] == '2':
            fdjandbsx = '汽油(Gas),GEELY 10TD(0.998L,100kw),6DCT,FWD'
        elif sVIN[7] == '3':
            fdjandbsx = '汽油(Gas),GEELY 1 4T(1.398L),6MT,FWD'
        elif sVIN[7] == '4':
            fdjandbsx = '汽油(Gas),GEELY 1 4T(1.398L,104kw),CVT,FWD'
        elif sVIN[7] == '5':
            fdjandbsx = '汽油(Gas),GEELY 1.5TD(1.477L,130kw) ,7DCT,FWD'
        elif sVIN[7] == '6':
            fdjandbsx = '汽油(Gas),GEELY1.5TDPHEV(1.477L,132+60kw), 7DCTH,FWD'
        elif sVIN[7] == '7':
            fdjandbsx = '汽油(Gas),GEELY 1.5L(1.498L,80kw),5MT,FWD'
        elif sVIN[7] == '8':
            fdjandbsx = '汽油(Gas),GEELY 1.SL(1.498L,80kw),CVT,FWD'
        elif sVIN[7] == '9':
            fdjandbsx = '汽油(Gas),GEELY1.8L(1.799L,96kw),5MT,FWD'
        elif sVIN[7] == 'A':
            fdjandbsx = '汽油(Gas),GEELY 1.8TD(1.799L,135kw),6AT,AWD'
        elif sVIN[7] == 'B':
            fdjandbsx = '汽油(Gas),GEELY 2.0L(1.997L,102kw),6AT,FWD'
    elif typeFlag == 2:
        if sVIN[7]=='1':
            fdjandbsx = '汽油(Gas),GEP3-1.5TD(1.477TD,115kw),6MT,FWD'
        elif sVIN[7] == '2':
            fdjandbsx = '汽油(Gas),GEP3-1.5TD(1.477TD,132kw),7DCT,FWD'
        elif sVIN[7] == '3':
            fdjandbsx = '汽油(Gas),HEV GEP3 Miller(1.477TD,143+50kw),7DCTH,FWD'
        elif sVIN[7] == '4':
            fdjandbsx = '汽油(Gas),HEV GEP3-1.5TD(1.477TD,132+60kw),7DCTH,FWD'
        elif sVIN[7] == '5':
            fdjandbsx = '汽油(Gas),PHEV GEP3-1.5TD(1.477TD,132+60kw),7DCTH,FWD'
        elif sVIN[7] == '6':
            fdjandbsx = '汽油(Gas),GEP3 MP+1.5TD(1.477TD,180kw),7DCT,FWD'
        elif sVIN[7] == '7':
            fdjandbsx = '汽油(Gas),PHEV GEP3 MP+(180+75kw,1.477TD),7DCTH,FWD'
        elif sVIN[7] == '8':
            fdjandbsx = '汽油(Gas),VEP4-2.0TD(1.969TD,140kw),6AT,FWD'
        elif sVIN[7] == '9':
            fdjandbsx = '汽油(Gas),VEP4-2.0TD(1.969TD,140kw),7DCT,AWD'
        elif sVIN[7] == 'A':
            fdjandbsx = '汽油(Gas),VEP4-2.0TD(1.969TD,187kw),8AT,FWD'
        elif sVIN[7] == 'B':
            fdjandbsx = '汽油(Gas),VEP4-2.0TD(1.969TD,187kw),8AT,AWD'
    if typeFlag == 3:
        if sVIN[7] == '1':
            fdjandbsx = 'EV,120kwFWD'
        elif sVIN[7] == '2':
            fdjandbsx = 'EV,130kwFWD'
        elif sVIN[7] == '3':
            fdjandbsx = 'EV,150kwFWD'
    return safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, cartype_q

def jkRC(sVIN):
    cartype = '*'
    pl = '*'
    fdjandbsx = '*'
    carxing = '*'
    safe = '*'
    year = 0
    year = getYear(sVIN[9])
    company = '*'
    cartype_q = '*'
    zpgc = '*'
    typeFlag = -1
    AX_flag = -1
    if sVIN[2] == '1':
        cartype_q = '轿车'
        typeFlag = 1
    elif sVIN[2] == '2':
        cartype_q = '多用途车'
        typeFlag = 2
    elif sVIN[2] == '3':
        cartype_q = '活顶帐篷车 conv.'
        typeFlag = 1
    elif sVIN[2] == '4' :
        if sVIN[0] == '1' or sVIN[0] == '4':
            cartype_q = '轿车'
            typeFlag = 1
        else:
            cartype_q = '多用途车/载货车cargo.'
            typeFlag = 2
    elif sVIN[2] == '6':
        cartype_q = '货车（卡车）Truck'
        typeFlag = 2
    elif sVIN[2] == '8':
        cartype_q = '多用途车'
        typeFlag = 2
    if sVIN[4] == 'U':
        if sVIN[3] == 'B':
            carxing = 'Altima'
            fdjandbsx = 'KA24DE 2.4L'
        elif sVIN[3] == 'C':
            carxing = 'Maxima'
            fdjandbsx = 'VQ30DE 3.0L'
        elif sVIN[3] == 'H':
            carxing = 'Maxima/Stanza'
            fdjandbsx = 'L24E 2.4L/VG30E 3.0L/CA20E'
        elif sVIN[3] == 'E':
            carxing = 'Maxima'
            fdjandbsx = 'VE30DE 3.0L'
        elif sVIN[3] == 'S':
            carxing = 'Maxima'
            fdjandbsx = 'LD28 2.8L柴油机'
        elif sVIN[3] == 'F':
            carxing = 'Stanza'
            fdjandbsx = 'KA24E'
        else:
            carxing =  'Altima/Maxima/Stanza'
    elif sVIN[4] == 'M':
        if sVIN[3] == 'H':
            carxing = 'Axxess/stanza wagon'
            AX_flag = 1
            fdjandbsx = 'KA24E 2.4L/CA20E'
        elif sVIN[3] == 'F':
            carxing = 'stanza wagon'
            fdjandbsx = 'KA24E'
        else:
            AX_flag = 1
            carxing = 'Axxess/stanza wagon'
    elif sVIN[4] == 'A' or sVIN[4] == 'J':
        carxing = 'Maxima'
        if sVIN[3] == 'C':
            fdjandbsx = 'VQ30DE 3.0L'
        elif sVIN[3] == 'H':
            fdjandbsx = 'L24E 2.4L/VG30E 3.0L'
        elif sVIN[3] == 'E':
            fdjandbsx = 'VE30DE 3.0L'
        elif sVIN[3] == 'S':
            fdjandbsx = 'LD28 2.8L柴油机'
    elif sVIN[4] == 'B':
        if sVIN[3] == 'E':
            carxing = 'NX Coupe/Sentra'
            fdjandbsx = 'GA16DE 1.6L'
        elif sVIN[3] == 'G':
            carxing = 'NX Coupe/Sentra'
            fdjandbsx = 'SR20DE 2.0L/GA16i 1.6L'
        elif sVIN[3] == 'A':
            carxing = '200SX/Sentra'
            fdjandbsx = 'GA16DE'
        elif sVIN[3] == 'B':
            carxing = '200SX/Sentra'
            fdjandbsx = 'SR20DE'
        elif sVIN[3] == 'P':
            carxing = '200SX/Sentra'
            fdjandbsx = 'E16i 1.6L/E16S 1.6L/E16 1.6L/Z22E 2.2L/CA20E 2.0L'
        elif sVIN[3] == 'S':
            carxing = 'Sentra'
            fdjandbsx = 'CD17 1.7L柴油机'
        elif sVIN[3] == 'H':
            carxing = 'Sentra'
            fdjandbsx = 'E15 1.5L'
        elif sVIN[3] == 'C':
            carxing = '200SX'
            fdjandbsx = 'CA18ET 1.8LTurbo(增压)'
        elif sVIN[3] == 'V':
            carxing = '200SX'
            fdjandbsx = 'VG30E 3.0L,V6'
        else:
            carxing = 'NX Coupe/Sentra/200SX'
    elif sVIN[4] == 'N':
        if sVIN[3] == 'P':
            carxing = 'Pulsar'
            fdjandbsx = 'E16i 1.6L'
        elif sVIN[3] == 'G':
            carxing = 'Pulsar'
            fdjandbsx = 'GA16i 1.6L'
        elif sVIN[3] == 'C':
            carxing = 'Pulsar'
            fdjandbsx = 'CA18DE 1.8L'
        elif sVIN[3] == 'E':
            carxing = 'Pulsar'
            fdjandbsx = 'CA16DE 1.6L'
        elif sVIN[3] == 'D':
            carxing = 'Quest'
            fdjandbsx = '5001~6000磅'
        else:
            carxing = 'Pulsar/Quest'
    elif sVIN[4] == 'S':
        if sVIN[3] == 'A':
            carxing = 'Sentra/200SX/240SX'
            fdjandbsx = 'GA16DE/KA24DE'
        elif sVIN[3] == 'B':
            carxing = 'Sentra/200SX'
            fdjandbsx = 'SR20DE'
        elif sVIN[3] == 'E':
            carxing = 'Sentra'
            fdjandbsx = 'GA16DE 1.6L'
        elif sVIN[3] == 'P':
            carxing = 'Sentra/200SX'
            fdjandbsx = 'E16i 1.6L/E16S 1.6L/E16 1.6L/Z22E 2.2L/CA20E 2.0L'
        elif sVIN[3] == 'S':
            carxing = 'Sentra'
            fdjandbsx = 'CD17 1.7L柴油机'
        elif sVIN[3] == 'H':
            carxing = 'Sentra/240SX'
            fdjandbsx = 'E15 1.5L/KA24E 2.4L/KA24DE 2.4L'
        elif sVIN[3] == 'G':
            carxing = 'Sentra'
            fdjandbsx = 'SR20DE 2.0L/GA16i 1.6L'
        elif sVIN[3] == 'C':
            carxing = '200SX'
            fdjandbsx = 'CA18ET 1.8LTurbo(增压)'
        elif sVIN[3] == 'V':
            carxing = '200SX'
            fdjandbsx = 'VG30E 3.0L,V6'
    elif sVIN[4] == 'T':
        carxing = 'Stanza'
        if sVIN[3] == 'F':
            fdjandbsx = 'KA24E'
        elif sVIN[3] == 'H':
            fdjandbsx = 'CA20E'
    elif sVIN[4] == 'Z':
        if sVIN[3] == 'C':
            carxing = '280ZX/300ZX'
            fdjandbsx = 'L28 2.8L/L2BET 2.8LTurbo/VG30ET 3.0L Turbo(增压)/vg30dett 3.0l TwinTurbo'
        elif sVIN == 'H':
            carxing = '300ZX'
            fdjandbsx = 'VG30E 3.0L'
        elif sVIN == 'R':
            carxing = '300ZX'
            fdjandbsx = 'VG30DE'
        else:
            carxing = '280ZX/300ZX'
    elif sVIN[4] == 'C' or sVIN[4] == 'D' or sVIN[4] == 'R':
        carxing = 'Truck货车/Van厢式车/pathfinder寻径者牌'
        if sVIN[3] == 'A':
            fdjandbsx = 'VG33E 3.3L'
        elif sVIN[3] == 'F':
            fdjandbsx = 'Z20 2.0L'
        elif sVIN[3] == 'H':
            fdjandbsx = 'VG30/VG30i/VG30E 3.0L'
        elif sVIN[3] == 'N':
            fdjandbsx = 'Z24/Z24i 2.4L'
        elif sVIN[3] == 'S':
            fdjandbsx = 'KA24E 2.4L/Z24i 2.4L'
        elif sVIN[3] == 'J':
            fdjandbsx = 'SD25,2.5L柴油机'
    if typeFlag == 1:
        if sVIN[6] == '1':
            cartype = '四门轿车 sedan'
        elif sVIN[6] == '2':
            cartype = '两门轿车 sedan'
        elif sVIN[6] == '3':
            cartype = '四门舱背式（Hatchback）'
        elif sVIN[6] == '4':
            cartype = '两门 coupe 跑车'
        elif sVIN[6] == '5':
            cartype = '五或七乘客汽车'
        elif sVIN[6] == '6':
            cartype = '两门舱背式汽车/2+2两门 coupe(300ZX)/直背式活动顶蓬式（200,240SX）汽车/coupe跑车（T-bar车顶盖）'
        elif sVIN[6] == '7':
            cartype = '活动顶蓬 convertible'
    elif typeFlag == 2:
        if sVIN[6] == '1':
            cartype = 'Quest 多用途车/短厢底盘车'
        elif sVIN[6] == '2':
            cartype = '长车厢底盘车/Quest载货车(cargo)'
        elif sVIN[6] == '4':
            cartype = '厢式车 pathfinder车'
        elif sVIN[6] == '5':
            cartype = '驾驶室和底盘'
        elif sVIN[6] == '6':
            cartype = 'Kingcab 车,两门旅行 pathfinder'
        elif sVIN[6] == '7':
            cartype = '厢式车,四门旅行车,pathfinder'
        elif sVIN[6] == '8':
            cartype = 'pathfinder'
    if typeFlag == 1:
        if AX_flag == 1:
            if sVIN[7] == 'J':
                safe = '两点式自动和手动式安全带(4WD)'
            elif sVIN[7] == 'P':
                safe = '两点式自动和手动式安全带(2WD)'
            elif sVIN[7] == 'S':
                safe = '三点式手动安全带(2WD)'
            elif sVIN[7] == 'Y':
                safe = '三点式手动安全带(4WD)'
        else:
            if sVIN[7] == 'A':
                safe = '三点式自动安全带'
            elif sVIN[7] == 'B':
                safe = '安全气囊系统'
            elif sVIN[7] == 'C':
                safe = '主动式座椅安全带/安全气囊系统（加拿大）'
            elif sVIN[7] == 'D':
                safe = '双安全气囊/三点式手动安全带'
            elif sVIN[7] == 'F':
                safe = '安全气囊系统（美国）'
            elif sVIN[7] == 'H':
                safe = '安全气囊系统'
            elif sVIN[7] == 'J':
                safe = '两点式自动安全带（4WD）'
            elif sVIN[7] == 'P':
                safe = '两点式自动安全带(2WD)'
            elif sVIN[7] == 'S':
                safe = '标准型'
    elif typeFlag == 2:
        if fdjandbsx == '*':
            if sVIN[7] == 'H':
                fdjandbsx = '重载型车（pickup）'
            elif sVIN[7] == 'S':
                fdjandbsx = '2WD两轮驱动/三点式手动（2WD）(pathfinder/pickup)'
            elif sVIN[7] == 'W':
                fdjandbsx = 'VG30E 3.0L(Quest)'
            elif sVIN[7] == 'Y':
                fdjandbsx = '三点式手动（4WD）(pathfinder/pickup)/4WD四轮驱动'
    return safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, cartype_q

def jkRC_WX(sVIN):
    cartype = '*'
    pl = '*'
    fdjandbsx = '*'
    carxing = '*'
    safe = '*'
    year = 0
    year = getYear(sVIN[9])
    company = '*'
    cartype_q = '*'
    zpgc = '*'
    typeFlag = -1
    if sVIN[2] == 'K':
        cartype_q = '轿车'
    elif sVIN[2] == 'R':
        cartype_q = 'MPV多用途车'
        typeFlag = 1
    elif sVIN[2] == 'X':
        cartype_q = '活顶敞篷汽车（Convertible）'
    if sVIN[3] == 'A':
        fdjandbsx = 'VG30DEV6发动机/VG33DEV6发动机'
    elif sVIN[3] == 'B':
        fdjandbsx = 'VH41DE V8 发动机'
    elif sVIN[3] == 'C':
        fdjandbsx = 'SR20DE 四缸 发动机/VQ30DE V6 发动机'
    elif sVIN[3] == 'H':
        fdjandbsx = 'VG30E V6 发动机'
    elif sVIN[3] == 'N':
        fdjandbsx = 'VH45DE V8 发动机'
    if sVIN[4] == 'A':
        carxing = 'Infinti(无限)130'
    elif sVIN[4] == 'F':
        carxing = 'Infinti(无限)M30'
    elif sVIN[4] == 'G':
        carxing = 'Infinti(无限)Q45'
    elif sVIN[4] == 'P':
        carxing = 'Infinti(无限)G20'
    elif sVIN[4] == 'R':
        carxing = 'Infinti(无限)QX4'
    elif sVIN[4] == 'Y':
        carxing = 'Infinti(无限)J30/Infinti(无限)Q45'
    if sVIN[6] == '1':
        cartype = '四门轿车（Sedan）'
    elif sVIN[6] == '4':
        cartype = '两门 Coupe'
    elif sVIN[6] == '5':
        cartype = '四门 Wagon(旅行车)(QX4)'
    elif sVIN[6] == '6':
        cartype = '两门 Convertible(活顶敞篷车)'
    elif sVIN[6] == '7':
        cartype = '四门 Wagon(QX4)(2000)'
    if typeFlag == 1:
        if sVIN[7] == 'Y':
            if fdjandbsx == '*':
                fdjandbsx = '4WD(四轮驱动)'
            else:
                fdjandbsx += '4WD(四轮驱动)'
    else:
        if sVIN[7] == 'A':
            safe = '驾驶员、乘客气囊和侧向安全气囊以及三点式安全带'
        elif sVIN[7] == 'C':
            safe = '安全气囊和三点式安全带'
        elif sVIN[7] == 'D':
            safe = '双气囊和三点式安全带'
        elif sVIN[7] == 'P':
            safe = '自动式座椅安全带'
    if sVIN[10] == 'M':
        zpgc = 'TochiGi 日本'
    elif sVIN[10] == 'T':
        zpgc = 'Oppama 日本'
    elif sVIN[10] == 'W':
        zpgc = 'Kyushi 日本'
    return safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, cartype_q
def jkBT(sVIN):
    cartype = '*'
    pl = '*'
    fdjandbsx = '*'
    carxing = '*'
    safe = '*'
    year = 0
    year = getYear(sVIN[9])
    company = '*'
    cartype_q = '*'
    zpgc = '*'
    typeFlag = -1
    civicFlag = '0'
    if sVIN[1] == 'H':
        company = '本田公司'
    if sVIN[0] == '1' or sVIN[0] == '4' or sVIN[0] == '2':
        if sVIN[0] == '2':
            if sVIN[1] == 'S':
                company = 'SIAPLANT,USA'
        if sVIN[2] == 'G':
            cartype_q = '本田轿车(美国和加拿大)'
        elif sVIN[2] == '1':
            cartype_q = '载货汽车'
        elif sVIN[2] == '2':
            cartype_q = '摩托车/货车'
        elif sVIN[2] == '3':
            cartype_q = '越野汽车'
        elif sVIN[2] == '4':
            cartype_q = '阿库拉轿车/载人小客车'
    elif sVIN[0] == 'J':
        if sVIN[2] == 'M':
            cartype_q = '本田轿车（日本）'
        elif sVIN[2] == '1':
            cartype_q = '载货汽车'
        elif sVIN[2] == '2':
            cartype_q = '摩托车/货车'
        elif sVIN[2] == '3':
            cartype_q = '越野汽车'
        elif sVIN[2] == '4':
            cartype_q = '阿库拉轿车/载人小客车'
    if sVIN[3:5] == 'AC':
        carxing = 'Accord'
        fdjandbsx = '1.6L'
        typeFlag = 1
    elif sVIN[3:5] == 'AD':
        carxing = 'Accord'
        fdjandbsx = '1.8L'
        typeFlag = 1
    elif sVIN[3:5] == 'BA':
        carxing = 'Accord'
        fdjandbsx = 'B'
        typeFlag = 1
    elif sVIN[3:5] == 'BZ':
        carxing = 'Accord'
        fdjandbsx = 'EK'
        typeFlag = 1
    elif sVIN[3:5] == 'SR':
        carxing = 'CIVIC 1500舱背式(Hatchback)'
        typeFlag = 2
    elif sVIN[3:5] == 'ST':
        carxing = 'CIVIC 1500普通轿车'
        typeFlag = 2
    elif sVIN[3:5] == 'VN':
        carxing = 'CIVIC 旅行厢式车'
        typeFlag = 2
    elif sVIN[3:5] == 'WD':
        carxing = 'CIVIC 1500型四门旅行车'
        typeFlag = 2
    elif sVIN[3:5] == 'AB':
        carxing = 'Prelude'
        typeFlag = 3
    elif sVIN[3:5] == 'BZ':
        carxing = 'Prelude si'
        typeFlag = 3
    if sVIN[3:6] == 'CA5':
        carxing = 'Accord 二门舱背式和四门轿车'
        typeFlag = 4
        fdjandbsx = '2.0L'
    elif sVIN[3:6] == 'CA6':
        carxing = 'Accord二门 coupe'
        typeFlag = 4
        fdjandbsx = '2.0L'
    elif sVIN[3:6] == 'CB7':
        carxing = 'Accord'
        typeFlag = 4
        fdjandbsx = '2.2L'
    elif sVIN[3:6] == 'CB9':
        carxing = 'Accord 旅行车'
        typeFlag = 4
        fdjandbsx = '2.2L'
    elif sVIN[3:6] == 'CD5':
        carxing = 'Accord 四门轿车'
        typeFlag = 4
        fdjandbsx = '2.2L'
    elif sVIN[3:6] == 'CD7':
        carxing = 'Accord 二门 coupe'
        typeFlag = 4
        fdjandbsx = '2.2L'
    elif sVIN[3:6] == 'CE1':
        carxing = 'Accord 旅行车'
        typeFlag = 4
        fdjandbsx = '2.2L'
    elif sVIN[3:6] == 'CE6':
        carxing = 'Accord 轿车(sedan)V6'
        typeFlag = 4
        fdjandbsx = '2.0L'
    elif sVIN[3:6] == 'EC1':
        carxing = 'CIVIC CRx'
        typeFlag = 5
        fdjandbsx = '1.5L'
    elif sVIN[3:6] == 'EC3':
        carxing = 'CIVIC 舱背式'
        typeFlag = 5
        fdjandbsx = '1.5L'
    elif sVIN[3:6] == 'EC5':
        carxing = 'CIVIC 旅行车'
        typeFlag = 5
        fdjandbsx = '1.5L'
    elif sVIN[3:6] == 'ED3':
        carxing = 'CIVIC 四门'
        civicFlag = '3'
        typeFlag = 5
        fdjandbsx = '1.5L'
    elif sVIN[3:6] == 'ED6':
        carxing = 'CIVIC 舱背式'
        typeFlag = 5
        fdjandbsx = '1.5L'
    elif sVIN[3:6] == 'ED8':
        carxing = 'CIVIC CRX'
        typeFlag = 5
        fdjandbsx = '1.5L'
    elif sVIN[3:6] == 'EE2':
        carxing = 'CIVIC 旅行车'
        typeFlag = 5
        fdjandbsx = '1.5L'
    elif sVIN[3:6] == 'EG1':
        carxing = 'CIVIC del sol'
        civicFlag = '4'
        typeFlag = 5
        fdjandbsx = '1.5L,102HP'
    elif sVIN[3:6] == 'EG2':
        carxing = 'CIVIC del sol'
        civicFlag = '4'
        typeFlag = 5
        fdjandbsx = '1.6L,160HP'
    elif sVIN[3:6] == 'EG8':
        carxing = 'CIVIC 四门'
        civicFlag = '3'
        typeFlag = 5
        fdjandbsx = '1.5L'
    elif sVIN[3:6] == 'EH3':
        carxing = 'CIVIC 二门'
        typeFlag = 5
        fdjandbsx = '1.6L'
    elif sVIN[3:6] == 'EH9':
        carxing = 'CIVIC 四门'
        civicFlag = '3'
        typeFlag = 5
        fdjandbsx = '1.6L'
    elif sVIN[3:6] == 'EJ2':
        carxing = 'CIVIC coupe'
        typeFlag = 5
        fdjandbsx = '1.5L'
    elif sVIN[3:6] == 'EC2':
        carxing = 'CIVIC 舱背式'
        typeFlag = 5
        fdjandbsx = '1.3L'
    elif sVIN[3:6] == 'EC4':
        carxing = 'CIVIC 轿车(sedan)'
        typeFlag = 5
        fdjandbsx = '1.5L'
    elif sVIN[3:6] == 'EC6':
        carxing = 'CIVIC 旅行车4WD'
        typeFlag = 5
        fdjandbsx = '1.5L'
    elif sVIN[3:6] == 'ED4':
        carxing = 'CIVIC 四门'
        civicFlag = '3'
        typeFlag = 5
        fdjandbsx = '1.6L'
    elif sVIN[3:6] == 'ED7':
        carxing = 'CIVIC 舱背式'
        typeFlag = 5
        fdjandbsx = '1.6L'
    elif sVIN[3:6] == 'ED9':
        carxing = 'CIVIC CRX'
        typeFlag = 5
        fdjandbsx = '1.6L'
    elif sVIN[3:6] == 'EE4':
        carxing = 'CIVIC 旅行车 4WD'
        typeFlag = 5
        fdjandbsx = '1.6L'
    elif sVIN[3:6] == 'EH2':
        carxing = 'CIVIC 二门'
        typeFlag = 5
        fdjandbsx = '1.5L'
    elif sVIN[3:6] == 'EH6':
        carxing = 'CIVIC  del sol'
        civicFlag = '4'
        typeFlag = 5
        fdjandbsx = '1.6L,125HP'
    elif sVIN[3:6] == 'EJ1':
        carxing = 'CIVIC coupe'
        typeFlag = 5
        fdjandbsx = '1.6L'
    elif sVIN[3:6] == 'EJ6':
        carxing = 'CIVIC coupe舱背式轿车'
        typeFlag = 5
        fdjandbsx = '1.6L'
    elif sVIN[3:6] == 'EJ7':
        carxing = 'CIVIC coupe'
        typeFlag = 5
        fdjandbsx = '1.6L,VTEC-2'
    elif sVIN[3:6] == 'EJ8':
        carxing = 'CIVIC coupe轿车'
        typeFlag = 5
        fdjandbsx = '1.6L,VETC'
    elif sVIN[3:6] == 'EY1':
        carxing = 'CIVIC 旅行厢式车(wagovan)'
        typeFlag = 5
        fdjandbsx = '1.5L'
    elif sVIN[3:6] == 'EY3':
        carxing = 'CIVIC 旅行厢式车'
        typeFlag = 5
        fdjandbsx = '1.5L'
    elif sVIN[3:6] == 'BA4':
        carxing = 'Prelude'
        typeFlag = 6
        fdjandbsx = '2.0L&2.05L'
    elif sVIN[3:6] == 'BA8':
        carxing = 'Prelude'
        typeFlag = 6
        fdjandbsx = '2.2L'
    elif sVIN[3:6] == 'BB1':
        carxing = 'Prelude'
        typeFlag = 6
        fdjandbsx = '2.2L VTEC'
    elif sVIN[3:6] == 'BB2':
        carxing = 'Prelude'
        typeFlag = 6
        fdjandbsx = '2.3L'
    elif sVIN[3:6] == 'BB6':
        carxing = 'Prelude'
        typeFlag = 6
        fdjandbsx = '2.2L'
    if typeFlag == 1 or typeFlag == 2 or typeFlag == 3:
        if sVIN[5] == '3':
            if fdjandbsx == '*':
                fdjandbsx = '自动式'
            else:
                fdjandbsx += ' 自动式'
        elif sVIN[5] == '4':
            if fdjandbsx == '*':
                fdjandbsx = '四速手动式'
            else:
                fdjandbsx += ' 四速手动式'
        elif sVIN[5] == '5':
            if fdjandbsx == '*':
                fdjandbsx = '五速手动式'
            else:
                fdjandbsx += ' 五速手动式'
        elif sVIN[5] == '6':
            if fdjandbsx == '*':
                fdjandbsx = '五速手动式加有超低速挡'
            else:
                fdjandbsx += ' 五速手动式加有超低速挡'
        elif sVIN[5] == '7':
            if fdjandbsx == '*':
                fdjandbsx = '自动式'
            else:
                fdjandbsx += ' 自动式'
    if sVIN[6] == '1':
        cartype = '二门敞篷活顶/二门 coupe'
        civicFlag = '1'
        if fdjandbsx == '*':
            fdjandbsx = '五速手动式'
        else:
            fdjandbsx += ' 五速手动式'
    elif sVIN[6] == '2':
        cartype = '二门 coupe/二门敞篷'
        civicFlag = '1'
        if fdjandbsx == '*':
            fdjandbsx = '五速手动式/四速自动式/CVT(无级变速器)'
        else:
            fdjandbsx += ' 五速手动式/四速自动式/CVT(无级变速器)'
    elif sVIN[6] == '3':
        cartype = '二门舱背式/二门 coupe'
        civicFlag = '12'
        if fdjandbsx == '*':
            fdjandbsx = '手动式'
        else:
            fdjandbsx += ' 手动式'
    elif sVIN[6] == '4':
        cartype = '四门轿车/二门 coupe/二门舱背式'
        civicFlag = '123'
        if fdjandbsx == '*':
            fdjandbsx = '四速自动式'
        else:
            fdjandbsx += ' 四速自动式'
    elif sVIN[6] == '5':
        cartype = 'civic旅行车和旅行厢式车/四门轿车'
        civicFlag = '3'
        if fdjandbsx == '*':
            fdjandbsx = '五速手动式'
        else:
            fdjandbsx += ' 五速手动式'
    elif sVIN[6] == '6':
        cartype = '四门轿车'
        civicFlag = '3'
        if fdjandbsx == '*':
            fdjandbsx = '四速自动式'
        else:
            fdjandbsx += ' 四速自动式'
    elif sVIN[6] == '7':
        cartype = '五门轿车/四门旅行车'
        if fdjandbsx == '*':
            fdjandbsx = '五速手动式'
        else:
            fdjandbsx += ' 五速手动式'
    elif sVIN[6] == '8':
        cartype = '五门轿车(Sedan)/四门旅行车'
        if fdjandbsx == '*':
            fdjandbsx = '四速自动式'
        else:
            fdjandbsx += ' 四速自动式'
    if typeFlag == 1 or typeFlag == 4:
        if sVIN[0] == '1' or sVIN[0] == '4':
            if sVIN[7] == '0':
                carxing += ' SE(special Edition)特殊款式'
            elif sVIN[7] == '1':
                carxing += ' DX带ABS,Coupe和Sedan'
            elif sVIN[7] == '2':
                carxing += ' DX不带ABS,Coupe和Sedan/DX舱背式和Sedan/S,std舱背式和sedan/LX不带ABS旅行车'
            elif sVIN[7] == '3':
                carxing += ' LX舱背式和Sedan/LX带ABS旅行车/LX不带ABS,Coupe和Sedan/LX不带ABS-V6'
            elif sVIN[7] == '4':
                carxing += ' DX coupe&sedan/LX带ABS Coupe&sedan/LX带ABS-V6/LXi舱背式和sedan'
            elif sVIN[7] == '5':
                carxing += ' LX/Excoupe&sedan/EX-V6/SEi舱背式和sedan'
            elif sVIN[7] == '6':
                carxing += ' EX/DX被动安全带,舱背式和sedan/EX(皮革)/EXL-V6(皮革)'
            elif sVIN[7] == '7':
                carxing += ' EX/SE Coupe/EXL-V6(皮革)'
            elif sVIN[7] == '8':
                carxing += ' DXA(25th Anniversary Edition)/LX被动安全带，舱背式和Sedan'
            elif sVIN[7] == '9':
                carxing += ' DXSV(Special Value)/EX旅行车/LXA Coupe和Sedan 10th Anniversary Edition'
        elif sVIN[0] == '2':
            if sVIN[7] == '0':
                carxing += ' SE'
            elif sVIN[7] == '1':
                carxing += ' LX Sedan'
            elif sVIN[7] == '2':
                carxing += ' EX旅行车/S/LX带ABS Sedan/EX sedan/S,Limited,EX'
            elif sVIN[7] == '3':
                carxing += ' EX带ABS旅行车/EX Coupe&sedan/LX/LX Coupe/LX,EX'
            elif sVIN[7] == '4':
                carxing += ' EX带ABS Sedan/EXi/LX coupe&sedan/LX带ABS'
            elif sVIN[7] == '5':
                carxing += ' EX sedan和旅行车/EX-R旅行车/EXR sedan不带皮革座椅/SEi'
            elif sVIN[7] == '6':
                carxing += ' EX-R/EX-R带皮革座椅'
            elif sVIN[7] == '7':
                carxing += ' EX-R带ABS/S,Limited,EX'
            elif sVIN[7] == '8':
                carxing += ' SE'
    elif typeFlag == 2 or typeFlag == 5:
        if civicFlag == '1':
            if sVIN[0] == '1' or sVIN[0] == '4':
                if sVIN[7] == '2':
                    carxing += ' DX.HX'
                elif sVIN[7] == '3':
                    carxing += ' DX带ABS,HX带ABS'
                elif sVIN[7] == '4':
                    carxing += ' DX带空调，HX带空调'
                elif sVIN[7] == '5':
                    carxing += ' EX带ABS/HX带ABS和空调'
            elif sVIN[0] == '2':
                if sVIN[7] == '2':
                    carxing += ' DX Si'
                elif sVIN[7] == '3':
                    carxing += ' Si带有ABS'
                elif sVIN[7] == '4':
                    carxing += ' DX带ABS'
                elif sVIN[7] == '5':
                    carxing += ' EX带ABS'
                elif sVIN[7] == '6':
                    carxing += ' DX带ABS和空调'
                elif sVIN[7] == '7':
                    carxing += ' Si带ABS和空调'
        elif civicFlag == '2':
            if sVIN[0] == '1' or sVIN[0] == '4':
                if sVIN[7] == '2':
                    carxing += ' CX'
                elif sVIN[7] == '3':
                    carxing += ' CX带空调'
                elif sVIN[7] == '4':
                    carxing += ' DX'
                elif sVIN[7] == '5':
                    carxing += ' DX带空调'
                elif sVIN[7] == '6':
                    carxing += ' DX带ABS'
                elif sVIN[7] == '7':
                    carxing += ' DX带空调和ABS'
            elif sVIN[0] == '2':
                if sVIN[7] == '2':
                    carxing += ' CX'
                elif sVIN[7] == '3':
                    carxing += ' CX-G'
        elif civicFlag == '3':
            if sVIN[0] == '1' or sVIN[0] == '4':
                if sVIN[7] == '0':
                    carxing += ' LX'
                elif sVIN[7] == '2':
                    carxing += ' DX'
                elif sVIN[7] == '3':
                    carxing += ' DX带空调'
                elif sVIN[7] == '4':
                    carxing += ' DX带ABS EX'
                elif sVIN[7] == '5':
                    carxing += ' EX带空调和ABS'
                elif sVIN[7] == '6':
                    carxing += ' LX'
                elif sVIN[7] == '7':
                    carxing += ' LX带空调'
                elif sVIN[7] == '8':
                    carxing += ' LX带ABS'
                elif sVIN[7] == '9':
                    carxing += ' LX带空调和ABS'
            elif sVIN[0] == '2':
                if sVIN[7] == '0':
                    carxing += ' EX'
                elif sVIN[7] == '3':
                    carxing += ' LX'
                elif sVIN[7] == '4':
                    carxing += ' LX带ABS'
                elif sVIN[7] == '5':
                    carxing += ' LX带ABS和空调'
                elif sVIN[7] == '6':
                    carxing += ' EX'
                elif sVIN[7] == '7':
                    carxing += ' EX带ABS'
                elif sVIN[7] == '8':
                    carxing += ' EX带ABS和空调'
        elif civicFlag == '4':
            if sVIN[7] == '4':
                carxing += ' S'
            elif sVIN[7] == '6':
                carxing += ' Si'
            elif sVIN[7] == '7':
                carxing += ' Si带ABS,VTEC'
        elif civicFlag == '12':
            if sVIN[0] == '1' or sVIN[0] == '4':
                if sVIN[7] == '2':
                    carxing += ' DX.HX/CX'
                elif sVIN[7] == '3':
                    carxing += ' DX带ABS,HX带ABS/CX带空调'
                elif sVIN[7] == '4':
                    carxing += ' DX带空调，HX带空调/DX'
                elif sVIN[7] == '5':
                    carxing += ' EX带ABS/HX带ABS和空调/DX带空调'
                elif sVIN[7] == '6':
                    carxing += ' DX带ABS'
                elif sVIN[7] == '7':
                    carxing += ' DX带空调和ABS'
            elif sVIN[0] == '2':
                if sVIN[7] == '2':
                    carxing += ' DX Si/CX'
                elif sVIN[7] == '3':
                    carxing += ' Si带有ABS/CX-G'
                elif sVIN[7] == '4':
                    carxing += ' DX带ABS'
                elif sVIN[7] == '5':
                    carxing += ' EX带ABS'
                elif sVIN[7] == '6':
                    carxing += ' DX带ABS和空调'
                elif sVIN[7] == '7':
                    carxing += ' Si带ABS和空调'
        elif civicFlag == '123':
            if sVIN[0] == '1' or sVIN[0] == '4':
                if sVIN[7] == '0':
                    carxing += ' LX'
                elif sVIN[7] == '2':
                    carxing += ' DX.HX/CX/DX'
                elif sVIN[7] == '3':
                    carxing += ' DX带ABS,HX带ABS/CX带空调/DX带空调'
                elif sVIN[7] == '4':
                    carxing += ' DX带空调，HX带空调/DX/DX带ABS EX'
                elif sVIN[7] == '5':
                    carxing += ' EX带ABS/HX带ABS和空调/DX带空调/DX带空调和ABS'
                elif sVIN[7] == '6':
                    carxing += ' DX带ABS/LX'
                elif sVIN[7] == '7':
                    carxing += ' DX带空调和ABS/LX带空调'
                elif sVIN[7] == '8':
                    carxing += ' LX带ABS'
                elif sVIN[7] == '9':
                    carxing += ' LX带空调和ABS'
            elif sVIN[0] == '2':
                if sVIN[7] == '0':
                    carxing += ' EX'
                elif sVIN[7] == '2':
                    carxing += ' DX Si/CX'
                elif sVIN[7] == '3':
                    carxing += ' Si带有ABS/CX-G/LX'
                elif sVIN[7] == '4':
                    carxing += ' DX带ABS/LX带ABS'
                elif sVIN[7] == '5':
                    carxing += ' EX带ABS/LX带ABS和空调'
                elif sVIN[7] == '6':
                    carxing += ' DX带ABS和空调/EX'
                elif sVIN[7] == '7':
                    carxing += ' Si带ABS和空调/EX带ABS'
                elif sVIN[7] == '8':
                    carxing += ' EX带ABS和空调'
    elif typeFlag == 3 or typeFlag == 6:
        if sVIN[7] == '1':
            carxing += ' 2.0S'
        if sVIN[7] == '2':
            carxing += ' DX型/1800DX/2.0S/2.0Si'
        elif sVIN[7] == '3':
            carxing += ' Si型/2.05Si/2.0Si'
        elif sVIN[7] == '4':
            carxing += ' 2000Si/2.0Si 4WS选装/2.05Si 4WS选装/基本型'
            safe = '2.2S带座椅安全带和气囊'
        elif sVIN[7] == '5':
            carxing += ' SH型'
            safe = '2.3Si/SR带座椅安全带和气囊'
        elif sVIN[7] == '6':
            safe = '2.3Si/SR4WS有座椅安全带和双气囊'
        elif sVIN[7] == '7':
            carxing += ' Si-VT,SR-V有座椅安全带和双气囊/2.25R,SiVTEC有座椅安全带和双气囊'
    if sVIN[10] == 'A':
        zpgc = 'Marysville ohio 美国'
    elif sVIN[10] == 'C':
        zpgc = 'Sayama 日本'
    elif sVIN[10] == 'D':
        zpgc = 'Saitama 日本'
    elif sVIN[10] == 'H':
        zpgc = 'Ontario 加拿大/Alliston 加拿大'
    elif sVIN[10] == 'L':
        zpgc = 'East Liberty ohio 美国'
    elif sVIN[10] == 'S':
        zpgc = 'Suzuki 日本铃木'
    elif sVIN[10] == 'T':
        zpgc = 'Tochigi 日本'
    elif sVIN[10] == '4':
        zpgc = 'SIA 美国'

    return safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, cartype_q

def jkBT_akl(sVIN):
    cartype = '*'
    pl = '*'
    fdjandbsx = '*'
    carxing = '*'
    safe = '*'
    year = 0
    year = getYear(sVIN[9])
    company = '*'
    cartype_q = '*'
    zpgc = '*'
    typeFlag = -1
    if sVIN[1] == 'H':
        company = '本田公司'
    elif sVIN[1] == '9':
        company = 'Acura 阿库拉'
    if sVIN[2] == 'H' or sVIN[2] == 'M' or sVIN[2] == 'U' or sVIN[2] == '4':
        cartype_q = 'Acura阿库拉轿车'
    if sVIN[3:6] == 'CC2':
        carxing = 'Vigor伟高轿车'
        typeFlag = 4
    elif sVIN[3:6] == 'DH1':
        carxing = 'Integra形格轿车四门'
        typeFlag = 1
        fdjandbsx = '1.6L 四缸'
    elif sVIN[3:6] == 'DA3':
        carxing = 'Integra二门轿车'
        typeFlag = 1
        fdjandbsx = '1.6L 四缸'
    elif sVIN[3:6] == 'DA9':
        carxing = 'Integra二门轿车'
        typeFlag = 1
        fdjandbsx = '1.8L 四缸'
    elif sVIN[3:6] == 'DB1':
        carxing = 'Integra四门轿车'
        typeFlag = 1
        fdjandbsx = '1.6L 四缸'
    elif sVIN[3:6] == 'DB2':
        carxing = 'Integra二门轿车'
        typeFlag = 1
        fdjandbsx = '1.7L 四缸'
    elif sVIN[3:6] == 'DB7':
        carxing = 'Integra四门'
        typeFlag = 1
        fdjandbsx = '1.8L 四缸 DOHC'
    elif sVIN[3:6] == 'DB8':
        carxing = 'Integra四门'
        typeFlag = 1
        fdjandbsx = '1.8L 四缸 DOHC-VTEC'
    elif sVIN[3:6] == 'DC2':
        carxing = 'Integra二门'
        typeFlag = 1
        fdjandbsx = '1.8L 四缸 DOHC'
    elif sVIN[3:6] == 'DC4':
        carxing = 'Integra二门'
        typeFlag = 1
        fdjandbsx = '1.8L 四缸 DOHC-VTEC'
    elif sVIN[3:6] == 'KA2':
        carxing = 'Legend里程四门轿车'
        typeFlag = 2
        fdjandbsx = '2.5L V6型发动机'
    elif sVIN[3:6] == 'KA3':
        carxing = 'Legend里程二门Coupe'
        typeFlag = 2
        fdjandbsx = '2.7L V6型发动机'
    elif sVIN[3:6] == 'KA4':
        carxing = 'Legend里程碑轿车'
        typeFlag = 2
        fdjandbsx = '2.7L V6型发动机'
    elif sVIN[3:6] == 'KA7' or sVIN[3:6] == 'KA8':
        carxing = 'Legend里程四门轿车'
        typeFlag = 2
        fdjandbsx = '3.2L V6型发动机'
    elif sVIN[3:6] == 'KA9':
        carxing = '3.5RL四门轿车'
        typeFlag = 8
        fdjandbsx = '3.5L V6型发动机'
    elif sVIN[3:6] == 'MB4':
        carxing = '1.6EL(经济型)四门轿车'
        typeFlag = 6
        fdjandbsx = '1.6L 四缸发动机'
    elif sVIN[3:6] == 'NA1':
        carxing = 'NSX(全球型)二门轿车'
        typeFlag = 3
        fdjandbsx = '3.0L V6型发动机'
    elif sVIN[3:6] == 'NA2':
        carxing = 'NSX-T二门轿车'
        typeFlag = 3
        fdjandbsx = '3.2L V6型发动机'
    elif sVIN[3:6] == 'UA2':
        carxing = '2.5TL四门轿车'
        typeFlag = 9
        fdjandbsx = '2.5L五缸发动机'
    elif sVIN[3:6] == 'UA3' or sVIN[3:6] == 'UV5':
        carxing = '3.2TL四门轿车'
        typeFlag = 9
        fdjandbsx = '3.2L V6型发动机'
    elif sVIN[3:6] == 'YA1':
        carxing = '2.2CL二门'
        typeFlag = 7
        fdjandbsx = '2.2L四缸发动机'
    elif sVIN[3:6] == 'YA2':
        carxing = '3.0CL二门'
        typeFlag = 7
        fdjandbsx = '3.0L V6型发动机'
    elif sVIN[3:6] == 'YA3':
        carxing = '2.3CL二门'
        typeFlag = 7
        fdjandbsx = '2.3L四缸发动机'
    if sVIN[6] == '1':
        cartype = '二门 Coupe(开顶敞篷)/二门'
        if fdjandbsx == '*':
            fdjandbsx = '五速手动变速器/四速手动/五速手动/六速手动变速器'
        else:
            fdjandbsx += '五速手动变速器/四速手动/五速手动/六速手动变速器'
    elif sVIN[6] == '2':
        cartype = '二门 Coupe/二门 Coupe(开顶敞篷)'
        if fdjandbsx == '*':
            fdjandbsx = '四速自动变速器'
        else:
            fdjandbsx += '四速自动变速器'
    elif sVIN[6] == '3':
        cartype = '二门后背舱门式车身'
        if fdjandbsx == '*':
            fdjandbsx = '五速手动变速器'
        else:
            fdjandbsx += '五速手动变速器'
    elif sVIN[6] == '4':
        cartype = '二门后背舱门式车身'
        if fdjandbsx == '*':
            fdjandbsx = '四速自动变速器'
        else:
            fdjandbsx += '四速自动变速器'
    elif sVIN[6] == '5':
        cartype = '四门轿车'
        if fdjandbsx == '*':
            fdjandbsx = '五速手动变速器'
        else:
            fdjandbsx += '五速手动变速器'
    elif sVIN[6] == '6':
        cartype = '四门轿车'
        if fdjandbsx == '*':
            fdjandbsx = '四速自动变速器'
        else:
            fdjandbsx += '四速自动变速器'
    elif sVIN[6] == '7':
        cartype = '四门后背舱门式'
        if fdjandbsx == '*':
            fdjandbsx = '五速手动变速器'
        else:
            fdjandbsx += '五速手动变速器'
    elif sVIN[6] == '8':
        cartype = '四门后背舱门式'
        if fdjandbsx == '*':
            fdjandbsx = '四速自动变速器'
        else:
            fdjandbsx += '四速自动变速器'
    if typeFlag == 1:
        if sVIN[7] == '1':
            safe = 'R型(2000)'
        elif sVIN[7] == '3':
            safe = 'RS.RSI.座椅安全带，安全气囊/RS特种型(2000)'
        elif sVIN[7] == '4':
            safe = 'RS座椅安全带/RS安全气囊'
        elif sVIN[7] == '5':
            safe = 'LS座椅安全带/LS安全带安全气囊'
        elif sVIN[7] == '6':
            safe = 'LS-SPL座椅安全带,安全气囊和皮革座椅/GS座椅安全带'
        elif sVIN[7] == '7':
            safe = 'GS皮革座椅，GSL皮革座椅'
        elif sVIN[7] == '8':
            safe = 'GS·R座椅安全带/GS·R座椅安全带，安全气囊/GS·R皮革座椅'
        elif sVIN[7] == '9':
            safe = 'LS·special(lssp)特殊型/GS·RL座椅安全带和安全气囊以及皮革座椅/GSL'
    elif typeFlag == 2:
        if sVIN[7] == '4':
            safe = '基本型，座椅安全带'
        elif sVIN[7] == '5':
            safe = 'L座椅安全带/L(Moquette)座椅安全带和安全气囊'
        elif sVIN[7] == '6':
            safe = 'LS型座椅安全带和安全气囊/L型座椅安全带和安全气囊'
        elif sVIN[7] == '7':
            safe = 'LS型座椅安全带和安全气囊'
        elif sVIN[7] == '8':
            safe = 'GS型座椅安全带和安全气囊'
        elif sVIN[7] == '5':
            safe = 'SE型座椅安全带和安全气囊'
    elif typeFlag == 3:
        if sVIN[7] == '2':
            safe = '两门 Coupe SRS'
        elif sVIN[7] == '3':
            safe = '两门 Coupe SRS(带有安全防护装置)/EPS(电动助力转向装置)'
        elif sVIN[7] == '5':
            safe = '两门 Coupe 带安全气囊'
        elif sVIN[7] == '6':
            safe = '两门 Coupe EPS(电动助力转向装置)和安全气囊/两门开顶敞篷，SRS防护装置，EPS转向装置和安全气囊'
        elif sVIN[7] == '8':
            safe = '两门开顶敞篷，EPS转向装置和安全气囊'
    elif typeFlag == 4:
        if sVIN[7] == '4':
            safe = 'LS安全带和安全气囊'
        elif sVIN[7] == '5' or sVIN[7] == '6':
            safe = 'GS安全带、安全气囊和皮革座椅'
    elif typeFlag == 5:
        if sVIN[7] == '3':
            safe = 'RS座椅安全带/基本型，不带天窗/基本型带有安全气囊'
        elif sVIN[7] == '4':
            safe = '基本型带有天窗，座椅安全带/LX-RSS,座椅安全带'
        elif sVIN[7] == '5' :
            safe = 'L型座椅安全带/L型座椅安全带，安全气囊/L(Moquette)座椅安全带和安全气囊/LS座椅安全带/LS座椅安全带和安全气囊/L(Moquette)座椅安全带和安全气囊'
    elif typeFlag == 6:
        if sVIN[7] == '4':
            if carxing == '*':
                carxing = ' RS不带ABS'
            else:
                carxing += ' RS不带ABS'
        elif sVIN[7] == '5':
            if carxing == '*':
                carxing = ' RS带有ABS'
            else:
                carxing += ' RS带有ABS'
        elif sVIN[7] == '6':
            if carxing == '*':
                carxing = ' TS'
            else:
                carxing += ' TS'
        elif sVIN[7] == '7':
            if carxing == '*':
                carxing = ' XS'
            else:
                carxing += ' XS'
    elif typeFlag == 7:
        if sVIN[7] == '4':
            if carxing == '*':
                carxing = ' 基本型装备'
            else:
                carxing += ' 基本型装备'
        elif sVIN[7] == '5':
            if carxing == '*':
                carxing = ' 高级型装备'
            else:
                carxing += ' 高级型装备'
    elif typeFlag == 8:
        if sVIN[7] == '4':
            if carxing == '*':
                carxing = ' 基本型装备/带有皮革座椅'
            else:
                carxing += ' 基本型装备/带有皮革座椅'
        elif sVIN[7] == '5':
            if carxing == '*':
                carxing = ' 高级型装备/不带导航系统'
            else:
                carxing += ' 高级型装备/不带导航系统'
        elif sVIN[7] == '6':
            if carxing == '*':
                carxing = ' 带有导航装备和高级型装备'
            else:
                carxing += ' 带有导航装备和高级型装备'
        elif sVIN[7] == '7':
            if carxing == '*':
                carxing = ' 带有导航系统'
            else:
                carxing += ' 带有导航系统'
    elif typeFlag == 9:
        if sVIN[7] == '4':
            if carxing == '*':
                carxing = ' 不带高级装备/不带导航系统'
            else:
                carxing += ' 不带高级装备/不带导航系统'
        elif sVIN[7] == '5':
            if carxing == '*':
                carxing = ' 带有高级装备配置/带有导航系统'
            else:
                carxing += ' 带有高级装备配置/带有导航系统'
        elif sVIN[7] == '6':
            if carxing == '*':
                carxing = ' 带不导航系统'
            else:
                carxing += ' 带不导航系统'
        elif sVIN[7] == '7':
            if carxing == '*':
                carxing = ' 带有导航系统'
            else:
                carxing += ' 带有导航系统'
    if sVIN[10] == 'A':
        zpgc = 'Marysville(美国俄亥俄州)'
    elif sVIN[10] == 'C':
        zpgc = 'Sayama 日本'
    elif sVIN[10] == 'H':
        zpgc = 'Ontario 加拿大'
    elif sVIN[10] == 'L':
        zpgc = 'East,Liberty(美国俄亥俄州)'
    elif sVIN[10] == 'S':
        zpgc = 'Suzuki 日本铃木'
    elif sVIN[10] == 'T':
        zpgc = 'Tochigi 日本'
    return safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, cartype_q

def jkMZD(sVIN):
    cartype = '*'
    pl = '*'
    fdjandbsx = '*'
    carxing = '*'
    safe = '*'
    year = 0
    year = getYear(sVIN[9])
    company = '*'
    cartype_q = '*'
    zpgc = '*'
    typeFlag = -1
    if sVIN[1] == 'F':
        company = '福特汽车公司(美国)'
    elif sVIN[1] == 'M':
        company = '马自达汽车公司(日本)'
    elif sVIN[1] == 'Y':
        company = '美国马自达汽车公司'
    if sVIN[2] == 'V' or sVIN[2] == '1':
        cartype_q = '载人小客车'
    elif sVIN[2] == '2':
        cartype_q = '载货汽车/厢式车'
    elif sVIN[2] == '3':
        cartype_q = 'MPV(多用途汽车)/载货汽车(Truck)/旅行车(Wagon)'
    elif sVIN[2] == '4':
        cartype_q = '载货汽车(Truck)'
    if sVIN[2] == '3' or sVIN == '4':
        if sVIN[3] == 'C':
            cartype_q += ' 4001~5000磅'
        elif sVIN[3] == 'D':
            cartype_q += ' 5001~6000磅'
        elif sVIN[3] == 'Y':
            cartype_q += ' 4001~5000磅(2000)'
        elif sVIN[3] == 'Z':
            cartype_q += ' 5001~6000磅(2000)'
        if sVIN[4:7] == 'R12':
            cartype = '4*2规定标准驾驶室'
        elif sVIN[4:7] == 'R13':
            cartype = '4*4规定标准驾驶室'
        elif sVIN[4:7] == 'R16':
            cartype = '4*2加长驾驶室'
        elif sVIN[4:7] == 'R17':
            cartype = '4*4加长驾驶室'
        if sVIN[7] == 'A':
            fdjandbsx = '2.3L四缸发动机'
        elif sVIN[7] == 'C':
            fdjandbsx = '2.0L四缸发动机/2.5L四缸发动机'
        elif sVIN[7] == 'D':
            fdjandbsx = '2.5L V6型发动机'
        elif sVIN[7] == 'U':
            fdjandbsx = '3.0L V6型发动机'
        elif sVIN[7] == 'V':
            fdjandbsx = '3.0L V6型发动机'
        elif sVIN[7] == 'X':
            fdjandbsx = '4.0L V6型发动机'
    if sVIN[2] == 'V' or sVIN[2] == '1' or sVIN[2] == '2' or sVIN[2] == '3':
        if sVIN[3:5] == 'BA':
            carxing = 'Protege'
        elif sVIN[3:5] == 'BB':
            carxing = '323/Protege'
        elif sVIN[3:5] == 'BC':
            carxing = 'Protege'
        elif sVIN[3:5] == 'BD':
            carxing = 'GLC,GLC旅行车'
        elif sVIN[3:5] == 'BF':
            carxing = '323'
        elif sVIN[3:5] == 'BG':
            carxing = '323,protege'
        elif sVIN[3:5] == 'BJ':
            carxing = 'Protege'
        elif sVIN[3:5] == 'CR':
            carxing = 'B2300,B3000,B4000'
        elif sVIN[3:5] == 'CU':
            carxing = 'Navajo'
        elif sVIN[3:5] == 'DR':
            carxing = 'B2300,B3000,B4000'
        elif sVIN[3:5] == 'EC':
            carxing = 'MX-3'
        elif sVIN[3:5] == 'FB' or sVIN[3:5] == 'FC':
            carxing = 'RX7'
        elif sVIN[3:5] == 'GB' or sVIN[3:5] == 'GC' or sVIN[3:5] == 'GD':
            carxing = '626'
        elif sVIN[3:5] == 'MX':
            carxing = '6'
        elif sVIN[3:5] == 'GE':
            carxing = '626 MX6'
        elif sVIN[3:5] == 'GF':
            carxing = '626'
        elif sVIN[3:5] == 'HC' or sVIN[3:5] == 'HD':
            carxing = '929'
        elif sVIN[3:5] == 'LV':
            carxing = 'MPV'
        elif sVIN[3:5] == 'TA':
            carxing = 'Millenia'
        elif sVIN[3:5] == 'NA' or sVIN[3:5] == 'NB':
            carxing = 'MX-5 Miata'
        elif sVIN[3:5] == 'UC':
            carxing = 'B2000'
        elif sVIN[3:5] == 'ND':
            carxing = 'B2200柴油机'
        elif sVIN[3:5] == 'UF':
            carxing = 'B2000,B2200,B2600,B2600i'
        if sVIN[2] == 'V' or sVIN[2] == '1':
            if sVIN[5:7] == '14' or sVIN[5:7] == '22':
                cartype = '四门轿车(Sedan)'
            elif sVIN[5:7] == '23':
                cartype = '323两门舱背式车身'
            elif sVIN[5:7] == '23':
                cartype = '323两门舱背式车身'
            elif sVIN[5:7] == '24':
                cartype = '四门舱背式车身'
            elif sVIN[5:7] == '31':
                cartype = '两门Coupe式车身'
            elif sVIN[5:7] == '32':
                cartype = '两门Coupe式车身增压型'
            elif sVIN[5:7] == '33':
                cartype = 'R*7'
            elif sVIN[5:7] == '34':
                cartype = '两门Coupe Conv./Turbo'
            elif sVIN[5:7] == '35':
                cartype = 'Convertible活顶敞篷式'
            elif sVIN[5:7] == '43':
                cartype = '两门Coupe'
            elif sVIN[5:7] == '46':
                cartype = '四门Sedan(轿车)'
            elif sVIN[5:7] == '52':
                cartype = 'Wagon(旅行车)'
            if sVIN[7] == '1':
                fdjandbsx  = '1.8L四缸机/2.5L V6型发动机'
            elif sVIN[7] == '2':
                fdjandbsx = '1.6L四缸发动机/2.3L V6型超增压发动机'
            elif sVIN[7] == 'C':
                fdjandbsx = '2.0L四缸发动机'
            elif sVIN[7] == 'D':
                fdjandbsx = '2.5L V6型发动机'
        elif sVIN[2] == '2' or sVIN[2] == '3':
            if sVIN[5:7] == '52':
                cartype = 'Wagon'
            elif sVIN[5:7] == '62':
                cartype = 'Van(厢式车)'
    if sVIN[10] == '0':
        zpgc = 'Hiroshima 日本'
    elif sVIN[10] == '1':
        zpgc = 'Hofu 日本'
    elif sVIN[10] == '5':
        zpgc = 'Flatrock 密西根州，美国'
    elif sVIN[10] == 'T':
        zpgc = 'Edison 新泽西州（美）'
    elif sVIN[10] == 'U':
        zpgc = 'Louisville(美)肯塔基州'
    return safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, cartype_q
def jkFT_LEXUS(sVIN):
    cartype = '*'
    pl = '*'
    fdjandbsx = '*'
    carxing = '*'
    safe = '*'
    year = 0
    year = getYear(sVIN[9])
    company = '*'
    cartype_q = '*'
    zpgc = '*'
    typeFlag = -1
    if sVIN[1] == 'T':
        company = '丰田汽车公司'
    if sVIN[2] == '6':
        cartype_q = 'MPV多用途汽车'
    elif sVIN[2] == '8':
        cartype_q = '轿车'
    if sVIN[3] == 'B':
        cartype = '四门轿车(Sedan)'
    elif sVIN[3] == 'C':
        cartype = '两门Coupe汽车'
    elif sVIN[3] == 'G':
        cartype = '四门MPV两轮驱动'
    elif sVIN[3] == 'H':
        cartype = '四门MPV/四门MPV四轮驱动'
    if sVIN[4] == 'D':
        fdjandbsx = '2JZGE 3.0L V6'
    elif sVIN[4] == 'F':
        fdjandbsx = '1MZFE 3.0L L6(直列六缸)'
    elif sVIN[4] == 'H':
        fdjandbsx = '1UZFE 4.0L V8'
    elif sVIN[4] == 'J':
        fdjandbsx = '1FZFE 4.5L L6'
    elif sVIN[4] == 'R':
        fdjandbsx = '1 UZ·FE(2003)'
    elif sVIN[4] == 'T':
        fdjandbsx = '2UZFE 4.7L V8'
    if sVIN[5] == '0':
        carxing = 'LX470'
    elif sVIN[5] == '1':
        carxing = 'ES300(1996)/RX300'
    elif sVIN[5] == '2':
        carxing = 'ES300(1997-2000)/LS400'
    elif sVIN[5] == '3':
        carxing = 'SC300/400'
    elif sVIN[5] == '4':
        carxing = 'GS300'
    elif sVIN[5] == '6':
        carxing = 'GS300/400'
    elif sVIN[5] == '8':
        carxing = 'LX450'
    if sVIN[2] == '8':
        if sVIN[6] == '0':
            safe = 'LX470带双安全气囊/RX300带有双前部和侧向安全气囊'
        elif sVIN[6] == '2':
            safe = '带有双安全气囊'
        elif sVIN[6] == '7':
            safe = 'GS300带双安全气囊'
        elif sVIN[6] == '8':
            safe = 'LX450带双安全气囊/带双前部和侧向安全气囊'
    if sVIN[7] == 'F':
        if carxing == '*':
            carxing = 'LS400'
        else:
            carxing += '/LS400'
    elif sVIN[7] == 'G':
        if carxing == '*':
            carxing = 'ES300'
        else:
            carxing += '/ES300'
    elif sVIN[7] == 'J':
        if carxing == '*':
            carxing = 'LX450'
        else:
            carxing += '/LX450'
    elif sVIN[7] == 'S':
        if carxing == '*':
            carxing = 'GS300'
        else:
            carxing += '/GS300'
    elif sVIN[7] == 'U':
        if carxing == '*':
            carxing = 'RX300'
        else:
            carxing += '/RX300'
    elif sVIN[7] == 'W':
        if carxing == '*':
            carxing = 'LX470'
        else:
            carxing += '/LX470'
    elif sVIN[7] == 'X':
        if carxing == '*':
            carxing = 'GS400'
        else:
            carxing += '/GS400'
    elif sVIN[7] == 'Z':
        if carxing == '*':
            carxing = 'SC300'
        else:
            carxing += '/SC300'
    elif sVIN[7] == 'Y':
        if carxing == '*':
            carxing = 'SC400'
        else:
            carxing += '/SC400'
    if sVIN[10] == '0':
        zpgc = 'Japan(日本)'

    return safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, cartype_q



sfz_presix=['110101','110102','110105','110106','110107','110108','110109','110111','110112','110113','110114','110115','110116','110117','110228','110229','120101','120102',
            '120103','120104','120105','120106','120110','120111','120112','120113','120114','120115','120116','120221','120223','120225','130101','130102','130103','130104',
            '130105','130107','130108','130121','130123','130124','130125','130126','130127','130128','130129','130130','130131','130132','130133','130181','130182','130183',
            '130184','130185','130201','130202','130203','130204','130205','130207','130208','130209','130223','130224','130225','130227','130229','130281','130283','130301',
            '130302','130303','130304','130321','130322','130323','130324','130401','130402','130403','130404','130406','130421','130423','130424','130425','130426','130427',
            '130428','130429','130430','130431','130432','130433','130434','130435','130481','130501','130502','130503','130521','130522','130523','130524','130525','130526',
            '130527','130528','130529','130530','130531','130532','130533','130534','130535','130581','130582','130601','130602','130603','130604','130621','130622','130623',
            '130624','130625','130626','130627','130628','130629','130630','130631','130632','130633','130634','130635','130636','130637','130638','130681','130682','130683',
            '130684','130701','130702','130703','130705','130706','130721','130722','130723','130724','130725','130726','130727','130728','130729','130730','130731','130732',
            '130733','130801','130802','130803','130804','130821','130822','130823','130824','130825','130826','130827','130828','130901','130902','130903','130921','130922',
            '130923','130924','130925','130926','130927','130928','130929','130930','130981','130982','130983','130984','131001','131002','131003','131022','131023','131024',
            '131025','131026','131028','131081','131082','131101','131102','131121','131122','131123','131124','131125','131126','131127','131128','131181','131182','140101',
            '140105','140106','140107','140108','140109','140110','140121','140122','140123','140181','140201','140202','140203','140211','140212','140221','140222','140223',
            '140224','140225','140226','140227','140301','140302','140303','140311','140321','140322','140401','140402','140411','140421','140423','140424','140425','140426',
            '140427','140428','140429','140430','140431','140481','140501','140502','140521','140522','140524','140525','140581','140601','140602','140603','140621','140622',
            '140623','140624','140701','140702','140721','140722','140723','140724','140725','140726','140727','140728','140729','140781','140801','140802','140821','140822',
            '140823','140824','140825','140826','140827','140828','140829','140830','140881','140882','140901','140902','140921','140922','140923','140924','140925','140926',
            '140927','140928','140929','140930','140931','140932','140981','141001','141002','141021','141022','141023','141024','141025','141026','141027','141028','141029',
            '141030','141031','141032','141033','141034','141081','141082','141101','141102','141121','141122','141123','141124','141125','141126','141127','141128','141129',
            '141130','141181','141182','150101','150102','150103','150104','150105','150121','150122','150123','150124','150125','150201','150202','150203','150204','150205',
            '150206','150207','150221','150222','150223','150301','150302','150303','150304','150401','150402','150403','150404','150421','150422','150423','150424','150425',
            '150426','150428','150429','150430','150501','150502','150521','150522','150523','150524','150525','150526','150581','150601','150602','150621','150622','150623',
            '150624','150625','150626','150627','150701','150702','150703','150721','150722','150723','150724','150725','150726','150727','150781','150782','150783','150784',
            '150785','150801','150802','150821','150822','150823','150824','150825','150826','150901','150902','150921','150922','150923','150924','150925','150926','150927',
            '150928','150929','150981','152201','152202','152221','152222','152223','152224','152501','152502','152522','152523','152524','152525','152526','152527','152528',
            '152529','152530','152531','152921','152922','152923','210101','210102','210103','210104','210105','210106','210111','210112','210113','210114','210122','210123',
            '210124','210181','210201','210202','210203','210204','210211','210212','210213','210224','210281','210282','210283','210301','210302','210303','210304','210311',
            '210321','210323','210381','210401','210402','210403','210404','210411','210421','210422','210423','210501','210502','210503','210504','210505','210521','210522',
            '210601','210602','210603','210604','210624','210681','210682','210701','210702','210703','210711','210726','210727','210781','210782','210801','210802','210803',
            '210804','210811','210881','210882','210901','210902','210903','210904','210905','210911','210921','210922','211001','211002','211003','211004','211005','211011',
            '211021','211081','211101','211102','211103','211121','211122','211201','211202','211204','211221','211223','211224','211281','211282','211301','211302','211303',
            '211321','211322','211324','211381','211382','211401','211402','211403','211404','211421','211422','211481','220101','220102','220103','220104','220105','220106',
            '220112','220122','220181','220182','220183','220201','220202','220203','220204','220211','220221','220281','220282','220283','220284','220301','220302','220303',
            '220322','220323','220381','220382','220401','220402','220403','220421','220422','220501','220502','220503','220521','220523','220524','220581','220582','220601',
            '220602','220605','220621','220622','220623','220681','220701','220702','220721','220722','220723','220781','220801','220802','220821','220822','220881','220882',
            '222401','222402','222403','222404','222405','222406','222424','222426','230101','230102','230103','230104','230108','230109','230110','230111','230112','230123',
            '230124','230125','230126','230127','230128','230129','230182','230183','230184','230201','230202','230203','230204','230205','230206','230207','230208','230221',
            '230223','230224','230225','230227','230229','230230','230231','230281','230301','230302','230303','230304','230305','230306','230307','230321','230381','230382',
            '230401','230402','230403','230404','230405','230406','230407','230421','230422','230501','230502','230503','230505','230506','230521','230522','230523','230524',
            '230601','230602','230603','230604','230605','230606','230621','230622','230623','230624','230701','230702','230703','230704','230705','230706','230707','230708',
            '230709','230710','230711','230712','230713','230714','230715','230716','230722','230781','230801','230803','230804','230805','230811','230822','230826','230828',
            '230833','230881','230882','230901','230902','230903','230904','230921','231001','231002','231003','231004','231005','231024','231025','231081','231083','231084',
            '231085','231101','231102','231121','231123','231124','231181','231182','231201','231202','231221','231222','231223','231224','231225','231226','231281','231282',
            '231283','232721','232722','232723','310101','310104','310105','310106','310107','310108','310109','310110','310112','310113','310114','310115','310116','310117',
            '310118','310120','310230','320101','320102','320104','320105','320106','320111','320113','320114','320115','320116','320117','320118','320201','320202','320203',
            '320204','320205','320206','320211','320281','320282','320301','320302','320303','320305','320311','320312','320321','320322','320324','320381','320382','320401',
            '320402','320404','320405','320411','320412','320481','320482','320501','320505','320506','320507','320508','320509','320581','320582','320583','320585','320601',
            '320602','320611','320612','320621','320623','320681','320682','320684','320701','320703','320705','320706','320721','320722','320723','320724','320801','320802',
            '320803','320804','320811','320826','320829','320830','320831','320901','320902','320903','320921','320922','320923','320924','320925','320981','320982','321001',
            '321002','321003','321012','321023','321081','321084','321101','321102','321111','321112','321181','321182','321183','321201','321202','321203','321204','321281',
            '321282','321283','321301','321302','321311','321322','321323','321324','330101','330102','330103','330104','330105','330106','330108','330109','330110','330122',
            '330127','330182','330183','330185','330201','330203','330204','330205','330206','330211','330212','330225','330226','330281','330282','330283','330301','330302',
            '330303','330304','330322','330324','330326','330327','330328','330329','330381','330382','330401','330402','330411','330421','330424','330481','330482','330483',
            '330501','330502','330503','330521','330522','330523','330601','330602','330621','330624','330681','330682','330683','330701','330702','330703','330723','330726',
            '330727','330781','330782','330783','330784','330801','330802','330803','330822','330824','330825','330881','330901','330902','330903','330921','330922','331001',
            '331002','331003','331004','331021','331022','331023','331024','331081','331082','331101','331102','331121','331122','331123','331124','331125','331126','331127',
            '331181','340101','340102','340103','340104','340111','340121','340122','340123','340124','340181','340201','340202','340203','340207','340208','340221','340222',
            '340223','340225','340301','340302','340303','340304','340311','340321','340322','340323','340401','340402','340403','340404','340405','340406','340421','340501',
            '340503','340504','340506','340521','340522','340523','340601','340602','340603','340604','340621','340701','340702','340703','340711','340721','340801','340802',
            '340803','340811','340822','340823','340824','340825','340826','340827','340828','340881','341001','341002','341003','341004','341021','341022','341023','341024',
            '341101','341102','341103','341122','341124','341125','341126','341181','341182','341201','341202','341203','341204','341221','341222','341225','341226','341282',
            '341301','341302','341321','341322','341323','341324','341501','341502','341503','341521','341522','341523','341524','341525','341601','341602','341621','341622',
            '341623','341701','341702','341721','341722','341723','341801','341802','341821','341822','341823','341824','341825','341881','350101','350102','350103','350104',
            '350105','350111','350121','350122','350123','350124','350125','350128','350181','350182','350201','350203','350205','350206','350211','350212','350213','350301',
            '350302','350303','350304','350305','350322','350401','350402','350403','350421','350423','350424','350425','350426','350427','350428','350429','350430','350481',
            '350501','350502','350503','350504','350505','350521','350524','350525','350526','350527','350581','350582','350583','350601','350602','350603','350622','350623',
            '350624','350625','350626','350627','350628','350629','350681','350701','350702','350721','350722','350723','350724','350725','350781','350782','350783','350784',
            '350801','350802','350821','350822','350823','350824','350825','350881','350901','350902','350921','350922','350923','350924','350925','350926','350981','350982',
            '360101','360102','360103','360104','360105','360111','360121','360122','360123','360124','360201','360202','360203','360222','360281','360301','360302','360313',
            '360321','360322','360323','360401','360402','360403','360421','360423','360424','360425','360426','360427','360428','360429','360430','360481','360482','360501',
            '360502','360521','360601','360602','360622','360681','360701','360702','360721','360722','360723','360724','360725','360726','360727','360728','360729','360730',
            '360731','360732','360733','360734','360735','360781','360782','360801','360802','360803','360821','360822','360823','360824','360825','360826','360827','360828',
            '360829','360830','360881','360901','360902','360921','360922','360923','360924','360925','360926','360981','360982','360983','361001','361002','361021','361022',
            '361023','361024','361025','361026','361027','361028','361029','361030','361101','361102','361121','361122','361123','361124','361125','361126','361127','361128',
            '361129','361130','361181','370101','370102','370103','370104','370105','370112','370113','370124','370125','370126','370181','370201','370202','370203','370211',
            '370212','370213','370214','370281','370282','370283','370285','370301','370302','370303','370304','370305','370306','370321','370322','370323','370401','370402',
            '370403','370404','370405','370406','370481','370501','370502','370503','370521','370522','370523','370601','370602','370611','370612','370613','370634','370681',
            '370682','370683','370684','370685','370686','370687','370701','370702','370703','370704','370705','370724','370725','370781','370782','370783','370784','370785',
            '370786','370801','370802','370811','370826','370827','370828','370829','370830','370831','370832','370881','370882','370883','370901','370902','370911','370921',
            '370923','370982','370983','371001','371002','371081','371082','371083','371101','371102','371103','371121','371122','371201','371202','371203','371301','371302',
            '371311','371312','371321','371322','371323','371324','371325','371326','371327','371328','371329','371401','371402','371421','371422','371423','371424','371425',
            '371426','371427','371428','371481','371482','371501','371502','371521','371522','371523','371524','371525','371526','371581','371601','371602','371621','371622',
            '371623','371624','371625','371626','371701','371702','371721','371722','371723','371724','371725','371726','371727','371728','410101','410102','410103','410104',
            '410105','410106','410108','410122','410181','410182','410183','410184','410185','410201','410202','410203','410204','410205','410211','410221','410222','410223',
            '410224','410225','410301','410302','410303','410304','410305','410306','410311','410322','410323','410324','410325','410326','410327','410328','410329','410381',
            '410401','410402','410403','410404','410411','410421','410422','410423','410425','410481','410482','410501','410502','410503','410505','410506','410522','410523',
            '410526','410527','410581','410601','410602','410603','410611','410621','410622','410701','410702','410703','410704','410711','410721','410724','410725','410726',
            '410727','410728','410781','410782','410801','410802','410803','410804','410811','410821','410822','410823','410825','410882','410883','410901','410902','410922',
            '410923','410926','410927','410928','411001','411002','411023','411024','411025','411081','411082','411101','411102','411103','411104','411121','411122','411201',
            '411202','411221','411222','411224','411281','411282','411301','411302','411303','411321','411322','411323','411324','411325','411326','411327','411328','411329',
            '411330','411381','411401','411402','411403','411421','411422','411423','411424','411425','411426','411481','411501','411502','411503','411521','411522','411523',
            '411524','411525','411526','411527','411528','411601','411602','411621','411622','411623','411624','411625','411626','411627','411628','411681','411701','411702',
            '411721','411722','411723','411724','411725','411726','411727','411728','411729','419001','420101','420102','420103','420104','420105','420106','420107','420111',
            '420112','420113','420114','420115','420116','420117','420201','420202','420203','420204','420205','420222','420281','420301','420302','420303','420321','420322',
            '420323','420324','420325','420381','420501','420502','420503','420504','420505','420506','420525','420526','420527','420528','420529','420581','420582','420583',
            '420601','420602','420606','420607','420624','420625','420626','420682','420683','420684','420701','420702','420703','420704','420801','420802','420804','420821',
            '420822','420881','420901','420902','420921','420922','420923','420981','420982','420984','421001','421002','421003','421022','421023','421024','421081','421083',
            '421087','421101','421102','421121','421122','421123','421124','421125','421126','421127','421181','421182','421201','421202','421221','421222','421223','421224',
            '421281','421301','421303','421321','421381','422801','422802','422822','422823','422825','422826','422827','422828','429004','429005','429006','429021','430101',
            '430102','430103','430104','430105','430111','430112','430121','430124','430181','430201','430202','430203','430204','430211','430221','430223','430224','430225',
            '430281','430301','430302','430304','430321','430381','430382','430401','430405','430406','430407','430408','430412','430421','430422','430423','430424','430426',
            '430481','430482','430501','430502','430503','430511','430521','430522','430523','430524','430525','430527','430528','430529','430581','430601','430602','430603',
            '430611','430621','430623','430624','430626','430681','430682','430701','430702','430703','430721','430722','430723','430724','430725','430726','430781','430801',
            '430802','430811','430821','430822','430901','430902','430903','430921','430922','430923','430981','431001','431002','431003','431021','431022','431023','431024',
            '431025','431026','431027','431028','431081','431101','431102','431103','431121','431122','431123','431124','431125','431126','431127','431128','431129','431201',
            '431202','431221','431222','431223','431224','431225','431226','431227','431228','431229','431230','431281','431301','431302','431321','431322','431381','431382',
            '433101','433122','433123','433124','433125','433126','433127','433130','440101','440103','440104','440105','440106','440111','440112','440113','440114','440115',
            '440116','440183','440184','440201','440203','440204','440205','440222','440224','440229','440232','440233','440281','440282','440301','440303','440304','440305',
            '440306','440307','440308','440401','440402','440403','440404','440501','440507','440511','440512','440513','440514','440515','440523','440601','440604','440605',
            '440606','440607','440608','440701','440703','440704','440705','440781','440783','440784','440785','440801','440802','440803','440804','440811','440823','440825',
            '440881','440882','440883','440901','440902','440903','440923','440981','440982','440983','441201','441202','441203','441223','441224','441225','441226','441283',
            '441284','441301','441302','441303','441322','441323','441324','441401','441402','441421','441422','441423','441424','441426','441427','441481','441501','441502',
            '441521','441523','441581','441601','441602','441621','441622','441623','441624','441625','441701','441702','441721','441723','441781','441801','441802','441803',
            '441821','441823','441825','441826','441881','441882','445101','445102','445103','445122','445201','445202','445203','445222','445224','445281','445301','445302',
            '445321','445322','445323','445381','450101','450102','450103','450105','450107','450108','450109','450122','450123','450124','450125','450126','450127','450201',
            '450202','450203','450204','450205','450221','450222','450223','450224','450225','450226','450301','450302','450303','450304','450305','450311','450312','450321',
            '450323','450324','450325','450326','450327','450328','450329','450330','450331','450332','450401','450403','450405','450406','450421','450422','450423','450481',
            '450501','450502','450503','450512','450521','450601','450602','450603','450621','450681','450701','450702','450703','450721','450722','450801','450802','450803',
            '450804','450821','450881','450901','450902','450903','450921','450922','450923','450924','450981','451001','451002','451021','451022','451023','451024','451025',
            '451026','451027','451028','451029','451030','451031','451101','451102','451121','451122','451123','451201','451202','451221','451222','451223','451224','451225',
            '451226','451227','451228','451229','451281','451301','451302','451321','451322','451323','451324','451381','451401','451402','451421','451422','451423','451424',
            '451425','451481','460101','460105','460106','460107','460108','460201','460321','460322','460323','469001','469002','469003','469005','469006','469007','469021',
            '469022','469023','469024','469025','469026','469027','469028','469029','469030','500101','500102','500103','500104','500105','500106','500107','500108','500109',
            '500110','500111','500112','500113','500114','500115','500116','500117','500118','500119','500223','500224','500226','500227','500228','500229','500230','500231',
            '500232','500233','500234','500235','500236','500237','500238','500240','500241','500242','500243','510101','510104','510105','510106','510107','510108','510112',
            '510113','510114','510115','510121','510122','510124','510129','510131','510132','510181','510182','510183','510184','510301','510302','510303','510304','510311',
            '510321','510322','510401','510402','510403','510411','510421','510422','510501','510502','510503','510504','510521','510522','510524','510525','510601','510603',
            '510623','510626','510681','510682','510683','510701','510703','510704','510722','510723','510724','510725','510726','510727','510781','510801','510802','510811',
            '510812','510821','510822','510823','510824','510901','510903','510904','510921','510922','510923','511001','511002','511011','511024','511025','511028','511101',
            '511102','511111','511112','511113','511123','511124','511126','511129','511132','511133','511181','511301','511302','511303','511304','511321','511322','511323',
            '511324','511325','511381','511401','511402','511421','511422','511423','511424','511425','511501','511502','511503','511521','511523','511524','511525','511526',
            '511527','511528','511529','511601','511602','511603','511621','511622','511623','511681','511701','511702','511703','511722','511723','511724','511725','511781',
            '511801','511802','511803','511822','511823','511824','511825','511826','511827','511901','511902','511903','511921','511922','511923','512001','512002','512021',
            '512022','512081','513221','513222','513223','513224','513225','513226','513227','513228','513229','513230','513231','513232','513233','513321','513322','513323',
            '513324','513325','513326','513327','513328','513329','513330','513331','513332','513333','513334','513335','513336','513337','513338','513401','513422','513423',
            '513424','513425','513426','513427','513428','513429','513430','513431','513432','513433','513434','513435','513436','513437','520101','520102','520103','520111',
            '520112','520113','520115','520121','520122','520123','520181','520201','520203','520221','520222','520301','520302','520303','520321','520322','520323','520324',
            '520325','520326','520327','520328','520329','520330','520381','520382','520401','520402','520421','520422','520423','520424','520425','520501','520502','520521',
            '520522','520523','520524','520525','520526','520527','520601','520602','520603','520621','520622','520623','520624','520625','520626','520627','520628','522301',
            '522322','522323','522324','522325','522326','522327','522328','522601','522622','522623','522624','522625','522626','522627','522628','522629','522630','522631',
            '522632','522633','522634','522635','522636','522701','522702','522722','522723','522725','522726','522727','522728','522729','522730','522731','522732','530101',
            '530102','530103','530111','530112','530113','530114','530122','530124','530125','530126','530127','530128','530129','530181','530301','530302','530321','530322',
            '530323','530324','530325','530326','530328','530381','530401','530402','530421','530422','530423','530424','530425','530426','530427','530428','530501','530502',
            '530521','530522','530523','530524','530601','530602','530621','530622','530623','530624','530625','530626','530627','530628','530629','530630','530701','530702',
            '530721','530722','530723','530724','530801','530802','530821','530822','530823','530824','530825','530826','530827','530828','530829','530901','530902','530921',
            '530922','530923','530924','530925','530926','530927','532301','532322','532323','532324','532325','532326','532327','532328','532329','532331','532501','532502',
            '532503','532504','532523','532524','532525','532527','532528','532529','532530','532531','532532','532601','532622','532623','532624','532625','532626','532627',
            '532628','532801','532822','532823','532901','532922','532923','532924','532925','532926','532927','532928','532929','532930','532931','532932','533102','533103',
            '533122','533123','533124','533321','533323','533324','533325','533421','533422','533423','540101','540102','540121','540122','540123','540124','540125','540126',
            '540127','542121','542122','542123','542124','542125','542126','542127','542128','542129','542132','542133','542221','542222','542223','542224','542225','542226',
            '542227','542228','542229','542231','542232','542233','542301','542322','542323','542324','542325','542326','542327','542328','542329','542330','542331','542332',
            '542333','542334','542335','542336','542337','542338','542421','542422','542423','542424','542425','542426','542427','542428','542429','542430','542431','542521',
            '542522','542523','542524','542525','542526','542527','542621','542622','542623','542624','542625','542626','542627','610101','610102','610103','610104','610111',
            '610112','610113','610114','610115','610116','610122','610124','610125','610126','610201','610202','610203','610204','610222','610301','610302','610303','610304',
            '610322','610323','610324','610326','610327','610328','610329','610330','610331','610401','610402','610403','610404','610422','610423','610424','610425','610426',
            '610427','610428','610429','610430','610431','610481','610501','610502','610521','610522','610523','610524','610525','610526','610527','610528','610581','610582',
            '610601','610602','610621','610622','610623','610624','610625','610626','610627','610628','610629','610630','610631','610632','610701','610702','610721','610722',
            '610723','610724','610725','610726','610727','610728','610729','610730','610801','610802','610821','610822','610823','610824','610825','610826','610827','610828',
            '610829','610830','610831','610901','610902','610921','610922','610923','610924','610925','610926','610927','610928','610929','611001','611002','611021','611022',
            '611023','611024','611025','611026','620101','620102','620103','620104','620105','620111','620121','620122','620123','620201','620301','620302','620321','620401',
            '620402','620403','620421','620422','620423','620501','620502','620503','620521','620522','620523','620524','620525','620601','620602','620621','620622','620623',
            '620701','620702','620721','620722','620723','620724','620725','620801','620802','620821','620822','620823','620824','620825','620826','620901','620902','620921',
            '620922','620923','620924','620981','620982','621001','621002','621021','621022','621023','621024','621025','621026','621027','621101','621102','621121','621122',
            '621123','621124','621125','621126','621201','621202','621221','621222','621223','621224','621225','621226','621227','621228','622901','622921','622922','622923',
            '622924','622925','622926','622927','623001','623021','623022','623023','623024','623025','623026','623027','630101','630102','630103','630104','630105','630121',
            '630122','630123','630202','630221','630222','630223','630224','630225','632221','632222','632223','632224','632321','632322','632323','632324','632521','632522',
            '632523','632524','632525','632621','632622','632623','632624','632625','632626','632701','632722','632723','632724','632725','632726','632801','632802','632821',
            '632822','632823','640101','640104','640105','640106','640121','640122','640181','640201','640202','640205','640221','640301','640302','640303','640323','640324',
            '640381','640401','640402','640422','640423','640424','640425','640501','640502','640521','640522','650101','650102','650103','650104','650105','650106','650107',
            '650109','650121','650201','650202','650203','650204','650205','652101','652122','652123','652201','652222','652223','652301','652302','652323','652324','652325',
            '652327','652328','652701','652702','652722','652723','652801','652822','652823','652824','652825','652826','652827','652828','652829','652901','652922','652923',
            '652924','652925','652926','652927','652928','652929','653001','653022','653023','653024','653101','653121','653122','653123','653124','653125','653126','653127',
            '653128','653129','653130','653131','653201','653221','653222','653223','653224','653225','653226','653227','654002','654003','654021','654022','654023','654024',
            '654025','654026','654027','654028','654201','654202','654221','654223','654224','654225','654226','654301','654321','654322','654323','654324','654325','654326',
            '659001','659002','659003','659004','710000','810000','820000']
def code(str):
    str2 = '*'
    if r'\u' in str:
        str=str.replace('\\\\u','\\u')
        ##print str.decode('unicode_escape')
        try:
            str2 = str.decode('unicode_escape')
        except:
            return '*'
        return str2
    else:
        str=str.replace('\\','%')
        try:
            str1=str.encode('utf-8')
            str2= urllib.unquote(str1).decode('utf-8', 'replace')
        except:
            ##print str
            return str
        return str2

def carvin_preprocess(line):
    pat_GCBMW = re.compile(r'([^A-Za-z0-9](LBV[A-HJ-NPR-Z0-9]{4}([0-1])[X0-9][A-HJ-NPR-TV-Y1-9][A-HJ-NPR-Z0-9]{3}[0-9]{4})[^A-Za-z0-9])')
    pat_JKBMW = re.compile(r'([^A-Za-z0-9](((WB)|(4U))[AS][A-H][A-GHJKMNPR][0-9][3-4][0-4][X0-9][A-HJ-NPR-Z1-9][A-GJ-LNPW][A-HJ-NPR-Z0-9]{2}[0-9]{4})[^A-Za-z0-9])')
    pat_GCBENZ = re.compile(r'([^A-Za-z0-9](LE4(GF|WF|WG|FT|HG|TG|CG)[A-HJ-NPR-Z0-9]{4}[A-HJ-NPR-TV-Y1-9][A-DF-HJ][0-9]{6})[^A-Za-z0-9])')
    pat_JKBENZ = re.compile(r'([^A-Za-z0-9](((WDB)|(4JG))[A-HJ-LNPRS][ABDE](56|57)[A-H][X0-9][A-HJ-NPR-TV-Y1-9][A-DF-HJTX][A-HJ-NPR-Z0-9]{2}[0-9]{4})[^A-Za-z0-9])')
    pat_JKTOYOTA_1 = re.compile(r'([^A-Za-z0-9]([J4]T[1-6ABDEGMNX][1A-EKHGJMSVZ][1A-HJKL-NPRSTUVY][0-59AETFCDSHUXYW][0-689DFJB][A-FHJ-NPRTUV013][X0-9][A-HJ-NPR-TV-Y1-9][A-HJ-NPR-Z0-9]{4}[0-9]{3})[^A-Za-z0-9])')
    pat_GCTOYOTA = re.compile(r'([^A-Za-z0-9]((LVG|LHG|LFP|LFM|LFV)F[2-4][A-C][1-3A-C][A-HJ-NPR-Z0-9]{2}[A-HJ-NPR-TV-Y1-9][A-HJ-NPR-Z0-9]{4}[0-9]{3})[^A-Za-z0-9])')
    pat_YQTOYOTA = re.compile(r'([^A-Za-z0-9](LFPF[234][ABC][BEHL][123ABC][0-9X][A-HJ-NPR-TV-Y1-9]U[A-HJ-NPR-Z0-9]{3}[0-9]{3})[^A-Za-z0-9])')
    pat_SHVW = re.compile(r'([^A-Za-z0-9](LSV[A-CEFHK][A-HJ-M]([0-6])(33|9F|9J|5X)[0-9X][A-HJ-NPR-TV-Y1-9]2[A-HJ-NPR-Z0-9]{2}[0-9]{4})[^A-Za-z0-9])')
    pat_JKVW = re.compile(r'([^A-Za-z0-9]([W139][BV][123W]([A-HK-MPRT])[A-HJKM][0-68](1C|1E|1H|1J|1V|3B|9M|1G|15|16|17|30|31|50|70)[X0-9][A-HJ-NPR-TV-Y1-9][BEGHJKMNPSVWY][A-HJ-NPR-Z0-9]{2}[0-9]{4})[^A-Za-z0-9])')
    pat_YQVW = re.compile(r'([^A-Za-z0-9](LFV[AB123456789][A-C]([1-6])(4B|8E|1G|1J|2J|1K|2K|3C|15)[0-9X][A-HJ-NPR-TV-Y1-9]3[A-HJ-NPR-Z0-9]{2}[0-9]{4})[^A-Za-z0-9])')
    pat_GZBT = re.compile(r'([^A-Za-z0-9](LHGCM[456]([56])[456][X0-9][A-HJ-NPR-TV-Y1-9]2[A-HJ-NPR-Z0-9]{3}[0-9]{3})[^A-Za-z0-9])')
    pat_BJXD = re.compile(r'([^A-Za-z0-9](LHBSCC[BHL]([CHK])[X0-9][A-HJ-NPR-TV-Y1-9]X[A-HJ-NPR-Z0-9]{3}[0-9]{3})[^A-Za-z0-9])')
    pat_MGTY = re.compile(r'([^A-Za-z0-9]([1234JKW][CGLY08]([12345678])[A-HJ-NPR-Z]{2}[12345689][1234567][A-HJ-NPR-Z0-9][X0-9][A-HJ-NPR-TV-Y1-9][A-HJ-NPR-Z0-9]{4}[0-9]{3})[^A-Za-z0-9])')
    pat_BSJ = re.compile(r'([^A-Za-z0-9](WP0[ABCDEJ]([ABC])[012]9[12345689][X0-9][A-HJ-NPR-TV-Y1-9][NSU][A-HJ-NPR-Z0-9]{3}[0-9]{3})[^A-Za-z0-9])')
    pat_JKLH = re.compile('([^A-Za-z0-9](SAL((DH)|(DV)|(HC)|(HE)|(HF)|(HV)|(JN)|(JY)|(PA)|(PC)|(PE)|(PF)|(PV)|(TY))[12][123456][48][X0-9][A-HJ-NPR-TV-Y1-9]A[A-HJ-NPR-Z0-9]{3}[0-9]{3})[^A-Za-z0-9])')
    pat_GQCQ = re.compile(r'([^A-Za-z0-9](LMG[DFABG]K([13])([37CSG])[258][X0-9][A-HJ-NPR-TV-Y1-9][A-HJ-NPR-Z0-9]{4}[0-9]{3})[^A-Za-z0-9])')
    pat_jl_1 = re.compile(r'([^A-Za-z0-9](((L6T)|(LJU)|(LB3)|(LJ2)|(L10))[01567][0-9KLMNPRSTUV](([0123456JKRS][247])|([789UPVWTXEFG]2)|([YF]4)|([WXZ]5))[SZWABNCDE][0-9X][A-HJ-NPR-Z0-9][A-HJ-MPT-X][A-HJ-NPR-Z0-9][0-9]{5})[^A-Za-z0-9])')
    pat_jl_2 = re.compile(r'([^A-Za-z0-9](((L6T)|(LJU)|(LB3)|(LJ2)|(L10))((E3)|(F7)|(F3)|(F5)|(FC)|(X3)|(X7)|(F6)|(SX)|(KC)|(NL)|(N3)|(S2)|(FY)|(VF)|(CX)|(CC)|(CS)|(CY)|(BX)|(GA)|(GC))[0-9E-GJKPR-Z][A-GRS0][1-9AB][0-9X][A-HJ-NPR-Z0-9][A-HJ-MPT-X][A-HJ-NPR-Z0-9][0-9]{5})[^A-Za-z0-9])')
    pat_jkrc_1 = re.compile(r'([^A-Za-z0-9]([J1435]N[1-468KR][0A-HJMNPSTV][A-DFJMNR-WYZ][A-HJ-NPR-Z0-9][ABDEFYZNTF1-8][12356A-FHJPSYUW][X0-9][A-HJ-NPR-Z0-9]{5}[0-9]{3})[^A-Za-z0-9])')
    pat_jkrc_2 = re.compile(r'([^A-Za-z0-9](JNK[ABCDHN][AFJGPRYV][0-36][14-7][ACDEFPY][X0-9][A-HJ-NPR-Z0-9]{5}[0-9]{3})[^A-Za-z0-9])')
    pat_jkbt_1 = re.compile(
        r'([^A-Za-z0-9](((JH[M1-4])|([14][HS][G1-4])|(2H[G1-4]))[A-ERSKVW][A-HNRTLJK][1-9]{2}[0-9][X0-9][A-HJ-NPR-Z0-9]{5}[0-9]{3})[^A-Za-z0-9])')
    pat_jkbt_2 = re.compile(
        r'([^A-Za-z0-9]([J124][H9][HMU4]((CC2)|(DH1)|(DA[39])|(DB[1278])|(DC[24])|(KA[234789])|(MB4)|(NA[12])|(UA235)|(YA[123]))[1-8][1-9][X0-9][A-HJ-NPR-Z0-9][ACHLST][A-HJ-NPR-Z0-9]{3}[0-9]{3})[^A-Za-z0-9])')
    pat_jkmzd = re.compile(
        r'([^A-Za-z0-9](((JM)|([14][FY]))[1-47V][B-HL-NSTUYZ][A-GJRKLSUVW][0-6][0-79][1-68A-DFLUVXZ][X0-9][A-HJ-NPR0-9][015DTU][A-HJ-NPR-Z0-9]{3}[0-9]{3})[^A-Za-z0-9])')
    pat_jktoyota_lexus = re.compile(r'([^A-Z0-9](JT[JH68][BKCGJUVHYZ][A-FHKJR-WYZ][0-568MR][0-378BCG][ACEFGJSTUWXYZ][X0-9][A-HJ-NPR0-9][02][A-HJ-NPR-Z0-9]{3}[0-9]{3})[^A-Z0-9])')
    patternHost=re.compile(r'Host: ([\s\S]+?)\\0D\\0A')
    patternUserAgent=re.compile(r'(User-Agent:[\s\S]+?)\\0D\\0A')
    pingtai=re.compile(r'Mozilla/[54].0 \(([\S\s]+?)\) [\S\s]+?\) ([\S\s]+)')
    phone = re.compile(r'"[Pp]hone":"([\S\s]*?)"')
    phone_mobile = re.compile(r'"[Mm]obile":"([\S\s]*?)"')
    mobilephone = re.compile(r'"[Mm]obile_[Pp]hone":"([\S\s]*?)"')
    telephone = re.compile(r'"[Tt]ele[Pp]hone":"([\S\s]*?)"')
    tele = re.compile(r'"[Tt]el":"([\S\s]*?)"')
    # tel1=re.compile(r'"[Tt]el\.":"([\S\s]*?)"')
    name_true = re.compile(r'"[Tt]rue_[Nn]ame":"([\S\s]*?)"')
    name_real = re.compile(r'"real[Nn]ame":"([\S\s]*?)"')
    name_reality = re.compile(r'"[Rr]eality[Nn]ame":"([\S\s]*?)"')
    name = re.compile(r'"[Nn]ame":"([\S\s]*?)"')
    address = re.compile(r'"address":"([\S\s]*?)"')
    addr = re.compile(r'"addr":"([\S\s]*?)"')
    longpat = re.compile(r'((([Ll]ong)|([Ll]ng)|([Ll]on))([\s\S]{1,15})((([789][0-9]\.[0-9][\s\S]+?)[^0-9])|((1[0123][0-9]\.[0-9][\s\S]+?)[^0-9])))')
    latpat = re.compile(r'(([Ll]at)([\s\S]{1,15})(((1[5-9]\.[0-9][\S\s]+?})[^0-9])|(([2-4][0-9]\.[0-9][\S\s]+?)[^0-9])|((5[0-5]\.[0-9][\S\s]+?)[^0-9])))')
    sfzpattern = re.compile(r'\D((1[1-5]|2[1-3]|3[1-7]|4[1-6]|5[0-4]|6[1-5]|71|8[1-2])[0|1|2|3|4|5|9][0-9]{1}[0|1|2|3|4|5|8][0-9]{1}(19[0-9]{2}|(200[0-9]{1}|201[0-9]{1}|202[0-2]{1}))((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|30|31)|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}([0-9]|x|X))\D')
    carnumpat = re.compile(r'\D((1[1-5]|2[1-3]|3[1-7]|4[1-6]|5[0-4]|6[1-5])[0|1|2|3|4|5|9][0-9]{9})\D')
    platenum = re.compile(r'((("[Pp]late[Nn]o":")|("[Pp]late_[Nn]umber":")|("[Ll]icense[Pp]late":"))([\s\S]+?)")')
    patternHost=re.compile(r'Host:([\s\S]+?)\0D\0A')
    patternUserAgent=re.compile(r'(User-Agent:[\s\S]+?)\0D\0A')
    pingtai=re.compile(r'Mozilla/[54].0 \(([\S\s]+?)\) [\S\s]+?\) ([\S\s]+)')
    phone = re.compile(r'"[Pp]hone":"([\S\s]*?)"')
    phone_mobile = re.compile(r'"[Mm]obile":"([\S\s]*?)"')
    mobilephone = re.compile(r'"[Mm]obile_[Pp]hone":"([\S\s]*?)"')
    telephone = re.compile(r'"[Tt]ele[Pp]hone":"([\S\s]*?)"')
    tele = re.compile(r'"[Tt]el":"([\S\s]*?)"')
    # tel1=re.compile(r'"[Tt]el\.":"([\S\s]*?)"')
    name_true = re.compile(r'"[Tt]rue_[Nn]ame":"([\S\s]*?)"')
    name_real = re.compile(r'"real[Nn]ame":"([\S\s]*?)"')
    name_reality = re.compile(r'"[Rr]eality[Nn]ame":"([\S\s]*?)"')
    name = re.compile(r'"[Nn]ame":"([\S\s]*?)"')
    address = re.compile(r'"address":"([\S\s]*?)"')
    addr = re.compile(r'"addr":"([\S\s]*?)"')
    longpat = re.compile(r'((([Ll]ong)|([Ll]ng)|([Ll]on))([\s\S]{1,15})((([789][0-9]\.[0-9][\s\S]+?)[^0-9])|((1[0123][0-9]\.[0-9][\s\S]+?)[^0-9])))')
    latpat = re.compile(r'(([Ll]at)([\s\S]{1,15})(((1[5-9]\.[0-9][\S\s]+?})[^0-9])|(([2-4][0-9]\.[0-9][\S\s]+?)[^0-9])|((5[0-5]\.[0-9][\S\s]+?)[^0-9])))')
    sfzpattern = re.compile(r'\D((1[1-5]|2[1-3]|3[1-7]|4[1-6]|5[0-4]|6[1-5]|71|8[1-2])[0|1|2|3|4|5|9][0-9]{1}[0|1|2|3|4|5|8][0-9]{1}(19[0-9]{2}|(200[0-9]{1}|201[0-9]{1}|202[0-2]{1}))((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|30|31)|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}([0-9]|x|X))\D')
    carnumpat = re.compile(r'\D((1[1-5]|2[1-3]|3[1-7]|4[1-6]|5[0-4]|6[1-5])[0|1|2|3|4|5|9][0-9]{9})\D')
    platenum = re.compile(r'((("[Pp]late[Nn]o":")|("[Pp]late_[Nn]umber":")|("[Ll]icense[Pp]late":"))([\s\S]+?)")')
    sums = 0
    nums = 0
    tests= 0
    GCBMW_nums = 0
    JKBMW_nums = 0
    GCBENZ_nums = 0
    JKBENZ_nums = 0
    JKTOYOTA_nums = 0
    SHVW_nums = 0
    JKVW_nums = 0
    YQVW_nums = 0
    GZBT_nums = 0
    BJXD_nums = 0
    MGTY_nums = 0
    BSJ_nums = 0
    JKLH_nums = 0
    GQCQ_nums = 0
    jl_nums = 0
    jl_num = 0
    jkrc_num = 0
    jkrc1_nums = 0
    jkrc2_nums = 0
    jkbt_num = 0
    jkbt1_nums = 0
    jkbt2_nums = 0
    jkmzd_num = 0
    jkmzd_nums = 0
    jktoyota_lexus_nums = 0
    mgTY_jytg = 0
    mgTY_ytype = 0
    #print(line)
    li = line.strip().split('\t')
    data_tmp=li[7]
    # data_tmp=dealWithPart7(li[7])
    # data_tmp=str(data_tmp)
    # data_tmp=data_tmp[2:-1]
    # line=li[0]+'\t'+li[1]+'\t'+li[2]+'\t'+li[3]+'\t'+li[4]+'\t'+li[5]+'\t'+li[6]+'\t'+data_tmp
    #print("after dealwith ")
    #print(line)
    host = '*'
    pingtaistr = '*'
    liulanqistr = '*'
    phonestr = '*'
    namestr = '*'
    addrstr = '*'
    longlat = ''
    sfznum = ''
    carnum = ''
    platestr = ''
    cartype = '*'
    pl = '*'
    fdjandbsx = '*'
    carxing = '*'
    safe = '*'
    year = "*"
    company = '*'
    type_q = '*'
    zpgc = '*'
    vin_str = ''
    rethost = re.findall(patternHost,line)
    retUserAgent = re.findall(patternUserAgent, line)
    retphone = re.findall(phone, line)
    retphone_mobile = re.findall(phone_mobile, line)
    retmobilephone = re.findall(mobilephone, line)
    rettelephone = re.findall(telephone, line)
    rettele = re.findall(tele, line)
    # rettel1=re.findall(tel1,one)
    retname_true = re.findall(name_true, line)
    retname_real = re.findall(name_real, line)
    retname_reality = re.findall(name_reality, line)
    retname = re.findall(name, line)
    retaddress = re.findall(address, line)
    retaddr = re.findall(addr, line)
    retlong = re.findall(longpat, line)
    retlat = re.findall(latpat, line)
    retcarnum = re.findall(carnumpat, data_tmp)
    retsfz = re.findall(sfzpattern, data_tmp)
    retplate = re.findall(platenum,line)
    if len(retplate) != 0:
        for one in retplate:
            carplate = code(one[-1])
            platestr = platestr +carplate+ ';'
    if platestr == '':
        platestr = '*'
    if len(retsfz) != 0:
        for aa in retsfz:
            sixpre = aa[0][:6]
            if (sixpre in sfz_presix):
                sfznum =sfznum + aa[0]+ ';'
    if sfznum == '':
        sfznum = '*'
    if len(retcarnum) != 0:
        for aa in retcarnum:
            fourpre = aa[0][:4]
            for onesix in sfz_presix:
                if fourpre == onesix[:4]:
                    carnum =carnum + aa[0] + ';'
    if carnum == '':
        carnum = '*'
    longli = []
    latli = []
    if len(retlong) != 0:
        ##print retlong
        for one in retlong:
            if one[-3] != '':
                if one[-3].count('.') == 1:
                    longli.append(one[-3])
            elif one[-1] != '':
                if one[-1].count('.') == 1:
                    longli.append(one[-1])
        ##print longstr
    if len(retlat) != 0:
        for one in retlat:
            if one[-1] != '':
                if one[-1].count('.') == 1:
                    latli.append(one[-1])
            elif one[-3] != '':
                if one[-3].count('.') == 1:
                    latli.append(one[-3])
            elif one[-5] != '':
                if one[-5].count('.') == 1:
                    latli.append(one[-5])
    longlinum = len(longli)
    latlinum = len(latli)
    if longlinum ==0 or latlinum == 0:
        longlat = '*'
    else :
        longlat =longli[0]+','+latli[0]
    if longlat == '':
        longlat = '*'
    carnumstr='*'
    if len(retcarnum) != 0:
        carnumstr = retcarnum[0]
        ##print retcarnum
    phonestr='*'
    if len(retphone):
        if len(retphone[0]) == 11 and retphone[0].isdigit():
            phonestr = retphone[0]
            # #print phonestr
    elif len(retmobilephone):
        if len(retmobilephone[0]) == 11 and retmobilephone[0].isdigit():
            phonestr = retmobilephone[0]
            # #print phonestr
    elif len(retphone_mobile):
        if len(retphone_mobile[0]) == 11 and retphone_mobile[0].isdigit():
            phonestr = retphone_mobile[0]
            # #print phonestr
    elif len(rettelephone):
        if len(rettelephone[0]) == 11 and rettelephone[0].isdigit():
            phonestr = rettelephone[0]
            # #print phonestr
    elif len(rettele):
        if len(rettele[0]) == 11 and rettele[0].isdigit():
            phonestr = rettele[0]
            # #print phonestr
    namestr='*'
    if len(retname_real):
        namestr = code(retname_real[0])
        # #print namestr
    elif len(retname_reality):
        namestr = code(retname_reality[0])
        # #print namestr
    elif len(retname_true):
        namestr = code(retname_true[0])
        # #print namestr
    elif len(retname):
        namestr = code(retname[0])
        # #print namestr
    addrstr='*'
    if len(retaddr):
        if len(retaddr[0]):
            if code(retaddr[0]) != '未分配或者内网IP':
                addrstr = code(retaddr[0])
                # #print addrstr
            # #print one
    elif len(retaddress):
        if len(retaddress[0]):
            addrstr = code(retaddress[0])
    host='*'
    if len(rethost) != 0:
        host = rethost[0]
        ##print host
    pingtaistr='*'
    liulanqistr='*'
    if len(retUserAgent)!= 0:
        #print("useragent")
        retpingtai=re.findall(pingtai,retUserAgent[0])
        for i in range(len(retpingtai)):
            ##print retpingtai[i]
            if  ('Windows NT' in retpingtai[i][0]) or ('MacOS' in retpingtai[i][0]):
                pingtaistr= 'PC '+retpingtai[i][0]
            else:
               pingtaistr= 'PM '+retpingtai[i][0]
            liulanqistr = retpingtai[i][1]
    sres = platestr+'\t' +sfznum+'\t' +carnum+'\t' +longlat+'\t' +phonestr+'\t' +namestr+'\t' +addrstr+'\t' +host+'\t' +liulanqistr+'\t' +pingtaistr+'\t'
    line=line.replace("\\t","\\")
    if li[0] == 'BIO030-CAR_VIN_GCBMW':
        ret = re.findall(pat_GCBMW, data_tmp)
        if len(ret) != 0:
            ##print 'CAR_VIN_GCBMW:'
            ##print ret
            resC = checkVIN(ret[0][1])
            if resC == True:
                GCBMW_nums += 1
                nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                year = getYear(sVIN[9])
                sres = sres + line+ '\t' + sVIN + '\t' + 'GCBMW' + '\t' + country + '\t' +'*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*'+ '\t' + '*' + '\t' + '*' + '\t' + str(year) + '\t' + '*' + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
            else:
                pass
                ##print ret[0][1]
    elif li[0] == 'BIO030-CAR_VIN_JKBMW':
        tests+=1
        ret = re.findall(pat_JKBMW, data_tmp)

        ##print ret
        if len(ret) != 0:
            ##print 'CAR_VIN_JKBMW:'
            ##print ret
            resC = checkVIN(ret[0][1])
            ##print sums
            if resC == True:
                ##print sums
                nums += 1
                JKBMW_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe, pl, cartype, fdjandbsx, carxing, zpgc, year = jkBWM(sVIN)
                sres = sres + line+ '\t' + sVIN + '\t' + 'JKBWM' + '\t' + country + '\t' + '德国宝马汽车公司' + '\t' + '*' + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
            else:
                pass
                ##print ret[0][1]
    #未解析
    elif li[0] == 'BIO030-CAR_VIN_GCBENZ':
        ret = re.findall(pat_GCBENZ, data_tmp)
        if len(ret) != 0:
            ##print 'CAR_VIN_GCBENZ'
            ##print ret
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                GCBENZ_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                year = getYear(sVIN[9])
                sres = sres + line+ '\t' + sVIN + '\t' + 'GCBENZ' + '\t' + country + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + str(year) + '\t' + '*' + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
            else:
                pass
                # #print ret[0][1]
    elif li[0] == 'BIO030-CAR_VIN_JKBENZ':
        ret = re.findall(pat_JKBENZ, data_tmp)
        if len(ret) != 0:
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                JKBENZ_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe, pl, cartype, fdjandbsx, carxing, zpgc, year = jkBENZ(sVIN)
                sres = sres + line+ '\t' + sVIN + '\t' + 'JKBENZ' + '\t' + country + '\t' +'德国梅赛德斯-奔驰汽车公司' + '\t' + '*' + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
            else:
                pass
                # #print ret[0][1]
    elif li[0] == 'BIO030-CAR_VIN_JKTOYOTA':
        ret = re.findall(pat_jktoyota_lexus, data_tmp)
        istrue = False
        if len(ret) != 0:
            tempret = 0
            vin_li = []
            for one in ret:
                if one[1] not in vin_li:
                    vin_li.append(one[1])
            for one in vin_li:
                resC = checkVIN(one)
                if resC == True:
                    if istrue == False:
                        jktoyota_lexus_nums += 1
                    if vin_str == '':
                        vin_str = one
                    else:
                        vin_str = vin_str + ';' + one
                    istrue = True
                    sVIN = one
                    # #print sVIN
                    # #print sVIN
                    country = scCountry(sVIN[0])
                    year = getYear(sVIN[9])
                    safe1, pl1, cartype1, fdjandbsx1, carxing1, zpgc1, year1, company1, type_q1 = jkFT_LEXUS(sVIN)
                    if tempret == 0:
                        safe = safe1
                        pl = pl1
                        cartype = cartype1
                        fdjandbsx = fdjandbsx1
                        carxing = carxing1
                        zpgc = zpgc1
                        year = str(year1)
                        company = company1
                        type_q = type_q1
                    else:
                        safe = safe + ';' + safe1
                        pl = pl + ';' + pl1
                        cartype = cartype + ';' + cartype1
                        fdjandbsx = fdjandbsx + ';' + fdjandbsx1
                        carxing = carxing + ';' + carxing1
                        zpgc = zpgc + ';' + zpgc1
                        year = str(year) + ';' + str(year1)
                        company = company + ';' + company1
                        type_q = type_q + ';' + type_q1
                    tempret += 1
                else:
                    pass
            if istrue == True:
                sres = sres + line+ '\t' + vin_str + '\t' + 'JKTOYOTA_LEXUS' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t' + bkj_str_th(host) + '\t' + bkj_str_th(pingtaistr) + '\t' + bkj_str_th(liulanqistr) + '\t' + bkj_str_th(namestr) + '\t' + bkj_str_th(phonestr) + '\t' + bkj_str_th(addrstr) + '\t' + bkj_str_th(longlat) + '\t' + bkj_str_th(sfznum) + '\t' + bkj_str_th(carnum) + '\t' + platestr + '\n'
                return sres
        else:
            ret = re.findall(pat_JKTOYOTA_1, data_tmp)
            if len(ret) != 0:
                resC = checkVIN(ret[0][1])
                if resC == True:
                    nums += 1
                    sVIN = ret[0][1]
                    JKTOYOTA_nums += 1
                    country = scCountry(sVIN[0])
                    safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, type_q = jkTOYOTA(sVIN)
                    sres = sres + line+ '\t' + sVIN + '\t' + 'JKTOYOTA' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                    return sres
                else:
                    pass
    #未解析
    elif li[0] == 'BIO030-CAR_VIN_GCTOYOTA':
        ret = re.findall(pat_GCTOYOTA, data_tmp)
        if len(ret) != 0:
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                year = getYear(sVIN[9])
                sres = sres + line+ '\t' + sVIN + '\t' + 'GCTOYOTA' + '\t' + country + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + str(year) + '\t' + '*' + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
            else:
                pass
                # #print ret[0][1]
    elif li[0] == 'BIO030-CAR_VIN_YQTOYOTA':
        ret = re.findall(pat_YQTOYOTA, data_tmp)
        if len(ret) != 0:
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1

                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                year = getYear(sVIN[9])
                sres = sres + line+ '\t' + sVIN + '\t' + 'YQTOYOTA' + '\t' + country + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + str(year) + '\t' + '*' + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
            else:
                pass
                # #print ret[0][1]
    elif li[0] == 'BIO030-CAR_VIN_SHVW':
        ret = re.findall(pat_SHVW, data_tmp)

        if len(ret) != 0:
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                SHVW_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe, pl, cartype, fdjandbsx, carxing, zpgc, year = shVM(sVIN)
                sres = sres + line+ '\t' + sVIN + '\t' + 'SHVW' + '\t' + country + '\t' +  '中国上海大众汽车有限公司' + '\t' + '*' + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
            else:
                pass
                # #print ret[0][1]
    elif li[0] == 'BIO030-CAR_VIN_JKVW':
        ret = re.findall(pat_JKVW, data_tmp)

        if len(ret) != 0:
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                JKVW_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe, pl, cartype, fdjandbsx, carxing, zpgc, year,company,type_q = jkVM(sVIN)
                sres = sres + line+ '\t' + sVIN + '\t' + 'JKVW' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
            else:
                pass
                # #print ret[0][1]
    elif li[0] == 'BIO030-CAR_VIN_YQVW':
        ret = re.findall(pat_YQVW, data_tmp)

        if len(ret) != 0:
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                YQVW_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe,pl, cartype, fdjandbsx, carxing, zpgc,year = yqVM(sVIN)
                ##print namestr+'\t'+phonestr+'\t'+addrstr+'\t'+longstr+'\t'+latstr+'\t'+sfznum+'\t'+carnum+ '\n'
                try:
                    sres = sres + line +'\t'+sVIN+ '\t'+'YQVW'+'\t'+country + '\t' + '中国一汽大众汽车有限公司' + '\t' + '*' +'\t'+pl + '\t'+safe+'\t'+cartype+'\t'+fdjandbsx +'\t'+carxing + '\t'+str(year) + '\t'+zpgc+ '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                except:
                    sres = sres + line+ '\t' + sVIN + '\t' + 'YQVW' + '\t' + country + '\t' + '中国一汽大众汽车有限公司' + '\t' + '*' + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t' + host + '\t' + pingtaistr + '\t' + liulanqistr + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\n'
                return sres
            else:
                pass
    elif li[0] == 'BIO030-CAR_VIN_GZBT':
        ret = re.findall(pat_GZBT, data_tmp)
        if len(ret) != 0:
            ##print 'CAR_VIN_GZBT'
            ##print ret
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                GZBT_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, type_q = gzBT(sVIN)
                sres = sres + line+ '\t' + sVIN + '\t' + 'GZBT' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
            else:
                pass
                # #print ret[0][1]
    elif li[0] == 'BIO030-CAR_VIN_BJXD':
        ret = re.findall(pat_BJXD, data_tmp)
        if len(ret) != 0:
            ##print 'CAR_VIN_BJXD'
            ##print ret
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                BJXD_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, type_q = bjXD(sVIN)
                sres = sres + line+ '\t' + sVIN + '\t' + 'BJXD' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
    elif li[0] == 'BIO030-CAR_VIN_MGTY':
        ret = re.findall(pat_MGTY, data_tmp)
        if len(ret) != 0:
            ##print 'CAR_VIN_MGTY:'
            ##print ret
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                MGTY_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, type_q = mgGM(sVIN)
                mgTY_ytype += 1
                sres = sres + line+ '\t' + sVIN + '\t' + 'MGTY' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
    elif li[0] == 'BIO030-CAR_VIN_BSJ':
        ret = re.findall(pat_BSJ, data_tmp)
        if len(ret) != 0:
            ##print 'CAR_VIN_BSJ:'
            ##print ret
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                BSJ_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, type_q = dgBSJ(sVIN)
                sres = sres + line+ '\t' + sVIN + '\t' + 'BSJ' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
    elif li[0] == 'BIO030-CAR_VIN_JKLH':
        ret = re.findall(pat_JKLH, data_tmp)
        if len(ret) != 0:
            ##print 'CAR_VIN_JKLH:'
            ##print ret
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                JKLH_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, type_q = ygLH(sVIN)
                sres = sres + line + '\t' + sVIN + '\t' + 'JKLH' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
    elif li[0] == 'BIO030-CAR_VIN_GQCQ':
        ret = re.findall(pat_GQCQ, data_tmp)
        if len(ret) != 0:
            ##print 'CAR_VIN_JKLH:'
            ##print ret
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                GQCQ_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, type_q = gqcq(sVIN)
                sres = sres + line+ '\t' + sVIN + '\t' + 'GQCQ' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
    elif li[0] == 'BIO030-CAR_VIN_JL':
        ret = re.findall(pat_jl_1, data_tmp)
        jl_num += 1
        istrue = False
        if len(ret) != 0:
            # #print 'CAR_VIN_GCBMW:'
            # #print ret
            tempret = 0
            vin_li = []
            for one in ret:
                if one[1] not in vin_li:
                    vin_li.append(one[1])
                # #print one[1]
            # #print vin_li
            for one in vin_li:
                # #print one
                resC = checkVIN(one)
                if resC == True:
                    if istrue == False:
                        jl_nums += 1
                    if vin_str == '':
                        vin_str = one
                    else:
                        vin_str = vin_str + ';' + one
                    istrue = True

                    sVIN = one
                    # #print sVIN
                    country = scCountry(sVIN[0])
                    year = getYear(sVIN[9])
                    safe1, pl1, cartype1, fdjandbsx1, carxing1, zpgc1, year1, company1, type_q1 = jl1(sVIN)
                    if tempret == 0:
                        safe = safe1
                        pl = pl1
                        cartype = cartype1
                        fdjandbsx = fdjandbsx1
                        carxing = carxing1
                        zpgc = zpgc1
                        year = str(year1)
                        company = company1
                        type_q = type_q1
                    else:

                        safe = safe + ';' + safe1
                        pl = pl + ';' + pl1
                        cartype = cartype + ';' + cartype1
                        fdjandbsx = fdjandbsx + ';' + fdjandbsx1
                        carxing = carxing + ';' + carxing1
                        zpgc = zpgc + ';' + zpgc1
                        year = str(year) + ';' + str(year1)
                        company = company + ';' + company1
                        type_q = type_q + ';' + type_q1
                    tempret += 1
                else:
                    pass
            if istrue == True:
                sres = sres + line+ '\t' + vin_str + '\t' + 'JL' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(
                    year) + '\t' + zpgc + '\t' + bkj_str_th(host) + '\t' + bkj_str_th(
                    pingtaistr) + '\t' + bkj_str_th(
                    liulanqistr) + '\t' + bkj_str_th(namestr) + '\t' + bkj_str_th(phonestr) + '\t' + bkj_str_th(
                    addrstr) + '\t' + bkj_str_th(longlat) + '\t' + bkj_str_th(sfznum) + '\t' + bkj_str_th(
                    carnum) + '\t' + platestr + '\n'
                return sres
        else:
            ret = re.findall(pat_jl_2, data_tmp)
            istrue = False
            if len(ret) != 0:
                tempret = 0
                vin_li = []
                for one in ret:
                    if one[1] not in vin_li:
                        vin_li.append(one[1])
                for one in vin_li:
                    resC = checkVIN(one)
                    if resC == True:
                        if istrue == False:
                            jl_nums += 1
                        if vin_str == '':
                            vin_str = one
                        else:
                            vin_str = vin_str + ';' + one
                        istrue = True
                        sVIN = one
                        # #print sVIN
                        ##print sVIN
                        country = scCountry(sVIN[0])
                        year = getYear(sVIN[9])
                        safe1, pl1, cartype1, fdjandbsx1, carxing1, zpgc1, year1, company1, type_q1 = jl2(sVIN)
                        if tempret == 0:
                            safe = safe1
                            pl = pl1
                            cartype = cartype1
                            fdjandbsx = fdjandbsx1
                            carxing = carxing1
                            zpgc = zpgc1
                            year = str(year1)
                            company = company1
                            type_q = type_q1
                        else:
                            safe = safe + ';' + safe1
                            pl = pl + ';' + pl1
                            cartype = cartype + ';' + cartype1
                            fdjandbsx = fdjandbsx + ';' + fdjandbsx1
                            carxing = carxing + ';' + carxing1
                            zpgc = zpgc + ';' + zpgc1
                            year = str(year) + ';' + str(year1)
                            company = company + ';' + company1
                            type_q = type_q + ';' + type_q1
                        tempret += 1
                    else:
                        pass
                if istrue == True:
                    sres = sres + line+ '\t' + vin_str + '\t' + 'JL2' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(
                        year) + '\t' + zpgc + '\t' + bkj_str_th(host) + '\t' + bkj_str_th(
                        pingtaistr) + '\t' + bkj_str_th(
                        liulanqistr) + '\t' + bkj_str_th(namestr) + '\t' + bkj_str_th(
                        phonestr) + '\t' + bkj_str_th(
                        addrstr) + '\t' + bkj_str_th(longlat) + '\t' + bkj_str_th(sfznum) + '\t' + bkj_str_th(
                        carnum) + '\t' + platestr + '\n'
                    return sres
    elif li[0] == 'BIO030-CAR_VIN_JKRC':
        ret = re.findall(pat_jkrc_2, data_tmp)
        jkrc_num += 1
        istrue = False
        if len(ret) != 0:
            # #print 'CAR_VIN_GCBMW:'
            # #print ret
            tempret = 0
            vin_li = []
            for one in ret:
                if one[1] not in vin_li:
                    vin_li.append(one[1])
                # #print one[1]
            for one in vin_li:
                resC = checkVIN(one)
                if resC == True:
                    if istrue == False:
                        jkrc2_nums += 1
                    if vin_str == '':
                        vin_str = one
                    else:
                        vin_str = vin_str + ';' + one
                    istrue = True

                    sVIN = one
                    # #print sVIN
                    country = scCountry(sVIN[0])
                    year = getYear(sVIN[9])
                    safe1, pl1, cartype1, fdjandbsx1, carxing1, zpgc1, year1, company1, type_q1 = jkRC_WX(
                        sVIN)
                    if tempret == 0:
                        safe = safe1
                        pl = pl1
                        cartype = cartype1
                        fdjandbsx = fdjandbsx1
                        carxing = carxing1
                        zpgc = zpgc1
                        year = str(year1)
                        company = company1
                        type_q = type_q1
                    else:
                        safe = safe + ';' + safe1
                        pl = pl + ';' + pl1
                        cartype = cartype + ';' + cartype1
                        fdjandbsx = fdjandbsx + ';' + fdjandbsx1
                        carxing = carxing + ';' + carxing1
                        zpgc = zpgc + ';' + zpgc1
                        year = str(year) + ';' + str(year1)
                        company = company + ';' + company1
                        type_q = type_q + ';' + type_q1
                    tempret += 1
                else:
                    pass
            if istrue == True:
                sres = sres + line+ '\t' + vin_str + '\t' + 'JKRC_WX' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(
                    year) + '\t' + zpgc + '\t' + bkj_str_th(host) + '\t' + bkj_str_th(
                    pingtaistr) + '\t' + bkj_str_th(
                    liulanqistr) + '\t' + bkj_str_th(namestr) + '\t' + bkj_str_th(
                    phonestr) + '\t' + bkj_str_th(
                    addrstr) + '\t' + bkj_str_th(longlat) + '\t' + bkj_str_th(sfznum) + '\t' + bkj_str_th(
                    carnum) + '\t' + platestr + '\n'
                return sres
        else:
            ret = re.findall(pat_jkrc_1, data_tmp)
            
            istrue = False
            if len(ret) != 0:
                # #print 'CAR_VIN_GCBMW:'
                # #print ret
                tempret = 0
                vin_li = []
                for one in ret:
                    if one[1] not in vin_li:
                        vin_li.append(one[1])
                    # #print one[1]
                for one in vin_li:
                    resC = checkVIN(one)
                    if resC == True:
                        if istrue == False:
                            jkrc1_nums += 1
                        if vin_str == '':
                            vin_str = one
                        else:
                            vin_str = vin_str + ';' + one
                        istrue = True

                        sVIN = one
                        # #print sVIN
                        country = scCountry(sVIN[0])
                        year = getYear(sVIN[9])
                        safe1, pl1, cartype1, fdjandbsx1, carxing1, zpgc1, year1, company1, type_q1 = jkRC(sVIN)
                        if tempret == 0:
                            safe = safe1
                            pl = pl1
                            cartype = cartype1
                            fdjandbsx = fdjandbsx1
                            carxing = carxing1
                            zpgc = zpgc1
                            year = str(year1)
                            company = company1
                            type_q = type_q1
                        else:
                            safe = safe + ';' + safe1
                            pl = pl + ';' + pl1
                            cartype = cartype + ';' + cartype1
                            fdjandbsx = fdjandbsx + ';' + fdjandbsx1
                            carxing = carxing + ';' + carxing1
                            zpgc = zpgc + ';' + zpgc1
                            year = str(year) + ';' + str(year1)
                            company = company + ';' + company1
                            type_q = type_q + ';' + type_q1
                        tempret += 1
                    else:
                        pass
                if istrue == True:
                    sres = sres + line+ '\t' + vin_str + '\t' + 'JKRC' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(
                        year) + '\t' + zpgc + '\t' + bkj_str_th(host) + '\t' + bkj_str_th(
                        pingtaistr) + '\t' + bkj_str_th(
                        liulanqistr) + '\t' + bkj_str_th(namestr) + '\t' + bkj_str_th(phonestr) + '\t' + bkj_str_th(
                        addrstr) + '\t' + bkj_str_th(longlat) + '\t' + bkj_str_th(sfznum) + '\t' + bkj_str_th(
                        carnum) + '\t' + platestr + '\n'
                    return sres
    elif li[0] == 'BIO030-CAR_VIN_JKBT':
        ret = re.findall(pat_jkbt_2, data_tmp)
        jkbt_num += 1
        istrue = False
        if len(ret) != 0:
            # #print 'CAR_VIN_GCBMW:'
            # #print ret
            tempret = 0
            vin_li = []
            for one in ret:
                if one[1] not in vin_li:
                    vin_li.append(one[1])
                # #print one[1]
            for one in vin_li:
                resC = checkVIN(one)
                if resC == True:
                    if istrue == False:
                        jkbt1_nums += 1
                    if vin_str == '':
                        vin_str = one
                    else:
                        vin_str = vin_str + ';' + one
                    istrue = True
                    sVIN = one
                    # #print sVIN
                    country = scCountry(sVIN[0])
                    year = getYear(sVIN[9])
                    safe1, pl1, cartype1, fdjandbsx1, carxing1, zpgc1, year1, company1, type_q1 = jkBT_akl(sVIN)
                    if tempret == 0:
                        safe = safe1
                        pl = pl1
                        cartype = cartype1
                        fdjandbsx = fdjandbsx1
                        carxing = carxing1
                        zpgc = zpgc1
                        year = str(year1)
                        company = company1
                        type_q = type_q1
                    else:
                        safe = safe + ';' + safe1
                        pl = pl + ';' + pl1
                        cartype = cartype + ';' + cartype1
                        fdjandbsx = fdjandbsx + ';' + fdjandbsx1
                        carxing = carxing + ';' + carxing1
                        zpgc = zpgc + ';' + zpgc1
                        year = str(year) + ';' + str(year1)
                        company = company + ';' + company1
                        type_q = type_q + ';' + type_q1
                    tempret += 1
                else:
                    pass
            if istrue == True:
                sres = sres + line+ '\t' + vin_str + '\t' + 'JKBT_ACURA' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(
                    year) + '\t' + zpgc + '\t' + bkj_str_th(host) + '\t' + bkj_str_th(
                    pingtaistr) + '\t' + bkj_str_th(
                    liulanqistr) + '\t' + bkj_str_th(namestr) + '\t' + bkj_str_th(phonestr) + '\t' + bkj_str_th(
                    addrstr) + '\t' + bkj_str_th(longlat) + '\t' + bkj_str_th(sfznum) + '\t' + bkj_str_th(
                    carnum) + '\t' + platestr + '\n'
                return sres
        else:
            ret = re.findall(pat_jkbt_1, data_tmp)
            istrue = False
            if len(ret) != 0:
                # #print 'CAR_VIN_GCBMW:'
                # #print ret
                tempret = 0
                vin_li = []
                for one in ret:
                    if one[1] not in vin_li:
                        vin_li.append(one[1])
                    # #print one[1]
                for one in vin_li:
                    resC = checkVIN(one)
                    if resC == True:
                        if istrue == False:
                            jkbt2_nums += 1
                        if vin_str == '':
                            vin_str = one
                        else:
                            vin_str = vin_str + ';' + one
                        istrue = True
                        sVIN = one
                        # #print sVIN
                        country = scCountry(sVIN[0])
                        year = getYear(sVIN[9])
                        safe1, pl1, cartype1, fdjandbsx1, carxing1, zpgc1, year1, company1, type_q1 = jkBT(sVIN)
                        if tempret == 0:
                            safe = safe1
                            pl = pl1
                            cartype = cartype1
                            fdjandbsx = fdjandbsx1
                            carxing = carxing1
                            zpgc = zpgc1
                            year = str(year1)
                            company = company1
                            type_q = type_q1
                        else:
                            safe = safe + ';' + safe1
                            pl = pl + ';' + pl1
                            cartype = cartype + ';' + cartype1
                            fdjandbsx = fdjandbsx + ';' + fdjandbsx1
                            carxing = carxing + ';' + carxing1
                            zpgc = zpgc + ';' + zpgc1
                            year = str(year) + ';' + str(year1)
                            company = company + ';' + company1
                            type_q = type_q + ';' + type_q1
                        tempret += 1
                    else:
                        pass
                if istrue == True:
                    sres = sres + line+ '\t' + vin_str + '\t' + 'JKBT' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(
                        year) + '\t' + zpgc + '\t' + bkj_str_th(host) + '\t' + bkj_str_th(
                        pingtaistr) + '\t' + bkj_str_th(
                        liulanqistr) + '\t' + bkj_str_th(namestr) + '\t' + bkj_str_th(
                        phonestr) + '\t' + bkj_str_th(
                        addrstr) + '\t' + bkj_str_th(longlat) + '\t' + bkj_str_th(sfznum) + '\t' + bkj_str_th(
                        carnum) + '\t' + platestr + '\n'
                    return sres
    elif li[0] == 'BIO030-CAR_VIN_JKMZD':
        ret = re.findall(pat_jkmzd, data_tmp)
        jkmzd_num += 1
        istrue = False
        if len(ret) != 0:
            # #print 'CAR_VIN_GCBMW:'
            # #print ret
            tempret = 0
            vin_li = []
            for one in ret:
                if one[1] not in vin_li:
                    vin_li.append(one[1])
                # #print one[1]
            for one in vin_li:
                resC = checkVIN(one)
                if resC == True:
                    if istrue == False:
                        jkmzd_nums += 1
                    if vin_str == '':
                        vin_str = one
                    else:
                        vin_str = vin_str + ';' + one
                    istrue = True
                    sVIN = one
                    # #print sVIN
                    country = scCountry(sVIN[0])
                    year = getYear(sVIN[9])
                    safe1, pl1, cartype1, fdjandbsx1, carxing1, zpgc1, year1, company1, type_q1 = jkMZD(sVIN)
                    if tempret == 0:
                        safe = safe1
                        pl = pl1
                        cartype = cartype1
                        fdjandbsx = fdjandbsx1
                        carxing = carxing1
                        zpgc = zpgc1
                        year = str(year1)
                        company = company1
                        type_q = type_q1
                    else:
                        safe = safe + ';' + safe1
                        pl = pl + ';' + pl1
                        cartype = cartype + ';' + cartype1
                        fdjandbsx = fdjandbsx + ';' + fdjandbsx1
                        carxing = carxing + ';' + carxing1
                        zpgc = zpgc + ';' + zpgc1
                        year = str(year) + ';' + str(year1)
                        company = company + ';' + company1
                        type_q = type_q + ';' + type_q1
                    tempret += 1
                else:
                    pass
            if istrue == True:
                sres = sres + line+ '\t' + vin_str + '\t' + 'JKMZD' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(
                    year) + '\t' + zpgc + '\t' + bkj_str_th(host) + '\t' + bkj_str_th(
                    pingtaistr) + '\t' + bkj_str_th(
                    liulanqistr) + '\t' + bkj_str_th(namestr) + '\t' + bkj_str_th(phonestr) + '\t' + bkj_str_th(
                    addrstr) + '\t' + bkj_str_th(longlat) + '\t' + bkj_str_th(sfznum) + '\t' + bkj_str_th(
                    carnum) + '\t' + platestr + '\n'
                return sres
    else:
        return ""
    if li[0] == 'BIO030-CAR_VIN_GCBMW':
        ret = re.findall(pat_GCBMW, data_tmp)

        if len(ret) != 0:
            ##print 'CAR_VIN_GCBMW:'
            ##print ret
            resC = checkVIN(ret[0][1])
            if resC == True:
                GCBMW_nums += 1
                nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                year = getYear(sVIN[9])
                sres = sres + line+ '\t' + sVIN + '\t' + 'GCBMW' + '\t' + country + '\t' +'*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*'+ '\t' + '*' + '\t' + '*' + '\t' + str(year) + '\t' + '*' + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
            else:
                pass
                ##print ret[0][1]
    elif li[0] == 'BIO030-CAR_VIN_JKBMW':
        tests+=1
        ret = re.findall(pat_JKBMW, data_tmp)

        ##print ret
        if len(ret) != 0:
            ##print 'CAR_VIN_JKBMW:'
            ##print ret
            resC = checkVIN(ret[0][1])
            ##print sums
            if resC == True:
                ##print sums
                nums += 1
                JKBMW_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe, pl, cartype, fdjandbsx, carxing, zpgc, year = jkBWM(sVIN)
                sres = sres + line+ '\t' + sVIN + '\t' + 'JKBWM' + '\t' + country + '\t' + '德国宝马汽车公司' + '\t' + '*' + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
            else:
                pass
                ##print ret[0][1]
    #未解析
    elif li[0] == 'BIO030-CAR_VIN_GCBENZ':
        ret = re.findall(pat_GCBENZ, data_tmp)
        if len(ret) != 0:
            ##print 'CAR_VIN_GCBENZ'
            ##print ret
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                GCBENZ_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                year = getYear(sVIN[9])
                sres = sres + line+ '\t' + sVIN + '\t' + 'GCBENZ' + '\t' + country + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + str(year) + '\t' + '*' + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
            else:
                pass
                # #print ret[0][1]
    elif li[0] == 'BIO030-CAR_VIN_JKBENZ':
        ret = re.findall(pat_JKBENZ, data_tmp)
        if len(ret) != 0:
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                JKBENZ_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe, pl, cartype, fdjandbsx, carxing, zpgc, year = jkBENZ(sVIN)
                sres = sres + line+ '\t' + sVIN + '\t' + 'JKBENZ' + '\t' + country + '\t' +'德国梅赛德斯-奔驰汽车公司' + '\t' + '*' + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
            else:
                pass
                # #print ret[0][1]
    elif li[0] == 'BIO030-CAR_VIN_JKTOYOTA':
        ret = re.findall(pat_jktoyota_lexus, data_tmp)
        istrue = False
        if len(ret) != 0:
            tempret = 0
            vin_li = []
            for one in ret:
                if one[1] not in vin_li:
                    vin_li.append(one[1])
            for one in vin_li:
                resC = checkVIN(one)
                if resC == True:
                    if istrue == False:
                        jktoyota_lexus_nums += 1
                    if vin_str == '':
                        vin_str = one
                    else:
                        vin_str = vin_str + ';' + one
                    istrue = True
                    sVIN = one
                    # #print sVIN
                    # #print sVIN
                    country = scCountry(sVIN[0])
                    year = getYear(sVIN[9])
                    safe1, pl1, cartype1, fdjandbsx1, carxing1, zpgc1, year1, company1, type_q1 = jkFT_LEXUS(sVIN)
                    if tempret == 0:
                        safe = safe1
                        pl = pl1
                        cartype = cartype1
                        fdjandbsx = fdjandbsx1
                        carxing = carxing1
                        zpgc = zpgc1
                        year = str(year1)
                        company = company1
                        type_q = type_q1
                    else:
                        safe = safe + ';' + safe1
                        pl = pl + ';' + pl1
                        cartype = cartype + ';' + cartype1
                        fdjandbsx = fdjandbsx + ';' + fdjandbsx1
                        carxing = carxing + ';' + carxing1
                        zpgc = zpgc + ';' + zpgc1
                        year = str(year) + ';' + str(year1)
                        company = company + ';' + company1
                        type_q = type_q + ';' + type_q1
                    tempret += 1
                else:
                    pass
            if istrue == True:
                sres = sres + line + '\t' + vin_str + '\t' + 'JKTOYOTA_LEXUS' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(
                    year) + '\t' + zpgc + '\t' + bkj_str_th(host) + '\t' + bkj_str_th(
                    pingtaistr) + '\t' + bkj_str_th(
                    liulanqistr) + '\t' + bkj_str_th(namestr) + '\t' + bkj_str_th(
                    phonestr) + '\t' + bkj_str_th(
                    addrstr) + '\t' + bkj_str_th(longlat) + '\t' + bkj_str_th(sfznum) + '\t' + bkj_str_th(
                    carnum) + '\t' + platestr + '\n'
                return sres
        else:
            ret = re.findall(pat_JKTOYOTA_1, data_tmp)
            if len(ret) != 0:
                resC = checkVIN(ret[0][1])
                if resC == True:
                    nums += 1
                    sVIN = ret[0][1]
                    JKTOYOTA_nums += 1
                    country = scCountry(sVIN[0])
                    safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, type_q = jkTOYOTA(sVIN)
                    sres = sres + line+ '\t' + sVIN + '\t' + 'JKTOYOTA' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                    return sres
                else:
                    pass
    #未解析
    elif li[0] == 'BIO030-CAR_VIN_GCTOYOTA':
        ret = re.findall(pat_GCTOYOTA, data_tmp)
        if len(ret) != 0:
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                year = getYear(sVIN[9])
                sres = sres + line + '\t' + sVIN + '\t' + 'GCTOYOTA' + '\t' + country + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + str(year) + '\t' + '*' + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
            else:
                pass
                # #print ret[0][1]
    elif li[0] == 'BIO030-CAR_VIN_YQTOYOTA':
        ret = re.findall(pat_YQTOYOTA, data_tmp)
        if len(ret) != 0:
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1

                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                year = getYear(sVIN[9])
                sres = sres + line+ '\t' + sVIN + '\t' + 'YQTOYOTA' + '\t' + country + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + str(year) + '\t' + '*' + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
            else:
                pass
                # #print ret[0][1]
    elif li[0] == 'BIO030-CAR_VIN_SHVW':
        ret = re.findall(pat_SHVW, data_tmp)

        if len(ret) != 0:
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                SHVW_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe, pl, cartype, fdjandbsx, carxing, zpgc, year = shVM(sVIN)
                sres = sres + line+ '\t' + sVIN + '\t' + 'SHVW' + '\t' + country + '\t' +  '中国上海大众汽车有限公司' + '\t' + '*' + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
            else:
                pass
                # #print ret[0][1]
    elif li[0] == 'BIO030-CAR_VIN_JKVW':
        ret = re.findall(pat_JKVW, data_tmp)

        if len(ret) != 0:
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                JKVW_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe, pl, cartype, fdjandbsx, carxing, zpgc, year,company,type_q = jkVM(sVIN)
                sres = sres + line+ '\t' + sVIN + '\t' + 'JKVW' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
            else:
                pass
                # #print ret[0][1]
    elif li[0] == 'BIO030-CAR_VIN_YQVW':
        ret = re.findall(pat_YQVW, data_tmp)

        if len(ret) != 0:
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                YQVW_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe,pl, cartype, fdjandbsx, carxing, zpgc,year = yqVM(sVIN)
                ##print namestr+'\t'+phonestr+'\t'+addrstr+'\t'+longstr+'\t'+latstr+'\t'+sfznum+'\t'+carnum+ '\n'
                try:
                    sres = sres + line +'\t'+sVIN+ '\t'+'YQVW'+'\t'+country + '\t' + '中国一汽大众汽车有限公司' + '\t' + '*' +'\t'+pl + '\t'+safe+'\t'+cartype+'\t'+fdjandbsx +'\t'+carxing + '\t'+str(year) + '\t'+zpgc+ '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                except:
                    sres = sres + line + '\t' + sVIN + '\t' + 'YQVW' + '\t' + country + '\t' + '中国一汽大众汽车有限公司' + '\t' + '*' + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(
                        year) + '\t' + zpgc + '\t' + host + '\t' + pingtaistr + '\t' + liulanqistr + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\t' + '*' + '\n'
                return sres
            else:
                pass
    elif li[0] == 'BIO030-CAR_VIN_GZBT':
        ret = re.findall(pat_GZBT, data_tmp)
        if len(ret) != 0:
            ##print 'CAR_VIN_GZBT'
            ##print ret
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                GZBT_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, type_q = gzBT(sVIN)
                sres = sres + line+ '\t' + sVIN + '\t' + 'GZBT' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
            else:
                pass
                # #print ret[0][1]
    elif li[0] == 'BIO030-CAR_VIN_BJXD':
        ret = re.findall(pat_BJXD, data_tmp)
        if len(ret) != 0:
            ##print 'CAR_VIN_BJXD'
            ##print ret
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                BJXD_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, type_q = bjXD(sVIN)
                sres = sres + line+ '\t' + sVIN + '\t' + 'BJXD' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
    elif li[0] == 'BIO030-CAR_VIN_MGTY':
        ret = re.findall(pat_MGTY, data_tmp)
        if len(ret) != 0:
            ##print 'CAR_VIN_MGTY:'
            ##print ret
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                MGTY_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, type_q = mgGM(sVIN)
                mgTY_ytype += 1
                sres = sres + line+ '\t' + sVIN + '\t' + 'MGTY' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
    elif li[0] == 'BIO030-CAR_VIN_BSJ':
        ret = re.findall(pat_BSJ, data_tmp)
        if len(ret) != 0:
            ##print 'CAR_VIN_BSJ:'
            ##print ret
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                BSJ_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, type_q = dgBSJ(sVIN)
                sres = sres + line+ '\t' + sVIN + '\t' + 'BSJ' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
    elif li[0] == 'BIO030-CAR_VIN_JKLH':
        ret = re.findall(pat_JKLH, data_tmp)
        if len(ret) != 0:
            ##print 'CAR_VIN_JKLH:'
            ##print ret
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                JKLH_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, type_q = ygLH(sVIN)
                sres = sres + line+ '\t' + sVIN + '\t' + 'JKLH' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
    elif li[0] == 'BIO030-CAR_VIN_GQCQ':
        ret = re.findall(pat_GQCQ, data_tmp)
        if len(ret) != 0:
            ##print 'CAR_VIN_JKLH:'
            ##print ret
            resC = checkVIN(ret[0][1])
            if resC == True:
                nums += 1
                GQCQ_nums += 1
                sVIN = ret[0][1]
                country = scCountry(sVIN[0])
                safe, pl, cartype, fdjandbsx, carxing, zpgc, year, company, type_q = gqcq(sVIN)
                sres = sres + line+ '\t' + sVIN + '\t' + 'GQCQ' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(year) + '\t' + zpgc + '\t'+host.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+pingtaistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+liulanqistr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+namestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+phonestr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+addrstr.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+longlat.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+sfznum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+carnum.strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\x01','').replace('\x00','').replace('\x02','').replace('\x03','').replace('\x04','').replace('\x05','').replace('\x06','').replace('\x07','').replace('\x08','').replace('\x09','').replace('\x0a','').replace('\x0b','').replace('\x0c','').replace('\x0d','').replace('\x0e','').replace('\x0f','').replace('\x10','').replace('\x11','').replace('\x12','').replace('\x13','').replace('\x14','').replace('\x15','').replace('\x16','').replace('\x17','').replace('\x18','').replace('\x19','').replace('\x1a','').replace('\x1b','').replace('\x1c','').replace('\x1d','').replace('\x1e','').replace('\x1f','').replace('\x7f','')+'\t'+platestr+ '\n'
                return sres
    elif li[0] == 'BIO030-CAR_VIN_JL':
        ret = re.findall(pat_jl_1, data_tmp)
        jl_num += 1
        istrue = False
        if len(ret) != 0:
            # #print 'CAR_VIN_GCBMW:'
            # #print ret
            tempret = 0
            vin_li = []
            for one in ret:
                if one[1] not in vin_li:
                    vin_li.append(one[1])
                # #print one[1]
            # #print vin_li
            for one in vin_li:
                # #print one
                resC = checkVIN(one)
                if resC == True:
                    if istrue == False:
                        jl_nums += 1
                    if vin_str == '':
                        vin_str = one
                    else:
                        vin_str = vin_str + ';' + one
                    istrue = True

                    sVIN = one
                    # #print sVIN
                    country = scCountry(sVIN[0])
                    year = getYear(sVIN[9])
                    safe1, pl1, cartype1, fdjandbsx1, carxing1, zpgc1, year1, company1, type_q1 = jl1(sVIN)
                    if tempret == 0:
                        safe = safe1
                        pl = pl1
                        cartype = cartype1
                        fdjandbsx = fdjandbsx1
                        carxing = carxing1
                        zpgc = zpgc1
                        year = str(year1)
                        company = company1
                        type_q = type_q1
                    else:

                        safe = safe + ';' + safe1
                        pl = pl + ';' + pl1
                        cartype = cartype + ';' + cartype1
                        fdjandbsx = fdjandbsx + ';' + fdjandbsx1
                        carxing = carxing + ';' + carxing1
                        zpgc = zpgc + ';' + zpgc1
                        year = str(year) + ';' + str(year1)
                        company = company + ';' + company1
                        type_q = type_q + ';' + type_q1
                    tempret += 1
                else:
                    pass
            if istrue == True:
                sres = sres + line+ '\t' + vin_str + '\t' + 'JL' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(
                    year) + '\t' + zpgc + '\t' + bkj_str_th(host) + '\t' + bkj_str_th(
                    pingtaistr) + '\t' + bkj_str_th(
                    liulanqistr) + '\t' + bkj_str_th(namestr) + '\t' + bkj_str_th(phonestr) + '\t' + bkj_str_th(
                    addrstr) + '\t' + bkj_str_th(longlat) + '\t' + bkj_str_th(sfznum) + '\t' + bkj_str_th(
                    carnum) + '\t' + platestr + '\n'
                return sres
        else:
            ret = re.findall(pat_jl_2, data_tmp)
            istrue = False
            if len(ret) != 0:
                tempret = 0
                vin_li = []
                for one in ret:
                    if one[1] not in vin_li:
                        vin_li.append(one[1])
                for one in vin_li:
                    resC = checkVIN(one)
                    if resC == True:
                        if istrue == False:
                            jl_nums += 1
                        if vin_str == '':
                            vin_str = one
                        else:
                            vin_str = vin_str + ';' + one
                        istrue = True
                        sVIN = one
                        # #print sVIN
                        ##print sVIN
                        country = scCountry(sVIN[0])
                        year = getYear(sVIN[9])
                        safe1, pl1, cartype1, fdjandbsx1, carxing1, zpgc1, year1, company1, type_q1 = jl2(sVIN)
                        if tempret == 0:
                            safe = safe1
                            pl = pl1
                            cartype = cartype1
                            fdjandbsx = fdjandbsx1
                            carxing = carxing1
                            zpgc = zpgc1
                            year = str(year1)
                            company = company1
                            type_q = type_q1
                        else:
                            safe = safe + ';' + safe1
                            pl = pl + ';' + pl1
                            cartype = cartype + ';' + cartype1
                            fdjandbsx = fdjandbsx + ';' + fdjandbsx1
                            carxing = carxing + ';' + carxing1
                            zpgc = zpgc + ';' + zpgc1
                            year = str(year) + ';' + str(year1)
                            company = company + ';' + company1
                            type_q = type_q + ';' + type_q1
                        tempret += 1
                    else:
                        pass
                if istrue == True:
                    sres = sres + line+ '\t' + vin_str + '\t' + 'JL2' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(
                        year) + '\t' + zpgc + '\t' + bkj_str_th(host) + '\t' + bkj_str_th(
                        pingtaistr) + '\t' + bkj_str_th(
                        liulanqistr) + '\t' + bkj_str_th(namestr) + '\t' + bkj_str_th(
                        phonestr) + '\t' + bkj_str_th(
                        addrstr) + '\t' + bkj_str_th(longlat) + '\t' + bkj_str_th(sfznum) + '\t' + bkj_str_th(
                        carnum) + '\t' + platestr + '\n'
                    return sres
    elif li[0] == 'BIO030-CAR_VIN_JKRC':
        ret = re.findall(pat_jkrc_2, data_tmp)
        jkrc_num += 1
        istrue = False
        if len(ret) != 0:
            # #print 'CAR_VIN_GCBMW:'
            # #print ret
            tempret = 0
            vin_li = []
            for one in ret:
                if one[1] not in vin_li:
                    vin_li.append(one[1])
                # #print one[1]
            for one in vin_li:
                resC = checkVIN(one)
                if resC == True:
                    if istrue == False:
                        jkrc2_nums += 1
                    if vin_str == '':
                        vin_str = one
                    else:
                        vin_str = vin_str + ';' + one
                    istrue = True

                    sVIN = one
                    # #print sVIN
                    country = scCountry(sVIN[0])
                    year = getYear(sVIN[9])
                    safe1, pl1, cartype1, fdjandbsx1, carxing1, zpgc1, year1, company1, type_q1 = jkRC_WX(
                        sVIN)
                    if tempret == 0:
                        safe = safe1
                        pl = pl1
                        cartype = cartype1
                        fdjandbsx = fdjandbsx1
                        carxing = carxing1
                        zpgc = zpgc1
                        year = str(year1)
                        company = company1
                        type_q = type_q1
                    else:
                        safe = safe + ';' + safe1
                        pl = pl + ';' + pl1
                        cartype = cartype + ';' + cartype1
                        fdjandbsx = fdjandbsx + ';' + fdjandbsx1
                        carxing = carxing + ';' + carxing1
                        zpgc = zpgc + ';' + zpgc1
                        year = str(year) + ';' + str(year1)
                        company = company + ';' + company1
                        type_q = type_q + ';' + type_q1
                    tempret += 1
                else:
                    pass
            if istrue == True:
                sres = sres + line+ '\t' + vin_str + '\t' + 'JKRC_WX' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(
                    year) + '\t' + zpgc + '\t' + bkj_str_th(host) + '\t' + bkj_str_th(
                    pingtaistr) + '\t' + bkj_str_th(
                    liulanqistr) + '\t' + bkj_str_th(namestr) + '\t' + bkj_str_th(
                    phonestr) + '\t' + bkj_str_th(
                    addrstr) + '\t' + bkj_str_th(longlat) + '\t' + bkj_str_th(sfznum) + '\t' + bkj_str_th(
                    carnum) + '\t' + platestr + '\n'
                return sres
        else:
            ret = re.findall(pat_jkrc_1, data_tmp)
            
            istrue = False
            if len(ret) != 0:
                # #print 'CAR_VIN_GCBMW:'
                # #print ret
                tempret = 0
                vin_li = []
                for one in ret:
                    if one[1] not in vin_li:
                        vin_li.append(one[1])
                    # #print one[1]
                for one in vin_li:
                    resC = checkVIN(one)
                    if resC == True:
                        if istrue == False:
                            jkrc1_nums += 1
                        if vin_str == '':
                            vin_str = one
                        else:
                            vin_str = vin_str + ';' + one
                        istrue = True

                        sVIN = one
                        # #print sVIN
                        country = scCountry(sVIN[0])
                        year = getYear(sVIN[9])
                        safe1, pl1, cartype1, fdjandbsx1, carxing1, zpgc1, year1, company1, type_q1 = jkRC(sVIN)
                        if tempret == 0:
                            safe = safe1
                            pl = pl1
                            cartype = cartype1
                            fdjandbsx = fdjandbsx1
                            carxing = carxing1
                            zpgc = zpgc1
                            year = str(year1)
                            company = company1
                            type_q = type_q1
                        else:
                            safe = safe + ';' + safe1
                            pl = pl + ';' + pl1
                            cartype = cartype + ';' + cartype1
                            fdjandbsx = fdjandbsx + ';' + fdjandbsx1
                            carxing = carxing + ';' + carxing1
                            zpgc = zpgc + ';' + zpgc1
                            year = str(year) + ';' + str(year1)
                            company = company + ';' + company1
                            type_q = type_q + ';' + type_q1
                        tempret += 1
                    else:
                        pass
                if istrue == True:
                    sres = sres + line+ '\t' + vin_str + '\t' + 'JKRC' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(
                        year) + '\t' + zpgc + '\t' + bkj_str_th(host) + '\t' + bkj_str_th(
                        pingtaistr) + '\t' + bkj_str_th(
                        liulanqistr) + '\t' + bkj_str_th(namestr) + '\t' + bkj_str_th(phonestr) + '\t' + bkj_str_th(
                        addrstr) + '\t' + bkj_str_th(longlat) + '\t' + bkj_str_th(sfznum) + '\t' + bkj_str_th(
                        carnum) + '\t' + platestr + '\n'
                    return sres
    elif li[0] == 'BIO030-CAR_VIN_JKBT':
        ret = re.findall(pat_jkbt_2, data_tmp)
        jkbt_num += 1
        istrue = False
        if len(ret) != 0:
            # #print 'CAR_VIN_GCBMW:'
            # #print ret
            tempret = 0
            vin_li = []
            for one in ret:
                if one[1] not in vin_li:
                    vin_li.append(one[1])
                # #print one[1]
            for one in vin_li:
                resC = checkVIN(one)
                if resC == True:
                    if istrue == False:
                        jkbt1_nums += 1
                    if vin_str == '':
                        vin_str = one
                    else:
                        vin_str = vin_str + ';' + one
                    istrue = True
                    sVIN = one
                    # #print sVIN
                    country = scCountry(sVIN[0])
                    year = getYear(sVIN[9])
                    safe1, pl1, cartype1, fdjandbsx1, carxing1, zpgc1, year1, company1, type_q1 = jkBT_akl(sVIN)
                    if tempret == 0:
                        safe = safe1
                        pl = pl1
                        cartype = cartype1
                        fdjandbsx = fdjandbsx1
                        carxing = carxing1
                        zpgc = zpgc1
                        year = str(year1)
                        company = company1
                        type_q = type_q1
                    else:
                        safe = safe + ';' + safe1
                        pl = pl + ';' + pl1
                        cartype = cartype + ';' + cartype1
                        fdjandbsx = fdjandbsx + ';' + fdjandbsx1
                        carxing = carxing + ';' + carxing1
                        zpgc = zpgc + ';' + zpgc1
                        year = str(year) + ';' + str(year1)
                        company = company + ';' + company1
                        type_q = type_q + ';' + type_q1
                    tempret += 1
                else:
                    pass
            if istrue == True:
                sres = sres + line+ '\t' + vin_str + '\t' + 'JKBT_ACURA' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(
                    year) + '\t' + zpgc + '\t' + bkj_str_th(host) + '\t' + bkj_str_th(
                    pingtaistr) + '\t' + bkj_str_th(
                    liulanqistr) + '\t' + bkj_str_th(namestr) + '\t' + bkj_str_th(phonestr) + '\t' + bkj_str_th(
                    addrstr) + '\t' + bkj_str_th(longlat) + '\t' + bkj_str_th(sfznum) + '\t' + bkj_str_th(
                    carnum) + '\t' + platestr + '\n'
                return sres
        else:
            ret = re.findall(pat_jkbt_1, data_tmp)
            istrue = False
            if len(ret) != 0:
                # #print 'CAR_VIN_GCBMW:'
                # #print ret
                tempret = 0
                vin_li = []
                for one in ret:
                    if one[1] not in vin_li:
                        vin_li.append(one[1])
                    # #print one[1]
                for one in vin_li:
                    resC = checkVIN(one)
                    if resC == True:
                        if istrue == False:
                            jkbt2_nums += 1
                        if vin_str == '':
                            vin_str = one
                        else:
                            vin_str = vin_str + ';' + one
                        istrue = True
                        sVIN = one
                        # #print sVIN
                        country = scCountry(sVIN[0])
                        year = getYear(sVIN[9])
                        safe1, pl1, cartype1, fdjandbsx1, carxing1, zpgc1, year1, company1, type_q1 = jkBT(sVIN)
                        if tempret == 0:
                            safe = safe1
                            pl = pl1
                            cartype = cartype1
                            fdjandbsx = fdjandbsx1
                            carxing = carxing1
                            zpgc = zpgc1
                            year = str(year1)
                            company = company1
                            type_q = type_q1
                        else:
                            safe = safe + ';' + safe1
                            pl = pl + ';' + pl1
                            cartype = cartype + ';' + cartype1
                            fdjandbsx = fdjandbsx + ';' + fdjandbsx1
                            carxing = carxing + ';' + carxing1
                            zpgc = zpgc + ';' + zpgc1
                            year = str(year) + ';' + str(year1)
                            company = company + ';' + company1
                            type_q = type_q + ';' + type_q1
                        tempret += 1
                    else:
                        pass
                if istrue == True:
                    sres = sres + line+ '\t' + vin_str + '\t' + 'JKBT' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(
                        year) + '\t' + zpgc + '\t' + bkj_str_th(host) + '\t' + bkj_str_th(
                        pingtaistr) + '\t' + bkj_str_th(
                        liulanqistr) + '\t' + bkj_str_th(namestr) + '\t' + bkj_str_th(
                        phonestr) + '\t' + bkj_str_th(
                        addrstr) + '\t' + bkj_str_th(longlat) + '\t' + bkj_str_th(sfznum) + '\t' + bkj_str_th(
                        carnum) + '\t' + platestr + '\n'
                    return sres
    elif li[0] == 'BIO030-CAR_VIN_JKMZD':
        ret = re.findall(pat_jkmzd, data_tmp)
        jkmzd_num += 1
        istrue = False
        if len(ret) != 0:
            # #print 'CAR_VIN_GCBMW:'
            # #print ret
            tempret = 0
            vin_li = []
            for one in ret:
                if one[1] not in vin_li:
                    vin_li.append(one[1])
                # #print one[1]
            for one in vin_li:
                resC = checkVIN(one)
                if resC == True:
                    if istrue == False:
                        jkmzd_nums += 1
                    if vin_str == '':
                        vin_str = one
                    else:
                        vin_str = vin_str + ';' + one
                    istrue = True
                    sVIN = one
                    # #print sVIN
                    country = scCountry(sVIN[0])
                    year = getYear(sVIN[9])
                    safe1, pl1, cartype1, fdjandbsx1, carxing1, zpgc1, year1, company1, type_q1 = jkMZD(sVIN)
                    if tempret == 0:
                        safe = safe1
                        pl = pl1
                        cartype = cartype1
                        fdjandbsx = fdjandbsx1
                        carxing = carxing1
                        zpgc = zpgc1
                        year = str(year1)
                        company = company1
                        type_q = type_q1
                    else:
                        safe = safe + ';' + safe1
                        pl = pl + ';' + pl1
                        cartype = cartype + ';' + cartype1
                        fdjandbsx = fdjandbsx + ';' + fdjandbsx1
                        carxing = carxing + ';' + carxing1
                        zpgc = zpgc + ';' + zpgc1
                        year = str(year) + ';' + str(year1)
                        company = company + ';' + company1
                        type_q = type_q + ';' + type_q1
                    tempret += 1
                else:
                    pass
            if istrue == True:
                sres = sres + line+ '\t' + vin_str + '\t' + 'JKMZD' + '\t' + country + '\t' + company + '\t' + type_q + '\t' + pl + '\t' + safe + '\t' + cartype + '\t' + fdjandbsx + '\t' + carxing + '\t' + str(
                    year) + '\t' + zpgc + '\t' + bkj_str_th(host) + '\t' + bkj_str_th(
                    pingtaistr) + '\t' + bkj_str_th(
                    liulanqistr) + '\t' + bkj_str_th(namestr) + '\t' + bkj_str_th(phonestr) + '\t' + bkj_str_th(
                    addrstr) + '\t' + bkj_str_th(longlat) + '\t' + bkj_str_th(sfznum) + '\t' + bkj_str_th(
                    carnum) + '\t' + platestr + '\n'
                return sres
    else:
        return ""
def isHex(d):
    if (d >= '0' and d <= '9') or (d >= 'A' and d <= 'F'):
        return True
    else:
        return False
def dealWithPart7(rdata):
    i = 0
    line=""
    #ret_li = ''
    while i < len(rdata):
        if rdata[i] == '\\':
            if i + 1 < len(rdata):
                if rdata[i + 1] == '\\':  # \\
                    line=line+'\\'
                else:  # \80
                    if i + 2 < len(rdata):
                        if isHex(rdata[i + 1]) and isHex(rdata[i + 2]):
                            wd = convertBin(rdata[i + 1], rdata[i + 2])
                            line=line+wd
                            i += 2
                        else:
                            line=line+rdata[i]
                            #fw.write(rdata[i])
                    else:  # \t\80
                        line=line+rdata[i]
                        #fw.write(rdata[i])
            else:
                line=line+rdata[i]
        else:
            line=line+rdata[i]
        i += 1
    line=bytes(line,'utf-8')
    return line
def convertBin(q, h):
    cc = '0x' + q + h
    num = int(cc, 16)
    return chr(num)
if __name__ == '__main__':
    line=carvin_preprocess("""BIO030-CAR_VIN_JL	188.64.207.40	47.110.175.169	1793	80	tcp	2023-02-28 00:00:09	eth_payload=E\00\01\DD\1C\95@\003\06\BF\05\BC@\CF(/n\AF\A9\07\01\00P!\CC\D8\BB\9D\D3\036P\18\FF\FF\E6Y\00\00GET*/tsp-ad/ecarx_ad_theme/vin/LB377U2W9NA101788*HTTP/1.1\0D\0AX-ENV-TYPE:*production\0D\0AX-APP-ID:*270047_advertising\0D\0AAuthorization:*NjIxMzA2NzUzMzJDMTc0REIwQUQ3RDY4M0UyOTlEM0E=\0D\0AAccept:*application/json;responseformat=3\0D\0AContent-type:*application/json\0D\0AX-AGENT-TYPE:*android\0D\0AX-DEVICE-TYPE:*ihu\0D\0AX-OPERATOR-CODE:*GEELY\0D\0AX-AGENT-VERSION:*5.1\0D\0AHost:*api.xchanger.cn\0D\0AConnection:*Keep-Alive\0D\0AAccept-Encoding:*gzip\0D\0AUser-Agent:*okhttp/3.12.1\0D\0A\0D\0A
    """)
    print("after process!")
    print(line)