"""
    检测模块
        从数据库中把代理数据拿出来, 挨个挨个检测代理的可用性(多任务)
        可用: 设置评分 100
        不可用: 执行减分操作
"""
import requests
from db import RedisClient
import concurrent.futures
from config import TEST_URL


# TEST_URL = 'https://www.baidu.com/'  # 检测代理的测试网址

redis_client = RedisClient()  # 实例化一个数据库对象


def verify_proxy(proxy):
    """
    检测代理是否可用
    """
    """
    代理形式

    proxies = {
      "http": "http://10.10.1.10:3128",
      "https": "https://10.10.1.10:1080",
    }
    """
    proxies = {
        "http": "http://" + proxy,
        "https": "https://" + proxy,
    }
    # 可以预知的报错
    try:
        response = requests.get(url=TEST_URL, proxies=proxies, timeout=2)
        if response.status_code in [200, 206, 302]:
            # 请求成功, 代表代理质量高, 可用: 设置评分 100 : 调用数据库模块的 max() 方法
            print('******代理可用******', proxy)
            redis_client.max(proxy)
        else:
            # 请求失败, 代表代理质量低, 不可用: 执行减分操作 : 调用数据库模块的 decrease() 方法
            print('---请求状态码不合法---', proxy)
            redis_client.decrease(proxy)
    except:
        # 如果try代码块的代码报错了, 代表当前的代理请求超时, 代表代理质量低, 执行减分操作 : 调用数据库模块的 decrease() 方法
        redis_client.decrease(proxy)
        print('-----请求超时-----', proxy)


def verify_thread_pool():
    """线程池检测代理"""
    # 1. 首先从数据库中取出所有代理
    proxies_list = redis_client.all()  # 列表
    # 2. 用线程池检测代理
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for proxy in proxies_list:
            executor.submit(verify_proxy, proxy)



if __name__ == '__main__':
    # proxy = ['1.196.177.160:6666', '1.196.177.180:2222', '1.196.177.254:6666',
    #          '1.197.203.189:8888','1.198.73.252:1111', '1.199.31.33:3333']

    # 几千个代理? 挨个挨个检测? 速度能保证吗?   多任务? <多线程?多进程?>  资源消耗问题?
    # for pro in proxy:
    #     verify_proxy(pro)

    verify_thread_pool()