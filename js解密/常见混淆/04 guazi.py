import requests
import execjs

ctx = execjs.compile(open('04 guazi.js', encoding='utf-8').read())

cookie = ctx.eval('build_cookie')
print(cookie)
headers = {
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # "Accept-Encoding": "gzip, deflate, br",
    # "Accept-Language": "zh-CN,zh;q=0.9",
    # "Cache-Control": "no-cache",
    # "Connection": "keep-alive",
    "Cookie": cookie,
    "Host": "www.guazi.com",
    # "Pragma": "no-cache",
    "Referer": "https://www.guazi.com/sz/dcde2f8bcb6d256fx.htm",
    # "Sec-Fetch-Dest": "document",
    # "Sec-Fetch-Mode": "navigate",
    # "Sec-Fetch-Site": "same-origin",
    # "Sec-Fetch-User": "?1",
    # "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
}

response = requests.get('https://www.guazi.com/sz/dcde2f8bcb6d256fx.htm', headers=headers)
response.encoding = response.apparent_encoding
print(response.text)
