import dcmdata
import json
if __name__ == '__main__':
	dcmdata.inittaglist(r'/home/k1816/fs/dataprocessor/taglist.txt')
	f=open("test/0bc335386f4d8fc8479ddd4912b6f2fe411bddc4_42.123.70.59_80_18.204.195.159_44858", "rb")
	res=f.read()
	f.close()
	final_result = []
	print(type(res))
	res=json.loads(dcmdata.parsedata(res.hex()))
	print("finish_load!")
	for resultitem in res:
		newresult={}
		if int(resultitem['code']) == 0 and resultitem['data'] != "null":
			name=resultitem['name']
			newresult[name]=resultitem['data']
			final_result.append(newresult)
	print(final_result)

