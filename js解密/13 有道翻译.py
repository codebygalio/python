import execjs
import requests


headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    # "Content-Length": "253",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "OUTFOX_SEARCH_USER_ID=1182672099@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=587031678.4648843; JSESSIONID=aaaHX5V14uvIl9lLejJrx; ___rl__test__cookies=1599391160335",
    "Host": "fanyi.youdao.com",
    "Origin": "http://fanyi.youdao.com",
    "Pragma": "no-cache",
    "Referer": "http://fanyi.youdao.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}

word = input('请输入你想要翻译的内容：')

with open('12 案例-有道翻译.js', encoding='utf-8') as f:
    js_code = f.read()

# 编译 js 代码， 然后可以调用代码里面的方法
ctx = execjs.compile(js_code)

encode_data = ctx.call('fanyi', word)
print(encode_data)


data = {
    "i": word,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    # "salt": "15993911603408",
    # "sign": "0308486fe5e52bfbfdecb1d723ea79f7",
    # "lts": "1599391160340",
    # "bv": "07f15609aa4583527f9a1c22f48db662",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME",
}

data.update(encode_data)

response = requests.post(
    url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule',
    headers=headers,
    data=data
)
print(response.json())
