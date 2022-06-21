import csv

import requests

# 1. 确定请求地址
url = 'https://index.mysteel.com/api/pricetrend/getChartMultiCity.htm'

params = {
    'catalog': '%E7%94%B5%E8%A7%A3%E9%93%9D_:_%E7%94%B5%E8%A7%A3%E9%93%9D',
    'city': '%E9%95%BF%E6%B2%99',
    'spec': 'A00_:_A00_',
    'startTime': '2022-04-01',
    'endTime': '2022-04-29',
    'callback': 'json',
    # 'v': '1651836956249',  # 时间戳: 格林威治时间1970年1月1号0时0分0秒 到 目前位置所消耗的时间总数
                           # 单位: 毫秒级时间戳<13数字>  微秒级时间戳<16个数字>
}

# 2. 发送请求
response = requests.get(url=url, params=params)
json_data = response.json()
print(json_data)

# 3.数据解析
list_data = json_data['data'][0]['dateValueMap']
city_name = json_data['data'][0]['lineName']
print(city_name)

with open('data.csv', mode='a', encoding='utf-8', newline="") as f:
    csv_write = csv.DictWriter(f, fieldnames=['date', 'value', 'city_name'])
    csv_write.writeheader()  # 写入表头, 只需要写入一次

    for data in list_data:
        data['city_name'] = city_name
        print(data)

        csv_write.writerow(data)



# import time
#
# print(int(time.time() * 1000000))