import time
import multiprocessing  # 进程模块, 内置


def sing():
    for i in range(3):
        print("正在唱歌...%d" % i)
        time.sleep(1)


def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        time.sleep(1)


"""多进程会导致解释器找不到主进程"""
if __name__ == '__main__':

    # 把普通的函数转换成进程对象
    sing_process = multiprocessing.Process(target=sing)
    # 执行进程对象
    sing_process.start()

    dance_process = multiprocessing.Process(target=dance)
    dance_process.start()

"""
多线程是很多人去做事, 但是只有一个人能拿到做事的权限
多进程是很多人同时去做事情

多进程现阶段无法记录程序执行时间
"""
