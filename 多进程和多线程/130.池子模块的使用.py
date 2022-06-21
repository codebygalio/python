import concurrent.futures  # 池子模块, 内置模块
import time


def thread_function(name):
	print("子线程 %s: 启动" % name)
	time.sleep(2)
	print("子线程 %s: 完成" % name)


if __name__ == '__main__':
    # ThreadPoolExecutor  线程池对象
    # ProcessPoolExecutor 进程池对象
    # max_workers  指定最大任务数, 控制多任务数量, 并发数
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for i in range(10):
            # submit  向池子里面添加任务
            executor.submit(thread_function, i)  # 参数1: 函数名;  参数2:函数的参数<按照位置传>