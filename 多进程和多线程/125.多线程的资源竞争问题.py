import threading
import time
import random


def add1(n):
    for i in range(100):
        time.sleep(random.randint(1,3))  # 随机1到3秒的延迟
        with open('hello.txt', mode='a', encoding='utf-8') as f:
            f.write(f'{n} hello world !' + 'hello world !'*1024)
            f.write('\n')


if __name__ == '__main__':
    for n in range(10):
        t1 = threading.Thread(target=add1, args=(n, ))
        t1.start()

"""
在多任务中, 会针对敏感代码, 产生资源的竞争
    全局变量
    单个的文件操作
    
    可以加锁
"""
