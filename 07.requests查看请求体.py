import requests

headers = {
    'Host': 'movie.douban.com',
    'Referer': 'https://www.baidu.com/link?url=cKXgBx9eo7ttOSYASFpeklnrlErk1XVldUc1oJEediMeAuyaGW2gvQrSt78wZ_xo&wd=&eqid=8fb7ffa800080cd9000000066259671d',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
}

url = 'https://movie.douban.com/top250'
response = requests.get(url)

"""如果想要通过代码查看请求信息, 需要通过response响应体查看"""
print(response.request.url)  # 查看请求体的url地址
print(response.request.headers)  # 查看请球体中请求头字段信息, 常见的字段requests模块会自动加上
print(response.request.method)  # 请求方法