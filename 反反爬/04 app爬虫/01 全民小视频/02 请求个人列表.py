"""
POST https://quanmin.baidu.com/mvideo/api?log=vhk&tn=1021212c&ctn=1021212c&imei=865166028969924&cuid=CF73FE899DF1B9944A646952719EC2A3|0&bdboxcuid=null&os=android&osbranch=a0&ua=1080_1920_480&ut=HD1900_5.1.1_22_OnePlus&uh=OnePlus,android_x86,HD1900,1&apiv=1.0.0.10&appv=123&version=1.15.5.10&life=1603529816&clife=1603529816&hid=9AF55BC2D869DBF7D08C23FB507A08B4&network=1&sids=3022_1-3258_2-3280_2-3287_3-3291_1-3304_1-3314_2&api_name=workspage&sign=4afce9d55ca857bc73e8e9abd547e8eb HTTP/1.1
Charset: UTF-8
XRAY-TRACEID: fb7033b7-b466-4fc7-a3c0-16b523f19541
XRAY-REQ-FUNC-ST-DNS: okHttp;1603545275587;0
User-Agent: Mozilla/5.0 (Linux; Android 5.1.1; HD1900 Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 bdminivideo/1.15.5.10 arsdk/240 (Baidu; P1 5.1.1)
Referer: https://quanmin.baidu.com/
Content-Type: application/x-www-form-urlencoded
Content-Length: 144
Host: quanmin.baidu.com
Connection: Keep-Alive
Accept-Encoding: gzip
Cookie: BAIDUID=7913ECC26C675A1CF6388D1B2937CC9A:FG=1; BAIDUZID=9PZIywXDyCY1WqHOJne1yy2dThMb5RvWLSaSkyO-MdRtUIv5hWZRKdwMNvnP0kJl5HREduZR6Vh723AILs75aOGOv4f5JGVo_C-z6YOEnZ2g; BAIDUCUID=0ivXil8KBtYp8SiHlO-g8g8L28gIO28MguBgu0uESiKmLqqqB

workspage=ext%3D%257B%2522authorId%2522%253A%2522eJ4rV5FoCxGmmGE_LmepMA%2522%252C%2522authorType%2522%253A%2522ugc%2522%257D%26refresh_state%3D0
"""
from pprint import pprint

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

data = 'workspage=ext%3D%257B%2522authorId%2522%253A%2522eJ4rV5FoCxGmmGE_LmepMA%2522%252C%2522authorType%2522%253A%2522ugc%2522%257D%26refresh_state%3D0'

response = requests.post(url, headers=headers, params=params, data=data, verify=False)
data = response.json()
pprint(data)
works_list = data['workspage']['data']['worksList']
for work in works_list:
    # pprint(work)
    print(work['title'])
    print(work['playurl'])
