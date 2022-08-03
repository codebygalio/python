import requests
import execjs
import re

# 1. 请求获取cookie
headers = {
    "Host": "www.guazi.com",
    "Referer": "https://www.guazi.com/sz/dcde2f8bcb6d256fx.htm",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
}

response = requests.get('https://www.guazi.com/sz/dcde2f8bcb6d256fx.htm', headers=headers)
response.encoding = response.apparent_encoding
html = response.text
print([html])
js_code = re.findall('<script type="text/javascript">(.*?)</script>', html, re.S)[0]

js_code1 = """document = {cookie: ""};
location = {href: "https://www.guazi.com/sz/dcde2f8bcb6d256fx.htm", protocol: "https:", replace : function () {}};
window = this;
window['location'] = location;"""

ctx = execjs.compile(js_code1 + js_code)

build_cookie = ctx.eval('name') + '=' + ctx.eval('value') + ';'
print(build_cookie)
# 2. 携带cookie发送请求
headers1 = {
    "Host": "www.guazi.com",
    "Referer": "https://www.guazi.com/sz/dcde2f8bcb6d256fx.htm",
    "Cookie": build_cookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
}
response = requests.get('https://www.guazi.com/sz/dcde2f8bcb6d256fx.htm', headers=headers1)
response.encoding = response.apparent_encoding
html = response.text
print([html])
