"""
    -  将北京,上海,广州三个城市的门店信息获取下来
	- 获取下来的信息用print函数打印
	
"""
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

def get_page(city_name):
    """获取城市页数的函数"""
    data = {
        'cname': '',
        'pid': '',
        'keyword': city_name,
        'pageIndex': '1',
        'pageSize': '10'
    }

    # data 是请求参数关键字
    response = requests.post(url=url, data=data, headers=headers)
    json_data = response.json()
    count = json_data['Table'][0]['rowcount']
    # print(count)

    if count % 10 > 0:
        page_num = count // 10 + 1

    else:
        page_num = count // 10
    return page_num


# print(get_page('北京'))
def send_requests(city_name):
    page_num = get_page(city_name)

    for page in range(1, page_num + 1):

        print(f'正在抓取 {city_name} 城市 -- 第 {page} 页数据')
        data = {
            'cname': '',
            'pid': '',
            'keyword': city_name,
            'pageIndex': str(page),
            'pageSize': '10'
        }

        response = requests.post(url=url, data=data, headers=headers)
        json_data = response.json()

        # 数据解析
        data_list = json_data['Table1']
        for da in data_list:
            storeName = da['storeName']
            cityName = da['cityName']
            addressDetail = da['addressDetail']
            pro = da['pro']

            print(storeName, cityName, addressDetail, pro)


if __name__ == '__main__':
    all_city = ['北京','上海','广州']
    for city in all_city:
        send_requests(city)
