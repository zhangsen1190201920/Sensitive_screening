# encoding: utf-8
import re
from lxml import etree
import queue
import hashlib
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.sql import select
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


content_table_head = ["tag_id","tag","content","parent_tag_id","flow_id","fence_province","fence_city","fence_service","fence_fencename","fence_relation"]
flowinfo_table_head = ["event_name","flow_id","s_ip","d_ip","s_port","d_port","time","stream_size","file_name","server","user_agent","domain","scountry","sprovince","scity","ssource","scompany","sscence","dcountry","dprovince","dcity","dsource","dcompany","dscence","direction","batch","payload"]
tag2parse = ["kml","folder","document","placemark","point","coordinates","linestring","track","multigeometry","linearring","polygon","outerboundaryis","innerboundaryis",]
tagid_tag_map = {}
# todo change this config to connect to the geoinfo database
engine = create_engine('postgresql://postgres:admin123@10.58.46.72:5449/postgres', echo=False)
conn = engine.connect()
tablename = 'fencetable'

content_log = open("/home/k1816/fs/content_log.txt","a+")
parsed_kml = open("/home/k1816/fs/parsed_kml.txt",'w+')
tag_log = open("/home/k1816/fs/tag_log.txt","w+")
class KmlInfo():
    def __init__(self):
        self.line = "*" # 原始文件的内容
        self.payload = "*" #负载
        self.content = [] # [{}]
        self.latest_id = 0
    def fill_info(self,line):
        self.line = line
        content_log.write("line!\n")
        content_log.write(line)
        self.payload = line
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
        line = line.replace("&lt;","<")
        line = line.replace("&gt;",">")
        line = line.replace("&quot;","\"")
        line = line.replace("&amp;","&")
        line = line.replace("<br>","")
        line = line.replace(r"\'","'")
        line = re.sub(r"<description>[\s\S]*?</description>","",line)
        line = re.sub(r"<!--[\s\S]*?-->","",line)
        line = re.sub(r"<!\[CDATA\[[\s\S]*?\]\]>","",line)
        # line = re.sub(r"...0A[\\|\s][\s\S]*?<","<",line)
        # line = re.sub(r"...0D[\\|\s][\s\S]*?<","<",line)
        print(" bottom! line:")
        print(line)
        line = re.sub(r"\\[0a-zA-Z]{2}","  ",line)
        line=re. sub(r"\\r\\n","  ",line)
        print("After preprocess! line:")
        print(line)
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
                print("KML_Str")
                print(kml_strs)
                root = etree.fromstring(kml_strs[i])
                parsed_kml.write(str(etree.tostring(root,pretty_print=True)))
                parsed_kml.write('\n')
                parent_id = 0
                tag_id = self.get_latest_tagid()
                node_tagid_map = {}
                q = queue.Queue(10000)
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
        #mmap["flow_id"] = self.flow_id
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
                    content_log.write("147!\n")
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
        
    def fill_content(self,index,row_data,province_fence,flag,geo_type):
        if flag:
            # 命中更详细的围栏
            if geo_type == "线":
                self.content[index]["fence_fencename"] = row_data[0].strip()
                self.content[index]["fence_service"] = row_data[1].strip()
                self.content[index]["fence_province"] = row_data[2].strip()
                self.content[index]["fence_city"] = row_data[3].strip()
                self.content[index]["fence_relation"] = [row_data[i] for i in range(4,7) if not row_data[i].startswith("不")][0] # 找出不是以"不"开头的关系字段
                self.content[index]["geo_type"]=geo_type
            elif geo_type == "面":
                self.content[index]["fence_fencename"] = row_data[0].strip()
                self.content[index]["fence_service"] = row_data[1].strip()
                self.content[index]["fence_province"] = row_data[2].strip()
                self.content[index]["fence_city"] = row_data[3].strip()
                self.content[index]["fence_relation"] = [row_data[i] for i in range(4,9) if not row_data[i].startswith("不")][0] # 找出不是以"不"开头的关系字段
                self.content[index]["geo_type"]=geo_type
            else:
                self.content[index]["fence_fencename"] = row_data[0].strip()
                self.content[index]["fence_service"] = row_data[1].strip()
                self.content[index]["fence_province"] = row_data[2].strip()
                self.content[index]["fence_city"] = row_data[3].strip()
                self.content[index]["fence_relation"] = "包含"
                self.content[index]["geo_type"]=geo_type
        else:
            # 只命中省级围栏
            self.content[index]["fence_fencename"] = "*"
            self.content[index]["fence_service"] = "*"
            self.content[index]["fence_province"] = province_fence
            self.content[index]["fence_city"] = "*"
            self.content[index]["fence_relation"] = "包含"
            self.content[index]["geo_type"]=geo_type
    def fetch_fence_info(self):
        for index in range(len(self.content)):
            if self.content[index]["tag"] == "coordinates" or self.content[index]["tag"] == "track":
                query_type = judge_query_type(self.content[index])
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
                            if is_valid_fence(result[i][1].strip()):
                                province_fence = result[i][1].strip()
                                break
                        if province_fence =="":continue
                        if is_valid_fence(province_fence):
                            sql_str = "select fencename,servicename,province,city,ST_AsText(longlats_wgs) from {} where ST_CONTAINS({}.longlats_wgs, st_geomfromtext('{}'))"
                            sql_str = sql_str.format(province_fence,province_fence,data2)
                            res = engine.execute(sql_str).fetchall()
                            if len(res)==0:
                                self.fill_content(index,None,province_fence,False,"点")
                                continue
                            if len(res)>1:
                                content_log.write("查询到{}个地理围栏:\n{}\n".format(len(res),sql_str))
                            row_data = res[0]
                            content_log.write("data:{}\n".format(res))
                            self.fill_content(index,row_data,province_fence,True,"点")
                        else:
                            self.fill_content(index,None,province_fence,False,"点")
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
                        print("data1:")
                        print(data1)
                        data1 = data1[:-1]+')'
                        data2 = data2[:-1]+')'
                        print("data1-plus:")
                        print(data1)
                        print("data2-plus")
                        print(data2)
                        #sql2 = "select province,servicename,fencename,a,b,c " \
                           #"from (select province,servicename,fencename," \
                           #"case ST_CONTAINS(" + row[1].strip() + ".longlats_wgs,'LINESTRING" + strsql4 + "') when 'True' then '包含' else '不包含' end a ," \
                           #"case ST_Intersects(" + row[1].strip() + ".longlats_wgs,'LINESTRING" + strsql4 + "') when 'True' then '相交' else '不相交' end b ," \
                           #"case ST_Touches(" + row[1].strip() + ".longlats_wgs,'LINESTRING" + strsql4 + "') when 'True' then '相切' else '不相切' end c " \
                           #"from " + row[1].strip() + ") t1 " \
                           #"where a = '包含' or b = '相交' or c = '外切' limit 1"
                        sql_str = "select * from fencetable where ST_Intersects(provincebj,st_geomfromtext('{}'))".format(data1)
                        print(sql_str)
                        result = engine.execute(sql_str).fetchall()
                        if len(result)==0: continue
                        if len(result)>1:
                            print("查询到{}个省份围栏:{}\n".format(len(result),sql_str))
                            content_log.write("查询到{}个省份围栏:{}\n".format(len(result),sql_str))
                        province_fence = result[0][1].strip() # 默认是第一个,如果有更详细的就使用最详细的
                        for i in range(len(result)):
                            if is_valid_fence(result[i][1].strip()):
                                province_fence = result[i][1].strip()
                                break
                        print("                        print(province_fence)")
                        print(province_fence)
                        if province_fence =="":continue
                        if is_valid_fence(province_fence):
                            print("sql2..")
                            sql2 = "select fencename,servicename,province,city,a,b,c " \
                               "from (select fencename,servicename,province,city," \
                               "case ST_CONTAINS(" + province_fence + ".longlats_wgs,'" + data2 + "') when 'True' then '包含' else '不包含' end a ," \
                               "case ST_Intersects(" + province_fence + ".longlats_wgs,'" + data2 + "') when 'True' then '相交' else '不相交' end b ," \
                               "case ST_Touches(" + province_fence + ".longlats_wgs,'" + data2 + "') when 'True' then '相切' else '不相切' end c " \
                               "from " + province_fence + ") t1 " \
                               "where a = '包含' or b = '相交' or c = '外切' limit 1 "
                            print(sql2)
                            # sql_str = "select fencename,servicename,province,city,ST_AsText(longlats_wgs) from {} where ST_Intersects({}.longlats_wgs, st_geomfromtext('{}'))"
                            # sql_str = sql_str.format(province_fence,province_fence,data2)
                            # res = engine.execute(sql_str).fetchall()
                            #print(res)
                            res=engine.execute(sql2).fetchall()
                            print("finish res!")
                            print(res)
                            if len(res)==0:
                                self.fill_content(index,None,province_fence,False,"线")
                                # content_log.write("可能碰上地理围栏的数据：\nsql：{}".format(sql_str)) 
                                continue
                            if len(res)>1:
                                content_log.write("查询到{}个地理围栏:\n{}\n".format(len(res),sql_str))
                            row_data = res[0]
                            content_log.write("data:{}\n".format(res))
                        
                            self.fill_content(index,row_data,province_fence,True,"线")
                        else:
                            self.fill_content(index,None,province_fence,False,"线")
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
                            if is_valid_fence(result[i][1].strip()):
                                province_fence = result[i][1].strip()
                                break
                        if province_fence =="":continue
                        if is_valid_fence(province_fence):
                            print("sql2..")
                            sql2 = "select province,servicename,fencename,a,b,c,d,e " \
                               "from (select province,servicename,fencename," \
                               "case ST_CONTAINS(" + province_fence + ".longlats_wgs,'" + data2 + "') when 'True' then '包含' else '不包含' end a ," \
                               "case ST_ContainsProperly(" + province_fence + ".longlats_wgs,'" + data2 + "') when 'True' then '覆盖' else '不覆盖' end b ," \
                               "case ST_Overlaps(" + province_fence + ".longlats_wgs,'" + data2 + "') when 'True' then '相交' else '不相交' end c ," \
                               "case ST_Touches(" + province_fence + ".longlats_wgs,'" + data2 + "') when 'True' then '外切' else '不外切' end d ," \
                               "case ST_Touches(" + province_fence + ".longlats_wgs,'" + data2 + "') when 'True' then '相等' else '不相等' end e " \
                               "from " + province_fence + ") t1 " \
                               "where a = '包含' or b = '覆盖' or c = '相交' or d='外切' or e= '相等' limit 1 "
                            print(sql2)
                            sql_str = "select fencename,servicename,province,city,ST_AsText(longlats_wgs) from {} where ST_Intersects({}.longlats_wgs, st_geomfromtext('{}'))"
                            sql_str = sql_str.format(province_fence,province_fence,data2)
                            res = engine.execute(sql2).fetchall()
                            #res = engine.execute(sql_str).fetchall()
                            if len(res)==0:
                                # content_log.write("可能碰上地理围栏的数据：\nsql：{}".format(sql_str)) 
                                self.fill_content(index,None,province_fence,False,"面")
                                continue
                            if len(res)>1:
                                content_log.write("查询到{}个地理围栏:\n{}\n".format(len(res),sql2))
                            row_data = res[0]
                            content_log.write("data:{}\n".format(res))
                            
                            self.fill_content(index,row_data,province_fence,True,"面")
                        else:
                            self.fill_content(index,None,province_fence,False,"面")
                        # print(self.content[i])
                            # self.content[i]["fence_district"] = row_data[3]
                except Exception as e:
                    if e.__class__==KeyboardInterrupt:
                        raise KeyboardInterrupt
                    else:
                        content_log.write("sql error:{}".format(sql_str))


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
    
    def toString(self):
        return self.line

def parse_kml(line):
    if line=="":return []
    kmlInfo = KmlInfo()
    print("before preprocess")
    print(line)
    kmlInfo.fill_info(kmlInfo.preprocess(line))
    return kmlInfo.content #[{}]


# 判断是否有可能命中更详细的围栏
def is_valid_fence(city_fence):
    if city_fence not in ["jsfence","bjfence","shfence","gdfence"]:
        # print city_fence+"无数据"
        return False
    # print "cityfence:"+city_fence
    return True

def judge_query_type(mmap):
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
        
def query_geo_info(longitude,latitude):
    res = {}
    res["fence_name"] = "*"
    res["fence_service"] = "*"
    res["fence_province"] = "*"
    res["fence_city"] = "*"
    res["fence_relation"] = "*"
    res["fence_type"]="点"
    data1 = "POINT({} {})".format(longitude,latitude)
    data2 = "POINT({} {})".format(latitude,longitude)
    sql_str = "select * from fencetable where ST_CONTAINS(fencetable.provincebj,st_geomfromtext('{}'))".format(data1)
    print(sql_str)
    result = engine.execute(sql_str).fetchall()
    if len(result)==0: return res
    if len(result)>1:
        content_log.write("查询到{}个城市围栏:{}\n".format(len(result),sql_str))
    province_fence = result[0][1].strip() # 默认是第一个,如果有更详细的就使用最详细的
    for i in range(len(result)):
        if is_valid_fence(result[i][1].strip()):
            province_fence = result[i][1].strip()
            break
    if province_fence =="": return res
    if is_valid_fence(province_fence):
        sql_str = "select fencename,servicename,province,city,ST_AsText(longlats_wgs) from {} where ST_CONTAINS({}.longlats_wgs, st_geomfromtext('{}'))"
        sql_str = sql_str.format(province_fence,province_fence,data2)
        print(sql_str)
        res = engine.execute(sql_str).fetchall()
        if len(res)==0:
            res["fence_name"] = "*"
            res["fence_service"] = "*"
            res["fence_province"] = province_fence
            res["fence_city"] = "*"
            res["fence_relation"] = "包含"
            res["fence_type"]="点"
            return res
        row_data = res[0]   
        res["fence_name"] = row_data[0].strip()
        res["fence_service"] = row_data[1].strip()
        res["fence_province"] = row_data[2].strip()
        res["fence_city"] = row_data[3].strip()
        res["fence_relation"] = row_data[4].strip()
        res["fence_type"]="点"
        return res
    else:
        res["fence_name"] = "*"
        res["fence_service"] = "*"
        res["fence_province"] = province_fence
        res["fence_city"] = "*"
        res["fence_relation"] = "包含"
        res["fence_type"]="点"
        return res             


