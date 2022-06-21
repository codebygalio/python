import time


def sing():
    for i in range(3):
        print("正在唱歌...%d" % i)
        time.sleep(1)  # 模拟的是, 在任务执行的时候可能会有程序发生了阻塞<请求网址>


def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        time.sleep(1)

start_time = time.time()
sing()
dance()
print('程序执行时间: ', time.time() - start_time)

"""
单线程任务
同时只能去做一件事情
"""