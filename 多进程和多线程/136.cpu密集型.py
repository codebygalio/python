# -*- coding: utf-8 -*-
import concurrent.futures
import time

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def evaluate_item(x):
    """计算总和，这里只是为了消耗时间"""
    a = 0
    for i in range(0, 10000000):
        # 重复计算 消耗时间 cpu计算能力
        a = a + i
        # time.sleep(0.00000001)
    return x


if __name__ == '__main__':
    """单线程"""
    start_time = time.time()
    for item in number_list:
        evaluate_item(item)
    print("单线程执行：" + str(time.time() - start_time), "秒")

    """多线程"""
    start_time_1 = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate_item, item)
    print("线程池计算的时间：" + str(time.time() - start_time_1), "秒")

    """多进程"""
    start_time_2 = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate_item, item)
    print("进程池计算的时间：" + str(time.time() - start_time_2), "秒")