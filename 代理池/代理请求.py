"""
    使用代理
"""
import requests



def get_proxy():
    proxy = requests.get(url="http://127.0.0.1:5000/get").text
    print('获取到的代理:', proxy)

    proxies = {
        "http": "http://" + proxy,
        "https": "https://" + proxy,
    }
    print('构建好的代理:', proxies)

    return proxies


get_proxy()


response = requests.get(url='https://www.baidu.com', proxies=get_proxy())
print(response.text)
print(response.status_code)



