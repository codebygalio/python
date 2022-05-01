import requests


# 获取代理的函数
def get_ip():
    json_data = requests.get(url='http://demo.spiderpy.cn/get/').json()
    ip = json_data['proxy']
    return ip

ip_port = get_ip()

proxies = {
  "http": "http://" + ip_port,
  "https": "http://" + ip_port,
}

# proxies=proxies  使用代理请求数据
# requests.exceptions.ProxyError  代理质量不高, 使用不了引发的报错
url = 'https://www.baidu.com/'
response = requests.get(url=url, proxies=proxies, timeout=5, verify=False)  # allow_redirects=False 阻止重定向
print(response.text)

# 当前网站封锁了自己的电脑, 可以用代理ip发送请求
