import threading
import time

def get(url, headers=None):
    print(url)
    time.sleep(5)
    print(headers)

urls = ['https://www.baidu.com','https://www.360.com','https://www.sousou.com']


"""
target  指定需要转换的函数名
args    位置参数, 一定要传一个元组(如果只有一个参数, 这个参数后面要加逗号)**坑**
kwargs  传递关键字参数
"""
for url in urls:
    get_thread = threading.Thread(target=get,
                                  args=(url,),  #  指定位置参数传参, 必须传一个元组
                                  kwargs={'headers': {'User-Agent': 'python'}}

                     )
    get_thread.start()