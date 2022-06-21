import threading
import time
import random


# 创建一把锁
lock = threading.Lock()


def add1(n):
    for i in range(100):
        time.sleep(random.randint(1,3))  # 随机1到3秒的延迟

        lock.acquire()  # 上锁
        with open('hello.txt', mode='a', encoding='utf-8') as f:
            f.write(f'{n} hello world !' + 'hello world !'*1024)
            f.write('\n')
        # 上完锁以后, 要记得解锁, 不然会出现死锁的现象
        lock.release()  # 解锁


if __name__ == '__main__':
    for n in range(10):
        t1 = threading.Thread(target=add1, args=(n, ))
        t1.start()

"""
在多任务中, 会针对敏感代码, 产生资源的竞争
    全局变量
    单个的文件操作
    
    可以加锁
    
    加锁的作用: 确保只有一个任务能够拿到资源的权限
"""
