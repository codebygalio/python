"""
    实现抓取免费代理的模块
"""
import requests
import re
import time
from db import RedisClient

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

proxy_pattern = re.compile('.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5}).*?', re.S)


def spider_yun_proxy():
    """
    抓取云代理数据
    目标网址: http://www.ip3366.net/free/
    """
    for page in range(1, 11):
        print('云代理:', f'http://www.ip3366.net/free/?stype=1&page={page}')
        time.sleep(1)  # 必须要延迟
        html_data = requests.get(url=f'http://www.ip3366.net/free/?stype=1&page={page}', headers=headers).text
        ip_port = re.findall(proxy_pattern, html_data)

        for ip, port in ip_port:
            # yield 返回的是一个对象, 可以在for循环内部返回, 对象可以用for循环遍历
            yield ip + ':' + port


def spider_89_proxies():
    """
    爬取89代理ip
    目标网址: https://www.89ip.cn/
    """
    for page in range(1, 11):
        time.sleep(1)
        print('89代理', f'https://www.89ip.cn/index_{page}.html')
        html_data = requests.get(url=f'https://www.89ip.cn/index_{page}.html', headers=headers).text
        ip_port = re.findall(proxy_pattern, html_data)
        # print(ip_port)
        for ip, port in ip_port:
            # 返回一个生成器对象,可以用for循环取值
            yield ip + ":" + port


def spider_kuai_proxies():
    """
    爬取快代理ip
    目标网址：https://www.kuaidaili.com/free/
    """
    for page in range(1, 11):
        time.sleep(1)
        print('快代理', f'https://www.kuaidaili.com/free/inha/{page}/')
        response = requests.get(f'https://www.kuaidaili.com/free/inha/{page}/', headers=headers)
        ip_port = re.findall(proxy_pattern, response.text)
        # print(ip_port)
        for ip, port in ip_port:
            # 返回一个生成器对象(在for循环中一个一个返回数据)
            yield ip + ":" + port

proxy_fuc_list = [spider_yun_proxy, spider_89_proxies, spider_kuai_proxies]

# 加其他网站的抓取逻辑

if __name__ == '__main__':
    # 让函数依次执行
    proxy_fuc_list = [spider_yun_proxy, spider_89_proxies, spider_kuai_proxies]
    # 函数调用 : 函数名 + (参数)

    # 鸭子类型: 不关心对象是什么, 只关注对象的行为

    redis_client = RedisClient()  # 实例化数据库对象


    # for func in proxy_fuc_list:
    #     proxies = func()
    #     for proxy in proxies:
    #         print(proxy)
    #         redis_client.add(proxy)

    result = redis_client.all()
    print(result)


