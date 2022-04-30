import requests

url = 'https://github.com/'
# timeout=1  设置请求的时间, 单位/秒, 超过这个时间就会引发程序的报错, 报错可以通过过异常捕获解决, 异常重试
response = requests.get(url=url, timeout=5)
print(response.text)