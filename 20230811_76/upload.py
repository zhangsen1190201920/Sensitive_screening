import requests

# 设置请求头中用户名密码
headers = {
    "Username": "u_wa_yj2s_sjcj_hsoft",
    "Password": "CA388EsvrC7kQ"
}

# 设置本地文件路径
local_file_path = "./test.txt"
# 远程服务器URL
remote_url = "http://10.58.136.36:80/wa_yj2s_sjcj_db_b_sjcj_file/test.txt"

# 发送PUT请求上传文件
with open(local_file_path, "rb") as file:
    response = requests.put(remote_url, headers=headers, data=file)
print(response.status_code)
# 检查响应状态码
if response.status_code == requests.codes.ok:
    print("文件上传成功")
else:
    print("文件上传失败")