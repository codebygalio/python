import urllib.parse
import re
import time
import requests

user_url = 'https://quanmin.hao222.com/feedvideoui/api?pd=author_share_mvideo&ucenter=ext%3D%257B%2522metiaId%2522%253A%2522JNncGYC-Gb2_JxMLUNLBjg%2522%252C%2522authorType%2522%253A%2522ugc%2522%252C%2522authorId%2522%253A%2522JNncGYC-Gb2_JxMLUNLBjg%2522%257D'

user_url = urllib.parse.unquote(urllib.parse.unquote(user_url))
user = re.findall('"authorType":"(.*?)","authorId":"(.*?)"', user_url)[0]

prefix = 'workspage=ext'
user = '{"authorId":"%s","authorType":"%s"}' % (user[1], user[0])

first_data = '=' + urllib.parse.quote(user) + '&refresh_state=0'
user_data = '=' + urllib.parse.quote(user) + '&refresh_state=2&pgext='

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

first_data = prefix + urllib.parse.quote(first_data)
response = requests.post(url, headers=headers, params=params, data=first_data, verify=False)
data = response.json()
# pprint(data)
works_list = data['workspage']['data']['worksList']
for work in works_list:
    # pprint(work)
    print(work['title'])
    print(work['playurl'])
page = 1
while True:
    next_data = data['workspage']['data']['ext']
    # print(next_data)
    data = prefix + urllib.parse.quote(user_data + next_data)
    response = requests.post(url, headers=headers, params=params, data=data, verify=False)
    data = response.json()
    # pprint(data)
    works_list = data['workspage']['data']['worksList']
    if not works_list:
        break
    for work in works_list:
        # pprint(work)
        print(work['title'])
        print(work['playurl'])
    print(f'正在爬取第 {page} 页 。。。。。。', works_list)
    page += 1
    time.sleep(2)
