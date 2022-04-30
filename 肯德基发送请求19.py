# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword

import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'

params = {'op': 'keyword'}

# 构建请求参数形式
data = {
    'cname':'',
    'pid':'',
    'keyword': '武汉',
    'pageIndex': '1',
    'pageSize': '10'
}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}

# data 是请求参数关键字
response = requests.post(url=url, params=params, data=data, headers=headers)
print(response.json())
