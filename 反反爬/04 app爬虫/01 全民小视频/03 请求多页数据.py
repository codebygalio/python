"""
第一页的请求参数
workspage=ext%3D%257B%2522authorId%2522%253A%2522j2deP_BZ_iqfxkUl6Y4aIQ%2522%252C%2522authorType%2522%253A%2522ugc%2522%257D%26refresh_state%3D0

workspage=ext=%7B%22authorId%22%3A%22j2deP_BZ_iqfxkUl6Y4aIQ%22%2C%22authorType%22%3A%22ugc%22%7D&refresh_state=0
workspage=ext={"authorId":"j2deP_BZ_iqfxkUl6Y4aIQ","authorType":"ugc"}&refresh_state=0

workspage=ext%3D%257B%2522authorId%2522%253A%2522j2deP_BZ_iqfxkUl6Y4aIQ%2522%252C%2522authorType%2522%253A%2522ugc%2522%257D%26refresh_state%3D2%26pgext%3D%257B%2522refresh_time%2522%253A1603869526%252C%2522list_min_time%2522%253A16034437804824%257D

workspage=ext%3D%257B%2522authorId%2522%253A%2522j2deP_BZ_iqfxkUl6Y4aIQ%2522%252C%2522authorType%2522%253A%2522ugc%2522%257D%26refresh_state%3D2%26pgext%3D%257B%2522refresh_time%2522%253A1603869526%252C%2522list_min_time%2522%253A16030775470069%257D

workspage=ext={"authorId":"j2deP_BZ_iqfxkUl6Y4aIQ","authorType":"ugc"}&refresh_state=0
workspage=ext={"authorId":"j2deP_BZ_iqfxkUl6Y4aIQ","authorType":"ugc"}&refresh_state=2&pgext={"refresh_time":1603869526,"list_min_time":16034437804824}
workspage=ext={"authorId":"j2deP_BZ_iqfxkUl6Y4aIQ","authorType":"ugc"}&refresh_state=2&pgext={"refresh_time":1603869526,"list_min_time":16030775470069}
"""
from pprint import pprint
import urllib.parse
import requests

url = 'https://quanmin.baidu.com/mvideo/api'
params = {
    "log": "vhk",
    "tn": "1021212c",
    "ctn": "1021212c",
    "imei": "865166021083095",
    "cuid": "4EEC132872D62EB1CDD6BD749C7CC274|0",
    "bdboxcuid": "null",
    "os": "android",
    "osbranch": "a0",
    "ua": "1080_1920_480",
    "ut": "SEA-AL10_5.1.1_22_HUAWEI",
    "uh": "HUAWEI,android_x86,SEA-AL10,1",
    "apiv": "1.0.0.10",
    "appv": "123",
    "version": "1.15.5.10",
    "life": "1603882735",
    "clife": "1603882735",
    "hid": "E9026359C6696D1E73A74025E0969736",
    "network": "1",
    "sids": "3022_1-3304_1-3333_1-3335_2-3337_1",
    "api_name": "workspage",
    "sign": "66482b720c7de1d253b09198e61ddb08",

}
headers = {
    "Charset": "UTF-8",
    "XRAY-TRACEID": "0bee9d8f-4eb1-46c5-a00d-ff5fe2d28186",
    "XRAY-REQ-FUNC-ST-DNS": "okHttp;1603884023032;0",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SEA-AL10 Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Safari/537.36 bdminivideo/1.15.5.10 arsdk/240 (Baidu; P1 5.1.1)",
    "Referer": "https://quanmin.baidu.com/",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "249",
    "Host": "quanmin.baidu.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Cookie": "BAIDUID=3D13D15A0A9B0713C3B65203E4FBD511:FG=1; BAIDUZID=H0Vs7VfI28ZblmVc3BW1aMifXAyXKa8PRxqWzbd1L5AxdGp4_v5-ClqAWoEbm0iE_M0yz5UA7SqZRe8FG9fyfUBl_Dn39tTN6qF7cuv9u73s; BAIDUCUID=giS9agaa2f_oaHiyg8SP808THi0Fi287jivsu0uR2iKaLqqqB",

}


data1 = 'workspage=ext'
user = urllib.parse.quote('{"authorId":"j2deP_BZ_iqfxkUl6Y4aIQ","authorType":"ugc"}')
data2 = f'={user}&refresh_state=0'

response = requests.post(url, headers=headers, params=params, data=data1+data2, verify=False)
data = response.json()
# pprint(data)
works_list = data['workspage']['data']['worksList']
for work in works_list:
    # pprint(work)
    print(work['title'])
    print(work['playurl'])

next_data = data['workspage']['data']['ext']
print('next_data', next_data)
data1 = '{"authorId":"j2deP_BZ_iqfxkUl6Y4aIQ","authorType":"ugc"}'
data2 = next_data

data3 = '=' + urllib.parse.quote(data1) + '&refresh_state=2&pgext=' + urllib.parse.quote(data2)
data4 = 'workspage=ext' + urllib.parse.quote(data3)
print('data4', data4)
response = requests.post(url, headers=headers, params=params, data=data4, verify=False)
data = response.json()
print('-'*50)
works_list = data['workspage']['data']['worksList']
for work in works_list:
    # pprint(work)
    print(work['title'])
    print(work['playurl'])


next_data = data['workspage']['data']['ext']
print('next_data', next_data)
data1 = '{"authorId":"j2deP_BZ_iqfxkUl6Y4aIQ","authorType":"ugc"}'
data2 = next_data

data3 = '=' + urllib.parse.quote(data1) + '&refresh_state=2&pgext=' + urllib.parse.quote(data2)
data4 = 'workspage=ext' + urllib.parse.quote(data3)
print('data4', data4)
response = requests.post(url, headers=headers, params=params, data=data4, verify=False)
data = response.json()
print('-'*50)
works_list = data['workspage']['data']['worksList']
for work in works_list:
    # pprint(work)
    print(work['title'])
    print(work['playurl'])