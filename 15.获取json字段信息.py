"""
	目标网址：https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76
	发送 GET 请求
	
	
	要求：
		1、请求上述网址的数据
		2、按照要求提取以下字段信息
			title、
			picPath、
			playUrl
		提取下来用 print() 函数打印即可

"""

import requests
import pprint

url = 'https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76'

response = requests.get(url)
json_data = response.json()  # 规范的 json 数据  json() 方法会在底层将数据转换成对象
pprint.pprint(json_data)

print(type(json_data))

data_list = json_data['data']

for data in  data_list:
    title = data['title']
    picPath = data['picPath']
    playUrl = data['playUrl']
    print(title, picPath, playUrl)