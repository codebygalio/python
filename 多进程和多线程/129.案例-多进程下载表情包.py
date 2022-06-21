import multiprocessing
import re
import time
import requests
import threading

# def run():
#     start_time = time.time()
#     for page in range(1, 11):
#         print(f'========================正在抓取第 {page} 页数据=========================')
#         response = requests.get(f'https://fabiaoqing.com/biaoqing/lists/page/{page}.html')
#         html_data = response.text
#         # print(html_data)
#
#         # 解析图片地址
#         # <img class="ui image lazy".*?src="(.*?)" titl.*?
#         # <img class="ui image lazy" data-original="(.*?)" src=.*?
#         result = re.findall('<img class="ui image lazy" data-original="(.*?)" src=.*?', html_data, re.S)
#         # print(result)
#
#         for img_url in result:
#             img_data = requests.get(img_url).content  # 图片数据
#             file_name = img_url.split('/')[-1]
#             with open('img\\' + file_name, mode='wb') as f:
#                 print('正在下载:', file_name)
#                 f.write(img_data)
#     print('花费时间:', time.time() - start_time)

"""
1. 确定请求地址
2. 发送请求
3. 解析数据
4. 保存数据
"""


def send_requests(url):
    """发送请求的函数"""
    response = requests.get(url=url)  # 响应体对象
    return response

def parse_data(data):  # --> 返回列表
    """解析数据的函数"""
    result_list = re.findall('<img class="ui image lazy" data-original="(.*?)" src=.*?', data, re.S)
    return result_list

def save_data(file_name, data):
    """
    保存数据的方法
    :param file_name: 文件名
    :param data: 图片数据
    :return:
    """
    with open('img\\' + file_name, mode='wb') as f:
        f.write(data)
        print('下载完成:', file_name)

# 多任务只针对一个函数对象
def main(url):
    """主函数, 调度其他三个函数的执行"""
    # 1. 调用发送请求的方法
    html_data = send_requests(url).text
    # 2. 调用解析数据的方法
    imgUrl_list = parse_data(html_data)
    # print(imgUrl_list)
    for imgUrl in imgUrl_list:
        img_data = send_requests(imgUrl).content  # 请求图片数据
        file_name = imgUrl.split('/')[-1]
        # 调用数据保存的方法
        save_data(file_name, img_data)


# 当主函数功能写完后, 一定要测试主函数是否能运行, 是否运行有错误
# main('https://fabiaoqing.com/biaoqing/lists/page/')


if __name__ == '__main__':

    for page in range(1, 11):
        url = f'https://fabiaoqing.com/biaoqing/lists/page/{page}.html'
        # 创建线程对象
        main_Process = multiprocessing.Process(target=main, args=(url,))
        # 执行线程对象
        main_Process.start()

"""
多进程比多线程消耗的系统资源要大得多
"""