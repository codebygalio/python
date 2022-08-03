"""
POST https://quanmin.baidu.com/mvideo/api?log=vhk&tn=1021212c&ctn=1021212c&imei=865166028969924&cuid=CF73FE899DF1B9944A646952719EC2A3|0&bdboxcuid=null&os=android&osbranch=a0&ua=1080_1920_480&ut=HD1900_5.1.1_22_OnePlus&uh=OnePlus,android_x86,HD1900,1&apiv=1.0.0.10&appv=123&version=1.15.5.10&life=1603529816&clife=1603529816&hid=9AF55BC2D869DBF7D08C23FB507A08B4&network=1&sids=3022_1-3258_2-3280_2-3287_3-3291_1-3304_1-3314_2&api_name=videodetail&sign=86a8adf640e75d562c1d6821f816936a HTTP/1.1
Charset: UTF-8
XRAY-TRACEID: 23b7b26a-7054-4cec-ab14-9b81fe404688
XRAY-REQ-FUNC-ST-DNS: okHttp;1603539839150;0
User-Agent: Mozilla/5.0 (Linux; Android 5.1.1; HD1900 Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 bdminivideo/1.15.5.10 arsdk/240 (Baidu; P1 5.1.1)
Referer: https://quanmin.baidu.com/
Content-Type: application/x-www-form-urlencoded
Content-Length: 121
Host: quanmin.baidu.com
Connection: Keep-Alive
Accept-Encoding: gzip
Cookie: BAIDUID=7913ECC26C675A1CF6388D1B2937CC9A:FG=1; BAIDUZID=9PZIywXDyCY1WqHOJne1yy2dThMb5RvWLSaSkyO-MdRtUIv5hWZRKdwMNvnP0kJl5HREduZR6Vh723AILs75aOGOv4f5JGVo_C-z6YOEnZ2g; BAIDUCUID=0ivXil8KBtYp8SiHlO-g8g8L28gIO28MguBgu0uESiKmLqqqB

videodetail=vid%3D5414333819866268196%26recommend_reason%3D%257B%2522a%2522%253Afalse%252C%2522b%2522%253A%2522%2522%257D
"""
import requests
import pprint

url = 'https://quanmin.baidu.com/mvideo/api'
params = {
    "log": "vhk",
    "tn": "1021212c",
    "ctn": "1021212c",
    "imei": "865166028969924",
    "cuid": "CF73FE899DF1B9944A646952719EC2A3|0",
    "bdboxcuid": "null",
    "os": "android",
    "osbranch": "a0",
    "ua": "1080_1920_480",
    "ut": "HD1900_5.1.1_22_OnePlus",
    "uh": "OnePlus,android_x86,HD1900,1",
    "apiv": "1.0.0.10",
    "appv": "123",
    "version": "1.15.5.10",
    "life": "1603529816",
    "clife": "1603529816",
    "hid": "9AF55BC2D869DBF7D08C23FB507A08B4",
    "network": "1",
    "sids": "3022_1-3258_2-3280_2-3287_3-3291_1-3304_1-3314_2",
    "api_name": "videodetail",
    "sign": "86a8adf640e75d562c1d6821f816936a",
}

headers = {
    "Charset": "UTF-8",
    "XRAY-TRACEID": "23b7b26a-7054-4cec-ab14-9b81fe404688",
    "XRAY-REQ-FUNC-ST-DNS": "okHttp;1603539839150;0",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; HD1900 Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 bdminivideo/1.15.5.10 arsdk/240 (Baidu; P1 5.1.1)",
    "Referer": "https://quanmin.baidu.com/",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "121",
    "Host": "quanmin.baidu.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Cookie": "BAIDUID=7913ECC26C675A1CF6388D1B2937CC9A:FG=1; BAIDUZID=9PZIywXDyCY1WqHOJne1yy2dThMb5RvWLSaSkyO-MdRtUIv5hWZRKdwMNvnP0kJl5HREduZR6Vh723AILs75aOGOv4f5JGVo_C-z6YOEnZ2g; BAIDUCUID=0ivXil8KBtYp8SiHlO-g8g8L28gIO28MguBgu0uESiKmLqqqB",

}

data = 'videodetail=vid%3D5414333819866268196%26recommend_reason%3D%257B%2522a%2522%253Afalse%252C%2522b%2522%253A%2522%2522%257D'
# 可以忽略证书安全的问题
response = requests.post(url, headers=headers, params=params, data=data, verify=False)
url = response.json()['videodetail']['data']['download']['url']
pprint.pprint(response.json()['videodetail']['data']['meta']['title'])

mp4_response = requests.get(url)
file = url.split('/')[-1]
open(file, mode='wb').write(mp4_response.content)
