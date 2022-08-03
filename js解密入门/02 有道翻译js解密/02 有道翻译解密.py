import requests
import execjs

url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

headers = {
    'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=1257807381.4736035; OUTFOX_SEARCH_USER_ID="-1855482410@10.110.96.154"; fanyi-ad-id=305838; fanyi-ad-closed=1; ___rl__test__cookies=1653313056974',
    'Host': 'fanyi.youdao.com',
    'Origin': 'https://fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
}

while True:
    word = input('请输入您要翻译的字符串(输入0退出循环):')

    with open('01 有道翻译js.js', mode='r', encoding='utf-8') as f:
        js_code = f.read()

    compile_result = execjs.compile(js_code)

    result = compile_result.call('youdao', word)

    data = {
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '16533130569765',
        'sign': 'd7591653cc346b10fac0a2fff90bf6c0',
        'lts': '1653313056976',
        'bv': '1744f6d1b31aab2b4895998c6078a934',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    }
    data.update(result)  # 更新字典


    response = requests.post(url=url, data=data, headers=headers)
    print(response.json()['translateResult'][0][0]['tgt'])
