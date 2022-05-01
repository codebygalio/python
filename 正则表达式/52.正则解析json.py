import re
import requests



# 1.地址
url = 'https://www.yy.com/more/page.action?biz=game&subBiz=idx&page=3&moduleId=1180&pageSize=60'

# 2.请求
response = requests.get(url=url)
json_data = response.text
print(json_data)

# 3.解析
author_name = re.findall(',"name":"(.*?)",', json_data, re.S)
room_name = re.findall(',"desc":"(.*?)",', json_data, re.S)
imgUrlList= re.findall(',"thumb":"(.*?)",', json_data, re.S)
print(author_name)
print(room_name)
print(imgUrlList)

for data in zip(author_name, room_name, imgUrlList):
    print(data)