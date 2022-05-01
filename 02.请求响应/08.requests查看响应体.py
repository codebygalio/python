import requests

headers = {
    'Host': 'movie.douban.com',
    'Referer': 'https://www.baidu.com/link?url=cKXgBx9eo7ttOSYASFpeklnrlErk1XVldUc1oJEediMeAuyaGW2gvQrSt78wZ_xo&wd=&eqid=8fb7ffa800080cd9000000066259671d',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
}

url = 'https://movie.douban.com/top250'
response = requests.get(url, headers=headers)

"""如果想要通过代码查看请求信息, 需要通过response响应体查看"""
print(response.text)  # 获取响应体的文本数据  str
print(response.content)  # 获取响应体的二进制数据
# print(response.json())  # 获取响应体的 json 数据, 如果获取的数据不是json格式, 就会报错(simplejson.errors.JSONDecodeError)
print(response.headers)  # 查看响应头字段信息
print(response.cookies)  # 查看响应体的cookies, 返回一个对象(RequestsCookieJar)  可以调用get_dict(), 把对象转字典格式
print(response.cookies.get_dict())
print(response.url)  # 获取响应体的url
print(response.status_code)  # 瞎看响应体状态码
print(response.encoding)  # 指定编码
print(response.apparent_encoding)  # 自动获取编码