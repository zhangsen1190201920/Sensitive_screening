# encoding: utf-8
import httplib
import codecs
import os
import json
import threading
import math
import socket
import struct
import re
import sys
from lxml import etree
import Queue
import hashlib
import random
import copy
import time
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
# from geoalchemy2 import Geometry
from sqlalchemy.sql import select
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pyspark.context import SparkContext
from pyspark.sql import SparkSession, SQLContext
SparkContext._ensure_initialized()
try:
    # Try to access HiveConf, it will raise exception if Hive is not added
    SparkContext._jvm.org.apache.hadoop.hive.conf.HiveConf()
    spark = SparkSession.builder.enableHiveSupport().getOrCreate()
except:
    spark = SparkSession.builder.getOrCreate()
    
#except py4j.protocol.Py4JError:
#    spark = SparkSession.builder.getOrCreate()
#except TypeError:
#    spark = SparkSession.builder.getOrCreate()

sc = spark.sparkContext
reload(sys)
sys.setdefaultencoding("utf-8")
from pyspark.sql import HiveContext
from pyspark.sql.types import Row
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import LongType

file2parse = sys.argv[1]

hive_database = 'a42167'
hive_table = 'kmlcontent'
hive_context = HiveContext(sc)
hive_context.sql('use {}'.format(hive_database))#使用的数据库名字
i = 1
try:
    data = hive_context.sql('select max(tag_id) from {}'.format(hive_table)).collect()
    print("***************"+data[0][0])
    i = int(data[0][0])
except:
    i = 1
lastid=open("/new_system/auto_res/1h/out/kml/lastest_tagid.txt","w+")
lastid.write(str(i))
lastid.flush()
lastid.close()


content_table_head = ["tag_id","tag","content","parent_tag_id","flow_id","fence_province","fence_city","fence_service","fence_fencename","fence_relation"]
flowinfo_table_head = ["event_name","flow_id","s_ip","d_ip","s_port","d_port","time","stream_size","file_name","server","user_agent","domain","scountry","sprovince","scity","ssource","scompany","sscence","dcountry","dprovince","dcity","dsource","dcompany","dscence","direction","batch","payload"]
tag2parse = ["kml","folder","document","placemark","point","coordinates","linestring","track","multigeometry","linearring","polygon","outerboundaryis","innerboundaryis",]
tagid_tag_map = {}
engine = create_engine('postgresql://postgres:admin123@10.128.131.81:5431/postgres', echo=False)
conn = engine.connect()
tablename = 'fencetable'

content_log = open("/new_system/auto_res/1h/out/kml/content_log.txt","w+")
parsed_kml = open("/new_system/auto_res/1h/out/kml/parsed_kml.txt",'w+')
tag_log = open("/new_system/auto_res/1h/out/kml/tag_log.txt","w+")
class KmlInfo():
    def __init__(self):
        self.line = "*" # 原始文件的内容
        self.event_name = '*' #事件名
        self.s_ip = '*'    #源IP
        self.d_ip = '*'   #目的IP
        self.s_port = '*'   #源端口
        self.d_port = '*'   #目的端口
        self.time = "*" # 时间

        self.stream_size = -1 #流的字节数
        self.payload = "*" #负载
        self.file_name = "*" # 返回文件名
        self.server = "*" #服务器类型
        self.user_agent = "*" # 客户端类型
        self.domain = "*" # 主机ip或者域名
        self.flow_id = "*" #流ID

        self.scountry = "*" # 源国家
        self.sprovince = "*" # 源省份
        self.scity = "*" #源城市
        self.ssource = "*" # sip定位来源
        self.scompany = "*" # 源用户
        self.sscence = "*" # 源应用场景

        self.dcountry = "*" #目的国家
        self.dprovince = "*" # 目的省份
        self.dcity = "*" #目的城市
        self.dsource = "*" #dip定位来源
        self.dcompany = "*" #目的用户
        self.dscence = "*" #目的应用场景

        self.direction = "*" #流向
        self.batch = "*" #批次
        self.content = [] # type:[{}]
        self.latest_id = 0

    def fill_info(self,line):
        self.line = line
        items = line.strip().split("\t")
        self.event_name = items[0] 
        self.s_ip = items[1]    
        self.d_ip = items[2]   
        self.s_port = items[3]   
        self.d_port = items[4]   
        self.time = items[5]
        self.stream_size = items[8]
        self.payload = items[9]

        self.scountry = items[12]
        
        self.sprovince = items[13]
        self.scity = items[14]
        self.ssource = items[15]
        self.scompany = items[16]
        self.sscence = items[17]

        self.dcountry = items[18]
        self.dprovince = items[19]
        self.dcity = items[20]
        self.dsource = items[21]
        self.dcompany = items[22]
        self.dscence = items[23]

        self.direction = items[24]
        self.batch = items[25]

        self.cal_flow_id()
        self.parse_flow_info()
        self.parse_kml_content()
        self.fetch_fence_info()
        # print 1
        

    def toContentString(self):
        s = ""
        for mmap in self.content:
            for key in content_table_head:
                s = s+str(mmap[key])+"\t"
            s+="\n"
        return s.strip()+"\n"
    def toFlowInfoString(self):
        s = ""
        for key in flowinfo_table_head:
            s = s + str(getattr(self,key)).replace("  ","")+"\t"
        return s.strip()+"\n"

    def preprocess(self,line):
        # try:
        #     self.line = self.line+str(time.time())
        # except Exception as e:
        #     print(e)
        line = line.replace("&lt;","<")
        line = line.replace("&gt;",">")
        line = line.replace("&quot;","\"")
        line = line.replace("&amp;","&")
        line = line.replace("<br>","")
        line = re.sub(r"<description>[\s\S]*?</description>","",line)
        line = re.sub(r"<!--[\s\S]*?-->","",line)
        line = re.sub(r"<!\[CDATA\[[\s\S]*?\]\]>","",line)
        # line = re.sub(r"...0A[\\|\s][\s\S]*?<","<",line)
        # line = re.sub(r"...0D[\\|\s][\s\S]*?<","<",line)
        line = re.sub(r"\\[0-9a-zA-Z]{2}","  ",line)
        return line

    def parse_flow_info(self):
        user_agent_pattern = re.compile(r"User-Agent: ([\s\S]*?)  ")
        server_pattern = re.compile(r"Server: ([\s\S]*?)  ")
        filename = re.compile(r'filename=\"(.*?)\"')

        user_agent = re.findall(user_agent_pattern,self.payload)
        if len(user_agent)!=0:
            self.user_agent = user_agent[0]
        
        server = re.findall(server_pattern,self.payload)
        if len(server)!=0:
            self.server = server[0]
            if "**" in self.server or len(self.server)>20:
                self.server = "*"

        
        filename = re.findall(filename,self.payload)
        if len(filename)!=0:
            self.file_name = filename[0]
    def parse_kml_content(self):
        self.payload = re.sub(r"  "," ",self.payload)
        kml_pattern = re.compile(r"<kml[\s\S]*?>[\s\S]*?</kml>")
        kml_strs = re.findall(kml_pattern,self.payload)
        
        for i in range(len(kml_strs)):
            # print("after:"+kml_strs[i])
            if kml_strs[i]=="*":
                print("empty")
            root = object()
            try:
                root = etree.fromstring(kml_strs[i])
                parsed_kml.write(etree.tostring(root,pretty_print=True))
                parsed_kml.write('\n')
                parent_id = 0
                tag_id = self.get_latest_tagid()
                node_tagid_map = {}
                q = Queue.Queue(10000)
                q.put(root)
                while(not q.empty()):
                    # level_size = q.qsize()
                    node = q.get()
                    if(node==root): 
                        self.append_node(node,tag_id,0)
                    else:
                        parent = node.xpath('..')[0]
                        self.append_node(node,tag_id,node_tagid_map[parent])
                        # content_log.write("node_tag:{}".format(self.get_tag(node)))
                    node_tagid_map[node] = tag_id
                    tag_id+=1
                    children = node.xpath('./*')
                    for child in children:
                        # tag_log.write(self.get_tag(child)+"\n")
                        if self.need_parse(self.get_tag(child)):
                            q.put(child)
                            # tag_log.write("putted:{}\n".format(self.get_tag(child)))
                # lastid = open("/new_system/auto_res/1h/out/kml/lastest_tagid.txt","w")
                # lastid.write(str(tag_id))
                # lastid.flush() 
                # lastid.close() 
                self.latest_id = tag_id    
            except Exception as e:
                # 暂时跳过解析失败的数据
                if e.__class__==KeyboardInterrupt:
                    raise KeyboardInterrupt
                else:
                    content_log.write("数据内容格式错误,解析失败:{}\n".format(e))
                    continue
    def append_node(self,node,tag_id,parent_id):
        mmap = {}
        tag = self.get_tag(node)
        mmap["parent_tag_id"] = parent_id
        mmap["tag_id"] = tag_id
        mmap["tag"] = tag
        mmap["flow_id"] = self.flow_id
        mmap["fence_province"] = "*"
        mmap["fence_city"] = "*"
        mmap["fence_service"] = "*"
        mmap["fence_fencename"] = "*"
        mmap["content"] = "*"
        mmap["fence_relation"] = "*"
        if tag == "coordinates":
            if not node.text is None and len(node.text.strip())>=1:
                content = node.text.strip()
                content = re.sub(r" {2,}"," ",content)
                if content != node.text.strip():
                    content_log.write("之前：{}\n之后:{}\n".format(node.text.strip(),content)) 
                if content.strip()!="":
                    mmap["content"]=content
        elif tag == "track":
            content_log.write("find gx:track\n")
            children = node.xpath("./*")
            whens = []
            coords = []
            for child in children:
                if self.get_tag(child)=="when":
                    # content_log.write("find when{}\n".format(child))
                    whens.append(child.text)
                elif self.get_tag(child)=="coord":
                    # content_log.write("find coord{}\n".format(child))
                    coords.append(child.text.replace(" ",","))
            content_log.write("whens:{}\n".format(whens))
            content_log.write("coords:{}\n".format(coords))
            if len(whens)!=len(coords):
                content_log.write("长度不同\n")
            content = ""
            for i in range(len(whens)):
                content = content+coords[i]+','+whens[i]+' '
            content = content[:-1]
            content_log.write("content:{}\n".format(content))
            mmap["content"] = content

        # print mmap
        self.content.append(mmap)
        tagid_tag_map[tag_id] = tag            

    def cal_flow_id(self):
        sha1 = hashlib.sha1()
        info = self.line.decode("utf-8")
        sha1.update(info)
        self.flow_id = sha1.hexdigest()
    
    def fill_content(self,index,row_data,province_fence,flag):
        if flag:
            # 命中更详细的围栏
            self.content[index]["fence_fencename"] = row_data[0].strip()
            self.content[index]["fence_service"] = row_data[1].strip()
            self.content[index]["fence_province"] = row_data[2].strip()
            self.content[index]["fence_city"] = row_data[3].strip()
            self.content[index]["fence_relation"] = "包含"
        else:
            # 只命中省级围栏
            self.content[index]["fence_fencename"] = "*"
            self.content[index]["fence_service"] = "*"
            self.content[index]["fence_province"] = province_fence
            self.content[index]["fence_city"] = "*"
            self.content[index]["fence_relation"] = "包含"
            
    def fetch_fence_info(self):
        for index in range(len(self.content)):
            if self.content[index]["tag"] == "coordinates" or self.content[index]["tag"] == "track":
                query_type = self.judge_query_type(self.content[index])
                if self.content[index]["content"]=="*":continue
                coordinates = self.content[index]["content"].split(" ")
                if len(coordinates)==0:
                    continue
                try:
                    sql_str = ""
                    if query_type == "point":
                        coordinate = coordinates[0].strip().split(",")
                        if len(coordinate)<2:continue
                        longitude = coordinate[0]
                        latitude = coordinate[1]
                        data1 = "POINT({} {})".format(longitude,latitude)
                        data2 = "POINT({} {})".format(latitude,longitude)
                        sql_str = "select * from fencetable where ST_CONTAINS(fencetable.provincebj,st_geomfromtext('{}'))".format(data1)
                        result = engine.execute(sql_str).fetchall()
                        if len(result)==0: continue
                        if len(result)>1:
                            content_log.write("查询到{}个城市围栏:{}\n".format(len(result),sql_str))
                        province_fence = result[0][1].strip() # 默认是第一个,如果有更详细的就使用最详细的
                        for i in range(len(result)):
                            if self.is_valid_fence(result[i][1].strip()):
                                province_fence = result[i][1].strip()
                                break
                        if province_fence =="":continue
                        if self.is_valid_fence(province_fence):
                            sql_str = "select fencename,servicename,province,city,ST_AsText(longlats_wgs) from {} where ST_CONTAINS({}.longlats_wgs, st_geomfromtext('{}'))"
                            sql_str = sql_str.format(province_fence,province_fence,data2)
                            res = engine.execute(sql_str).fetchall()
                            if len(res)==0:
                                self.fill_content(index,None,province_fence,False)
                                continue
                            if len(res)>1:
                                content_log.write("查询到{}个地理围栏:\n{}\n".format(len(res),sql_str))
                            row_data = res[0]
                            content_log.write("data:{}\n".format(res))
                            self.fill_content(index,row_data,province_fence,True)
                        else:
                            self.fill_content(index,None,province_fence,False)
                        # print(self.content[i])
                        # self.content[i]["fence_district"] = row_data[3] 
                    elif query_type == "linestring":
                        longlats = []
                        for coordinate in coordinates:
                            tmp = coordinate.strip().split(",")
                            if len(tmp)<2: continue
                            # print tmp
                            longitude = tmp[0]
                            latitude = tmp[1]
                            longlats.append([latitude,longitude])
                        if len(longlats)<2:
                            print("点的数量少于两个{}".format(longlats))
                            continue
                        data1 = 'LINESTRING('
                        data2 = 'LINESTRING('
                        for i in range(0,len(longlats)):
                            data1 = data1 + longlats[i][1] + ' ' + longlats[i][0] + ','
                            data2 = data2 + longlats[i][0] + ' ' + longlats[i][1] + ','
                        data1 = data1[:-1]+')'
                        data2 = data2[:-1]+')'

                        sql_str = "select * from fencetable where ST_Intersects(provincebj,st_geomfromtext('{}'))".format(data1)
                        result = engine.execute(sql_str).fetchall()
                        if len(result)==0: continue
                        if len(result)>1:
                            content_log.write("查询到{}个省份围栏:{}\n".format(len(result),sql_str))
                        province_fence = result[0][1].strip() # 默认是第一个,如果有更详细的就使用最详细的
                        for i in range(len(result)):
                            if self.is_valid_fence(result[i][1].strip()):
                                province_fence = result[i][1].strip()
                                break
                        if province_fence =="":continue
                        if self.is_valid_fence(province_fence):
                            sql_str = "select fencename,servicename,province,city,ST_AsText(longlats_wgs) from {} where ST_Intersects({}.longlats_wgs, st_geomfromtext('{}'))"
                            sql_str = sql_str.format(province_fence,province_fence,data2)
                            res = engine.execute(sql_str).fetchall()
                            if len(res)==0:
                                self.fill_content(index,None,province_fence,False)
                                # content_log.write("可能碰上地理围栏的数据：\nsql：{}".format(sql_str)) 
                                continue
                            if len(res)>1:
                                content_log.write("查询到{}个地理围栏:\n{}\n".format(len(res),sql_str))
                            row_data = res[0]
                            content_log.write("data:{}\n".format(res))
                        
                            self.fill_content(index,row_data,province_fence,True)
                        else:
                            self.fill_content(index,None,province_fence,False)
                        # print(self.content[i])
                        # self.content[i]["fence_district"] = row_data[3] 

                    elif query_type == "polygon":
                        longlats = []
                        for coordinate in coordinates:
                            tmp = coordinate.strip().split(",")
                            if len(tmp)<2: continue
                            # print tmp
                            longitude = tmp[0]
                            latitude = tmp[1]
                            longlats.append([latitude,longitude])
                        if len(longlats)==0:
                            print("无坐标{}".format(coordinates))
                            continue
                        longlats.append(longlats[0]) # 闭合曲线
                        if len(longlats)<4:
                            print("不同点的数量少于三个{}".format(longlats))
                            continue
                        data1 = 'POLYGON(('
                        data2 = 'POLYGON(('
                        for i in range(0,len(longlats)):
                            data1 = data1 + longlats[i][1] + ' ' + longlats[i][0] + ','
                            data2 = data2 + longlats[i][0] + ' ' + longlats[i][1] + ','
                        data1 = data1[:-1] + '))'
                        data2 = data2[:-1] + '))'
                        sql_str = "select * from fencetable where ST_Intersects(provincebj,st_geomfromtext('{}'))".format(data1)
                        result = engine.execute(sql_str).fetchall()
                        if len(result)==0: continue
                        if len(result)>1:
                            content_log.write("查询到{}个城市围栏:{}\n".format(len(result),sql_str))
                        province_fence = result[0][1].strip() # 默认是第一个,如果有更详细的就使用最详细的
                        for i in range(len(result)):
                            if self.is_valid_fence(result[i][1].strip()):
                                province_fence = result[i][1].strip()
                                break
                        if province_fence =="":continue
                        if self.is_valid_fence(province_fence):
                            sql_str = "select fencename,servicename,province,city,ST_AsText(longlats_wgs) from {} where ST_Intersects({}.longlats_wgs, st_geomfromtext('{}'))"
                            sql_str = sql_str.format(province_fence,province_fence,data2)
                            res = engine.execute(sql_str).fetchall()
                            if len(res)==0:
                                # content_log.write("可能碰上地理围栏的数据：\nsql：{}".format(sql_str)) 
                                self.fill_content(index,None,province_fence,False)
                                continue
                            if len(res)>1:
                                content_log.write("查询到{}个地理围栏:\n{}\n".format(len(res),sql_str))
                            row_data = res[0]
                            content_log.write("data:{}\n".format(res))
                            
                            self.fill_content(index,row_data,province_fence,True)
                        else:
                            self.fill_content(index,None,province_fence,False)
                        # print(self.content[i])
                            # self.content[i]["fence_district"] = row_data[3]
                except Exception as e:
                    if e.__class__==KeyboardInterrupt:
                        raise KeyboardInterrupt
                    else:
                        content_log.write("sql error:{}".format(sql_str))

    # 判断是否有可能命中更详细的围栏
    def is_valid_fence(self,city_fence):
        if city_fence not in ["jsfence","bjfence","shfence","gdfence"]:
            # print city_fence+"无数据"
            return False
        # print "cityfence:"+city_fence
        return True

    def judge_query_type(self,mmap):
        if mmap["tag"] == "track":
            content_log.write("judge track")
            return "linestring"
        parent_tag_id = mmap["parent_tag_id"]
        parent_tag = tagid_tag_map[parent_tag_id]
        query_type = "*"
        if parent_tag == "point":
            query_type = "point"
        elif parent_tag == "linestring":
            query_type = "linestring"
        elif parent_tag == "linearring":
            query_type = "polygon"
        return query_type

    def need_parse(self,s):
        s = s.lower()
            # print "gx_tag:{}\n".format(s)
        # for t in tag2parse:
        #     if s in t:
        #         return True
        if s in tag2parse:
            return True
        return False

    def get_tag(self,node):
        return etree.QName(node).localname.lower()

    def get_latest_tagid(self):
        return self.latest_id
        # try:
        #     f = open("/new_system/auto_res/1h/out/kml/lastest_tagid.txt","r")
        #     line = f.readline()
        #     return int(line)
        # except:
        #     print "get tag id error"
        #     return 1
    
    def toString(self):
        return self.line



if __name__ == '__main__':

    # file_dir = sys.argv[1]
    # # os.system("rm -f /home/res/bio_res.txt")
    # # 将结果暂存到文本文件中
    out_stream_info = open("/new_system/auto_res/1h/out/kml/stream_info.txt","w+") # 保存的是流相关的信息
    out_kml_content = open("/new_system/auto_res/1h/out/kml/kml_content.txt","w+") # 保存的是解析的kml内容
    # out_stream_info = open("./out/stream_info.txt","w") # 保存的是流相关的信息
    # out_kml_content = open("./out/kml_content.txt","w") # 保存的是解析的kml内容
    # fp = open(file_dir,"r")
    # filenames = os.listdir(r"/new_system/auto_res/1h/history/kml_history_address")
    # random.shuffle(filenames)
    # print("需要处理的文件为：{}".format(filenames))
    # for filename in filenames:
    #     if os.path.splitext(filename)[1]==".txt" and len(os.path.splitext(filename))==2:
    #         filename = "/new_system/auto_res/1h/history/kml_history_address/"+filename
    #         with open(filename,"r") as f:
    #             print("==================处理文件{}=============".format(filename))
    #             for line in f:
    #                 kmlInfo = KmlInfo()
    #                 try:
    #                     kmlInfo.fill_info(kmlInfo.preprocess(line))
    #                     if len(kmlInfo.toContentString())!=0:
    #                         out_kml_content.write(kmlInfo.toContentString())
    #                         out_stream_info.write(kmlInfo.toFlowInfoString())
    #                 except:
    #                 	continue
    with open(file2parse,"r") as f:
        print("==================处理文件{}=============".format(file2parse))
        for line in f:
            kmlInfo = KmlInfo()
            try:
                kmlInfo.fill_info(kmlInfo.preprocess(line))
                if len(kmlInfo.toContentString())!=0:
                    out_kml_content.write(kmlInfo.toContentString())
                    out_stream_info.write(kmlInfo.toFlowInfoString())
            except:
                continue
    print "analyze done..."                                        


