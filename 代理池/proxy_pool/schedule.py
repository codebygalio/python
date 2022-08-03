"""
    调度模块
"""
import time

from getter import proxy_fuc_list
from db import RedisClient
from verify import verify_thread_pool
from api import app
import multiprocessing
from config import GETTER_PROXY, VERIFY_PROXY
from config import SERVER_HOST, SERVER_PORT


redis_client = RedisClient()

class Schedule:
    # 1. 调度获取代理模块, 免费代理会不定时更新, 所以我们每个一段时间就要抓取一次代理数据
    def getter_proxy(self):
        while True:
            for func in proxy_fuc_list:
                proxies = func()
                for proxy in proxies:
                    print('--代理写入数据库--', proxy)
                    redis_client.add(proxy)
            time.sleep(GETTER_PROXY)

    # 2. 调度检测代理模块, 不断的检测代理可用性(质量)
    def verify_proxy(self):
        while True:
            verify_thread_pool()
            time.sleep(VERIFY_PROXY)

    # 3. 调度api服务模块
    def api_server(self):
        app.run(host=SERVER_HOST, port=SERVER_PORT)

    # 调用这三个函数一起<同时>运行?
    def run(self):
        print('##################--代理池开始运行--##################')
        getter_proxy_process = multiprocessing.Process(target=self.getter_proxy)
        getter_proxy_process.start()

        if redis_client.count() > 0:  # 数据库有代理我们才检测
            verify_proxy_process = multiprocessing.Process(target=self.verify_proxy)
            verify_proxy_process.start()

        api_server_process = multiprocessing.Process(target=self.api_server)
        api_server_process.start()



if __name__ == '__main__':
    work = Schedule()
    work.run()

