# -*- coding: utf-8 -*-
import concurrent.futures
import time
import random

urls = [
    f'https://maoyan.com/board/4?offset={page}' for page in range(1000)
]


def download(url):
    # print(url)
    # 延时操作
    time.sleep(0.0000001)


if __name__ == '__main__':
    """单线程"""
    start_time = time.time()
    for url in urls:
        download(url)
    print("单线程执行：" + str(time.time() - start_time), "秒")

    """多线程"""
    start_time_1 = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for url in urls:
            executor.submit(download, url)
    print("线程池计算的时间：" + str(time.time() - start_time_1), "秒")

    """多进程"""  # 多进程的开销会比较大
    start_time_1 = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for url in urls:
            executor.submit(download, url)
    print("进程池计算的时间：" + str(time.time() - start_time_1), "秒")

"""
函数部分

"""