"""
    目标网址: https://place.qyer.com/china/citylist-0-0-1/
    
    需求:
        1、用xpath采集数据
        2、采集以下信息
            city_name   # 城市名
            travel_people  # 去过的人数
            travel_hot    # 热门景点
            img_url  # 城市图片url
            
        解析到数据用print()函数打印
"""
import requests
import parsel


# 1.请求地址
url = 'https://place.qyer.com/china/citylist-0-0-1/'

# 2.发送请求
response = requests.get(url=url)
html_data = response.text
# print(html_data)

# 3. 数据解析
selector = parsel.Selector(html_data)
lis = selector.xpath('//ul[@class="plcCitylist"]/li')

for li in lis:
    city_name = li.xpath('.//h3/a/text()').get()
    travel_people = li.xpath('.//p[@class="beento"]/text()').get()
    travel_hot = li.xpath('.//p[@class="pois"]/a/text()').getall()

    travel_hot = [hot.strip() for hot in travel_hot]
    travel_hot = ','.join(travel_hot)

    img_url = li.xpath('.//p[@class="pics"]//img/@src').get()

    print(img_url)

