"""
	目标网址：https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76
	
	要求：
		1、请求上述网址的数据
		2、把获取到的数据保存到json文件中
            文件命名: data.json
            需要在文件中看到json字符串

"""

import requests
import json

# 1.请求地址
url = 'https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76'

# 2. 发送请求
response = requests.get(url=url)
json_data = response.json()  # ---> dict
print(json_data)

# 序列化   对象 --> str
json_str = json.dumps(json_data, ensure_ascii=False)


with open('data.json', mode='w', encoding='utf-8') as f:
    f.write(json_str)