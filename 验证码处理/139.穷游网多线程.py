"""
    目标网址: https://place.qyer.com/china/citylist-0-0-1/
    
    需求:
        1、用多线程采集170页所有数据保存为csv, 计算程序运行的时间
        2、采集以下信息
            city_name   # 城市名
            travel_people  # 去过的人数
            travel_hot    # 热门景点  比如香港有热门景点[ 香港海洋公园 、 星光大道 、 维多利亚港 、 太平山 、 尖沙咀 、 金紫荆广场 、 香港迪士尼乐园 、 中环 、 弥敦道 、 兰桂坊 、 中银大厦 、 香港杜莎夫人蜡像馆 、 中环至半山自动扶]
            img_url  # 城市图片url
            
请在下方编写代码：
"""

# 多任务函数封装
# 多任务, 只能把函数对象转换成多任务
import csv
import concurrent.futures
import time

import parsel
import requests

"""
1.确定请求的地址
2.发送请求
3.解析数据
4.保存数据
"""
# 最理想的函数: 一个函数逻辑只实现一个功能

import threading


lock = threading.Lock()


def send_requests(url):
    """发送请求"""
    response = requests.get(url=url)
    html_data = response.text
    return html_data

def parse_data(data):
    """数据解析"""
    selector = parsel.Selector(data)
    lis = selector.xpath('//ul[@class="plcCitylist"]/li')

    data_list = []  # 定义一个空列表, 用于存放每一条数据, 嵌套的数据
    for li in lis:
        city_name = li.xpath('.//h3/a/text()').get()
        travel_people = li.xpath('.//p[@class="beento"]/text()').get()
        travel_hot = li.xpath('.//p[@class="pois"]/a/text()').getall()

        travel_hot = [hot.strip() for hot in travel_hot]
        travel_hot = ','.join(travel_hot)

        img_url = li.xpath('.//p[@class="pics"]//img/@src').get()

        print(city_name, travel_people, travel_hot, img_url)
        data_list.append([city_name, travel_people, travel_hot, img_url])

    return data_list

def save_data(save_data):
    with open('穷游.csv', mode='a', encoding='utf-8', newline='') as f:
        csv_write = csv.writer(f)
        for data in save_data:
            lock.acquire()  # 针对敏感代码需要上锁
            csv_write.writerow(data)
            lock.release()

#  主函数: 把其他的函数功能按照代码逻辑依次调用
def main(url):
    html_data = send_requests(url)
    parse_list = parse_data(html_data)  # 解析出来的数据
    save_data(parse_list)

# 测试主函数是否能运行
# main('https://place.qyer.com/china/citylist-0-0-1/')



if __name__ == '__main__':

    # 记录池子模块消耗的时间
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        for page in range(1, 171):
            url = f'https://place.qyer.com/china/citylist-0-0-{page}/'
            executor.submit(main, url)
    print('共花费时间:', time.time() - start_time)

# 如果每一个页面的响应速度都慢, 那么多任务也会挂起很多任务,