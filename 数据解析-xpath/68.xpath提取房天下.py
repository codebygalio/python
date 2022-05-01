import requests
import parsel


# 1.找数据对应的地址
url = 'https://newhouse.fang.com/house/s/b92/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

# 2. 发送请求
response = requests.get(url=url, headers=headers)
# response.encoding = 'gb2312'
html_data = response.text
print(html_data)  # 在做数据解析之前, 一定要确认数据请求到了


# # 3. 数据解析
# # 3.1 转换数据类型
selector = parsel.Selector(html_data)
# 3.2 数据解析  二次提取
lis = selector.xpath('//div[@class="nl_con clearfix"]/ul/li')

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

    print(name)







