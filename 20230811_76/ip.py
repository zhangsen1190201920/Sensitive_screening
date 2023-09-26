def ip2num(ip):
	dec_value=0
	v_list=ip.split('.')
	v_list.reverse()
	t = 1
	for v in v_list:
		dec_value+=(int)v * t
		t=t*(2 ** 8)
	return dec_value
if __name__ == '__main__':
	ip=input()
	dec_value=ip2num(ip)
	print(dec_value)