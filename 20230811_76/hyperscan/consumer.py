import re
from multiprocessing import JoinableQueue
import dcmdata
# import magic
import chardet
import textract
import os
import json

# rules 已经细分到行业
import hyperscan
from shared_variable import sensitive_models, file_subscribes
from db_utils import *
from engine.geo_engine import parse_kml
def consumer(data_unit_q: JoinableQueue, write_q: JoinableQueue,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18):
	testDict=dict()
	realDict=dict()
	while True:
		try:
			data_unit = data_unit_q.get()
			if data_unit is None:
			    print("consumer got None")
			    continue
			#rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18=consume_test(data_unit,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18)
			#print(data_unit)
			#results = consume_sm(data_unit)
			#print("sm final results:{}".format(results))
			#for res in results:
			    # 将命中的结果日志绑定到数据单元上
			   # sm_hit_log = SmHitLogDataUnit(res)
			    #data_unit.sm_hit.append(sm_hit_log)
			#if consume_bio(data_unit): continue
			results = consume_geo(data_unit)
			print("geo final results:{}".format(results))
			for res in results:
			    # 将geo命中的结果日志绑定到数据单元上
			    geo_hit_log = GeoHitLogDataUnit(res)
			    data_unit.geo_hit.append(geo_hit_log)
			results = consume_identity(data_unit)
			print("identity final results:{}".format(results))
			for res in results:
			     #将ide命中的结果日志绑定到数据单元上
			    identity_hit_log = IDeHitLogDataUnit(res)
			    data_unit.ide_hit.append(identity_hit_log)
			results=consume_dcm(data_unit)
			print("dcm final results:{}".format(results))
			if results is not None :
			    for res in results:
			   # 将dcm命中的结果日志绑定到数据单元上
			       dcm_hit_log = MedHitLogDataUnit(res)
			       data_unit.dcm_hit.append(dcm_hit_log)
			testDict,realDict=consume_eventid(data_unit,testDict,realDict)
			if (data_unit.geo_hit is not None and len(data_unit.geo_hit) != 0) or (data_unit.dcm_hit is not None and len(data_unit.dcm_hit) != 0) or  (data_unit.ide_hit is not None and len(data_unit.ide_hit) != 0) :
			   write_q.put(data_unit)
		except Exception as e:
			print("consumer extension %s",%e)
			f2=open("errorlog.txt",'a',encoding='UTF-8')
			f2.write(str(e))
			f2.close()
def consume_eventid(data_unit,testDict,realDict):
	if data_unit.c_event_id in testDict:
		testDict[data_unit.c_event_id]+=1
	else:
		testDict[data_unit.c_event_id]=1
	print(testDict)
	print(realDict)
	if (data_unit.geo_hit is not None and len(data_unit.geo_hit) != 0) or (data_unit.dcm_hit is not None and len(data_unit.dcm_hit) != 0) or  (data_unit.ide_hit is not None and len(data_unit.ide_hit) != 0) :
		if data_unit.c_event_id in realDict:
			realDict[data_unit.c_event_id]+=1
			name=str(data_unit.c_event_id)+".txt"
			f=open(name,'w+',encoding='UTF-8')
			f.write("have_content:"+str(realDict[data_unit.c_event_id]))
			f.write("all:"+str(allDict[data_unit.c_event_id]))
			f.close()
	else:
		realDict[data_unit.c_event_id] =0
		name=str(data_unit.c_event_id)+".txt"
		print(name)
		f=open(name,'w+',encoding='UTF-8')
		print("created!")
		f.write("have_content:"+str(realDict[data_unit.c_event_id]))
		f.write("all:"+str(allDict[data_unit.c_event_id]))
		f.close()
	return testDict,realDict
def consume_bio(data_unit):
    if isinstance(data_unit, (HttpFileDataUnit, FtpFileDataUnit, EmailFileDataUnit,TrxFileDataUnit)):
        extension = os.path.splitext(data_unit.filepath)[-1]
        if extension in ["fasta"]:
            try:
                with open(data_unit.filepath, "rb") as f:
                    up_file = {
                        'file': (os.path.basename(data_unit.filepath), f)
                    }
                    url = "ip:port/upload" # todo 需要填写服务器地址
                    resp = requests.post(url=url, files=up_file)
                    print(resp)
                    return True
            except Exception as ex:
                print(ex)
    return False
def consume_identity(data_unit):
    final_result = []
    if isinstance(data_unit, (HttpFileDataUnit, FtpFileDataUnit, EmailFileDataUnit)):
        # 如果是报文引擎的数据，默认都需要进行敏感甄别
        print("not implement")
    elif isinstance(data_unit, TrxFileDataUnit):
        # 如果是天融信的文件
        print("not implement")
    elif isinstance(data_unit, RawTrafficDataUnit):
        # 如果是原始流量数据
        print("not implement")
    elif isinstance(data_unit, ReturnValueDataUnit):
        # 如果是变量返回值
        # 16进制的数据
        result = {}
        # result = hyperscan.match(bytes.fromhex(data_unit.c_return_info))
        #bytes.fromhex(data_unit.c_return_info).decode()
        if  str(data_unit.c_event_id) == "10030003339": 
            print("consume_identity has been in!!!")
            print("###################")
            print(data_unit.c_event_id)
            return_info = str(bytes.fromhex(data_unit.c_return_info))
            print(return_info)
            result["model_id"] = "2" #TODO 先填上身份证的id,后续再改
            sm = sensitive_models[int(result['model_id'])]
            idcard_pattern=re.compile(r'\D((1[1-5]|2[1-3]|3[1-7]|4[1-6]|5[0-4]|6[1-5]|71|8[1-2])[0|1|2|3|4|5|9][0-9]{1}[0|1|2|3|4|5|8][0-9]{1}(19[0-9]{2}|(200[0-9]{1}|201[0-9]{1}|202[0-2]{1}))((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|30|31)|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}([0-9]|x|X))\D')
            host_pattern=re.compile(r'Host: ([\s\S]+?)\\0D\\0A')
            user_agent_pattern=re.compile(r'(User-Agent:[\s\S]+?)\\0D\\0A')
            phone_pattern = phone=re.compile(r'"[Pp]hone":"([\S\s]*?)"')
            name_pattern=re.compile(r'"[Nn]ame":"([\S\s]*?)"')
            address_pattern=re.compile(r'"address":"([\S\s]*?)"')
            bankcard_pattern = re.compile(r'"[Bb]ank[Cc]ard":"([\S\s]*?)"')
            password_pattern=re.compile(r'"[Pp]ass[Ww]or[d|ds]":"([\S\s]*?)"')
            
            idcards = re.findall(idcard_pattern,return_info)
            if len(idcards) == 0:
                return final_result
            result['idcard'] = result_concat(idcards)
            result['host'] = result_concat(re.findall(host_pattern,return_info))
            result['user_agent'] = result_concat(re.findall(user_agent_pattern,return_info))
            result['name'] = result_concat2(re.findall(name_pattern,return_info))
            result['phone'] = result_concat(re.findall(phone_pattern,return_info))
            result['address'] = result_concat2(re.findall(address_pattern,return_info))
            result['bankcard'] = result_concat(re.findall(bankcard_pattern,return_info))
            result['password'] = result_concat(re.findall(password_pattern,return_info))
            result['hit_count'] = len(idcards)
            
            # 填写额外的字段
            result["model_name"] = sm.model_name
            result["industry"] = sm.industry
            result["master_tablename"] = data_unit.tablename
            final_result.append(result)

    return final_result

def consume_sm(data_unit):
    final_result = []
    # print("got data_unit! filepath:{}".format(data_unit.filepath))
    print("got data_unit!")
    if isinstance(data_unit, (HttpFileDataUnit, FtpFileDataUnit, EmailFileDataUnit)):
        # 如果是报文引擎的数据，默认都需要进行敏感甄别
        #extract_content(data_unit, file_type=data_unit.c_file_type)
        # print("extracted content：{}".format(data_unit.content))
        #result = hyperscan.match(data_unit.content)
        result={}
        print("match result:{}".format(result))
        for res in result:
            if res['content'] == '':
                continue
            model_id = int(res["model_id"])
            sm = sensitive_models[model_id]
            # TODO 如果是身份证号码,需要进行过滤
            if sm.model_name == "身份证":
                if not validate_id_number(res['content']):
                    continue
            file_types = sm.file_type.split(";")
            # 根据文件类型以及fs——sm关联表过滤匹配结果
            if data_unit.c_file_type not in file_types:
                # print("file type not match! data_unit.c_file_type:{}".format(data_unit.c_file_type))
                continue
            fs_ids = query_fs_by_model_id(model_id)
            print("fs_ids:{}".format(fs_ids))
            if len(fs_ids) == 0:
                continue
            flag = False
            for fs_id in fs_ids:
                fs = file_subscribes[fs_id[0]]
                if data_unit.c_file_type in fs.file_type.split(";"):
                    flag = True
            if flag is False:
                continue

            # 填写额外的字段
            res["model_name"] = sm.model_name
            res["industry"] = sm.industry
            res["hit_count"] = len(res["content"].split(";"))
            res["master_tablename"] = data_unit.tablename
            final_result.append(res)

    elif isinstance(data_unit, TrxFileDataUnit):
        # 如果是天融信的文件
        extract_content(data_unit)
        print("extracted content：{}".format(data_unit.content))
        result = hyperscan.match(data_unit.content)
        print("match result:{}".format(result))
        model_ids = query_sm_by_csemp_rule_id(data_unit.rule_id)
        for res in result:
            # 过滤掉result中content为空的结果
            if res['content'] == '':
                continue
            # 过滤掉result中未配置规则的匹配结果
            if res['model_id'] not in model_ids:
                continue
            sm = sensitive_models[res['model_id']]
            
            # TODO 如果是身份证号码,需要进行过滤
            if sm.model_name == "身份证":
                if not validate_id_number(res['content']):
                    continue
                
            # 填写额外的字段
            res["model_name"] = sm.model_name
            res["industry"] = sm.industry
            res["hit_count"] = len(res["content"].split(";"))
            res["master_tablename"] = data_unit.tablename
            final_result.append(res)


    elif isinstance(data_unit, RawTrafficDataUnit):
        # 如果是原始流量数据
        result = hyperscan.match(data_unit.block_content)
        print("raw traffic match result:{}".format(result))
        model_ids = query_sm_by_csemp_rule_id(data_unit.rule_id)
        for res in result:
            # 过滤掉result中content为空的结果
            if res['content'] == '':
                continue
            # 过滤掉result中未配置规则的匹配结果
            if res['model_id'] not in model_ids:
                continue
            sm = sensitive_models[res['model_id']]
            
            # TODO 如果是身份证号码,需要进行过滤
            if sm.model_name == "身份证":
                if not validate_id_number(res['content']):
                    continue
                
            # 填写额外的字段
            res["model_name"] = sm.model_name
            res["industry"] = sm.industry
            res["hit_count"] = len(res["content"].split(";"))
            res["master_tablename"] = data_unit.tablename
            final_result.append(res)
    
    elif isinstance(data_unit, ReturnValueDataUnit):
        # 如果是变量返回值
        # 16进制的数据
        result = []
        result = hyperscan.match(bytes.fromhex(data_unit.c_return_info))
        print("return value match result:{}".format(result))
        print(data_unit.c_event_id)
        model_ids = query_sm_by_csemp_rule_id(data_unit.c_event_id)
        model_ids=[x[0] for x in model_ids]
        print(model_ids)
        for res in result:
            # 过滤掉result中content为空的结果
            if res['content'] == '':
                continue
            # 过滤掉result中未配置规则的匹配结果
            if int(res['model_id'] ) not in model_ids:
                continue
            sm = sensitive_models[int(res['model_id'])]
            
            # TODO 如果是身份证号码,需要进行过滤
            if sm.model_name == "身份证":
                if not validate_id_number(res['content']):
                    continue
            
            # 填写额外的字段
            res["model_name"] = sm.model_name
            res["industry"] = sm.industry
            res["hit_count"] = len(res["content"].split(";"))
            res["master_tablename"] = data_unit.tablename
            final_result.append(res)

    return final_result

def consume_geo(data_unit):
    final_result = []
    # print("got data_unit! filepath:{}".format(data_unit.filepath))
    print("geo got data_unit!")
    if isinstance(data_unit, (HttpFileDataUnit, FtpFileDataUnit, EmailFileDataUnit)):
        # 如果是报文引擎的数据，默认都需要进行敏感甄别
        extract_content(data_unit, file_type=data_unit.c_file_type)
        print("extracted content:{}".format(data_unit.content))
        result = parse_kml(data_unit.content)
        result=[]
        print("geo engine match result:{}".format(result))
        for res in result:
            new_res = {}
            if res['content'] == '*' or res["content"] == "":
                continue
            new_res["long_lati"] = res["content"]
            new_res["geography"] = "地理"
            new_res["geo_type"] = res["geo_type"]
            new_res["fence_province"] = res["fence_province"]
            new_res["fence_city"] = res["fence_city"]
            new_res["fence_name"] = res["fence_fencename"]
            # todo
            new_res["fence_type"] = "unknown"
            new_res["fecne_relation"] = res["fecne_relation"]
            #new_res["need_irregualr_judge"] = need_irregular_judge("地理","kml")
            final_result.append(new_res)

    elif isinstance(data_unit, TrxFileDataUnit):
        # 如果是天融信的文件
        extract_content(data_unit)
        print("extracted content：{}".format(data_unit.content))
        result = parse_kml(data_unit.content)
        print("geo engine match result:{}".format(result))
        
        for res in result:
            new_res = {}
            if res['content'] == '*' or res["content"] == "":
                continue
            new_res["long_lati"] = res["content"]
            new_res["geography"] = "地理"
            new_res["geo_type"] = res["geo_type"]
            new_res["fence_province"] = res["fence_province"]
            new_res["fence_city"] = res["fence_city"]
            new_res["fence_name"] = res["fence_fencename"]
            # todo
            new_res["fence_type"] = "unknown"
            new_res["fecne_relation"] = res["fecne_relation"]
            new_res["need_irregualr_judge"] = need_irregular_judge("地理","kml")
            
            final_result.append(new_res)
        


    elif isinstance(data_unit, RawTrafficDataUnit):
        # 如果是原始流量数据
        final_result = []
        result = parse_kml(data_unit.block_content)
        print("raw traffic geo engine match result:{}".format(result))

        for res in result:
            new_res = {}
            if res['content'] == '*' or res["content"] == "":
                continue
            new_res["long_lati"] = res["content"]
            new_res["geography"] = "地理"
            new_res["geo_type"] = res["geo_type"]
            new_res["fence_province"] = res["fence_province"]
            new_res["fence_city"] = res["fence_city"]
            new_res["fence_name"] = res["fence_fencename"]
            # todo
            new_res["fence_type"] = "unknown"
            new_res["fecne_relation"] = res["fecne_relation"]
            new_res["need_irregualr_judge"] = need_irregular_judge("地理","kml")

            final_result.append(new_res)
    
    elif isinstance(data_unit, ReturnValueDataUnit):
        # 如果是变量返回值
        # 16进制的数据
        #print(data_unit.c_return_info)
        #print(bytes.fromhex(data_unit.c_return_info))
        result=[]
        final_result = []
        print(data_unit.c_event_id)
        if str(data_unit.c_event_id)=="10030002903" or str(data_unit.c_event_id)=="10030002920"  or str(data_unit.c_event_id)=="10030003338" or str(data_unit.c_event_id)=="10030003201":
             result = parse_kml(str(bytes.fromhex(data_unit.c_return_info)))
             #print(format(str(bytes.fromhex(data_unit.c_return_info))))
       # print("return value geo engine match result:{}".format(result))
        str_test="coordinates"
        str_save=str(bytes.fromhex(data_unit.c_return_info))
        if str_save.find(str_test)>=0:
            print(str_save)
            f2=open("kml_create.txt",'w',encoding='UTF-8')
            f2.write(str_save)
            f2.close()
            #os.system('pause')
        for res in result:
            new_res = {}
            if res['content'] == '*' or res["content"] == "" or  res["fence_province"]=='*'  :
                continue
            new_res["long_lati"] = res["content"]
            new_res["geography"] = "地理"
            new_res["geo_type"] = res["geo_type"]
            new_res["fence_province"] = res["fence_province"]
            new_res["fence_city"] = res["fence_city"]
            new_res["fence_name"] = res["fence_fencename"]
            # todo
            new_res["fence_type"] = res["fence_service"]
            new_res["fence_relation"] = res["fence_relation"]
            new_res["master_tablename"] = data_unit.tablename
            #new_res["need_irregualr_judge"] = need_irregular_judge("地理","kml")
            final_result.append(new_res)
    return final_result
def consume_dcm(data_unit):
    final_result = []
    # print("got data_unit! filepath:{}".format(data_unit.filepath))
    #print("DCM got data_unit!")
    if isinstance(data_unit, (HttpFileDataUnit, FtpFileDataUnit, EmailFileDataUnit)):
        print("Not finish!")
    elif isinstance(data_unit, ReturnValueDataUnit):
        # 如果是变量返回值
        # 16进制的数据
        #print(data_unit.c_return_info)
        #print(bytes.fromhex(data_unit.c_return_info))
        result=[]
        final_result = []
        #print(data_unit.c_event_id)
        if str(data_unit.c_event_id)=="10030003331" :
           print("DCM got data_unit!")
           res =json.loads( dcmdata.parsedata(data_unit.c_return_info))
           #print(res)
           final_result = []
           newresult={}
           print("########finish_dcmparse!###########")
           for resultitem in res:
               if int(resultitem['code']) == 0 and resultitem['data'] != "null":
                     name=resultitem['name']
                     newresult[name]=resultitem['data']
               else :
                     name=resultitem['name']
                     newresult[name]="*"
           newresult["master_tablename"] = data_unit.tablename
           #newresult["need_irregualr_judge"] = need_irregular_judge("医疗","dcm")

           final_result.append(newresult)
           print(final_result)
           f2=open("dcm_create.dcm",'w',encoding='UTF-8')
           f2.write(data_unit.c_return_info)
           f2.close()
           #os.system('pause')
        return final_result
def extract_content(data_unit, file_type=None):
    try:
        # TODO 文件内容可能不是utf-8编码
        content = textract.process(data_unit.filepath, extension=file_type).decode("utf-8")
        data_unit.content = content
    except UnicodeDecodeError as ue:
        print(ue)
        print("{}处理出错".format(data_unit.data))
    except LookupError as le:
        print(le)
        print("未知拓展名data:{}\tfile_type:{}".format(data_unit.data, file_type))


def guess_encoding(filename):
    """Returns a tuple of (guessed encoding, confidence).
    :param filename:
    """
    res = chardet.detect(open(filename).read())
    return res['encoding'], res['confidence']


def validate_id_number(id_number):
    """校验身份证号码的合法性"""
    if len(id_number) != 18:
        return False

    # 计算校验码
    factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1]
    checksum = sum(int(id_number[i]) * factors[i] for i in range(17))
    checksum %= 11
    checksum = (12 - checksum) % 11
    if checksum == 10:
        checksum = 'X'
    # 检查校验码是否正确
    return str(checksum) == id_number[-1].upper()


def need_irregular_judge(industry,filetype):
    for sm in sensitive_models:
        print(sm)
        if sm.industry == "地理" and sm.file_type == "kml" and sm.need_irregular_judge == 1:
            return True
    return False

# 将多个结果使用分号拼接到一块
def result_concat(results):
    s = ""
    for result in results:
        print(result)
        if isinstance(result,tuple):
            s= s+result[0] + ";"
        else :
            s=s+result+";"
    s = s[:-1]
    return s
# 用于转码的结果连接
def result_concat2(results):
    s = ""
    for result in results:
        #print(result)
            print("result not tuple")
            print(result)
            print("convert(result)")
            print(convert(result))
            print("###!!!###")
            s=s+convert(result)+";"
    s = s[:-1]
    #print("s")
    #print(s)
    return s

def convert(input):
    input=re.sub(r"\\x","",input)
    s=""
    encodings=["utf-8","gbk","gb2312","big5"]
    for encoding in encodings:
        try:
             byte_str=bytes.fromhex(input)
             s=byte_str.decode(encoding)
             print("成功使用编码%解码!"%encoding)
             break
        except Exception as e:
             print("consumer extension %s",e)
    return s
    #return input.encode("raw_unicode_escape").decode('utf-8')
if __name__ == '__main__':
    for root, dirs, files in os.walk("test"):
        for file in files:
            print("filename:{} desc:{}".format(file, magic.from_file(os.path.join(root, file))))
