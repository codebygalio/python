import time
import threading  # 线程任务模块, 内置模块


def sing():
    # 只有函数对象可以使用多任务<多进程, 多线程>
    for i in range(3):
        print("正在唱歌...%d" % i)
        time.sleep(1)  # 模拟的是, 在任务执行的时候可能会有程序发生了阻塞<请求网址>


def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        time.sleep(1)
        # 如果要计算线程任务时间, 只能写在线程对应的函数里面进行计算
        print('程序花费时间', time.time() - start_time)


if __name__ == '__main__':
    start_time = time.time()
    """默认情况下只有一个主线程和一个子线程"""
    """但是构建多线程, 那么就会有多个子线程"""
    # threading.enumerate() 查看线程数量
    print('当前线程的数量:', threading.enumerate())
    # 把 sing 这个函数, 转换成线程任务
    sing_thread = threading.Thread(target=sing)  # 只需要传函数名字
    sing_thread.start()  # 执行线程任务

    print('当前线程的数量:', threading.enumerate())

    dance_thread = threading.Thread(target=dance)  # 只需要传函数名字
    dance_thread.start()  # 执行线程任务

    print('当前线程的数量:', threading.enumerate())



"""
在程序发生阻塞的时候, 可以通过多任务, 把阻塞的函数挂起
轮询制度: 计算机会通过调度取询问是否任然是挂起状态
"""

"""用性能换取速度"""

"""多任务执行没有顺序"""