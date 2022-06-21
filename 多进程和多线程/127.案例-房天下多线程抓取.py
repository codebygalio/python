import csv
import threading

import requests
import parsel


# # 1.找数据对应的地址
# url = 'https://newhouse.fang.com/house/s/b92/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
#
# # 2. 发送请求
# response = requests.get(url=url, headers=headers)
# # response.encoding = 'gb2312'
# html_data = response.text
# print(html_data)  # 在做数据解析之前, 一定要确认数据请求到了
#
#
# # # 3. 数据解析
# # # 3.1 转换数据类型
# selector = parsel.Selector(html_data)
# # 3.2 数据解析  二次提取
# lis = selector.xpath('//div[@class="nl_con clearfix"]/ul/li')
#
# for li in lis:
#     name = li.xpath('.//div[@class="nlcd_name"]/a/text()').get().strip()
#     price = li.xpath('.//div[@class="nhouse_price"]/*/text()').getall()
#
#     if price == ['暂未取得预售证']:
#         price = price[0]
#     else:
#         price = ''.join(price)
#
#     rooms = li.xpath('.//div[@class="house_type clearfix"]/a/text()').getall()
#     rooms = '-'.join(rooms)
#
#     area = li.xpath('.//div[@class="house_type clearfix"]/text()').re('[\d~平米]+')
#     if area:
#         area = area[0]
#     else:
#         area = 'None'
#
#     tel = li.xpath('.//div[@class="tel"]//*/text()').getall()
#
#     if tel:
#         if len(tel) > 1:
#             tel = ''.join(tel)
#         else:
#             tel = tel[0]
#
#     else:
#         tel = 'None'
#
#     print(name)


lock = threading.Lock()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}


def send_requests(url):
    """发送请求的函数"""
    response = requests.get(url=url, headers=headers)
    return response.text

def parse_data(data):  # --> 返回列表
    """解析数据的函数"""
    selector = parsel.Selector(data)
    # 3.2 数据解析  二次提取
    lis = selector.xpath('//div[@class="nl_con clearfix"]/ul/li')

    data_list = []  # 定义空列表, 接受每一条数据, 二维列表 [[], [], [] ....]
    for li in lis:
        name = li.xpath('.//div[@class="nlcd_name"]/a/text()').get().strip()
        price = li.xpath('.//div[@class="nhouse_price"]/*/text()').getall()
        if price == ['暂未取得预售证']:
            price = price[0]
        else:
            price = ''.join(price)
        rooms = li.xpath('.//div[@class="house_type clearfix"]/a/text()').getall()
        rooms = '-'.join(rooms)
        area = li.xpath('.//div[@class="house_type clearfix"]/text()').re('[\d~平米]+')
        if area:
            area = area[0]
        else:
            area = 'None'
        tel = li.xpath('.//div[@class="tel"]//*/text()').getall()
        if tel:
            if len(tel) > 1:
                tel = ''.join(tel)
            else:
                tel = tel[0]
        else:
            tel = 'None'
        print(name, price, rooms, area, tel)

        data_list.append([name, price, rooms, area, tel])

    return data_list  # 返回二维列表数据

def save_data(data_list):  # 传入一个二维列表
    """保存数据的方法"""
    # 加锁和解锁要放在代码的关键位置
    lock.acquire()
    with open('房天下.csv', mode='a', encoding='utf-8', newline='') as f:
        csv_write = csv.writer(f)
        for data in data_list:
            csv_write.writerow(data)
    lock.release()

# 多任务只针对一个函数对象
def main(url):
    """主函数, 调度其他三个函数的执行"""
    # 1. 调用发送请求的方法
    html_data = send_requests(url)
    # 2. 调用解析数据的方法
    data_list = parse_data(html_data)
    # 调用数据保存的方法
    save_data(data_list)

# 测试主函数是否能运行
# main('https://newhouse.fang.com/house/s/b92/')

if __name__ == '__main__':
    for page in range(1, 31):
        url = f'https://newhouse.fang.com/house/s/b9{page}/'

        threading.Thread(target=main, args=(url, )).start()
