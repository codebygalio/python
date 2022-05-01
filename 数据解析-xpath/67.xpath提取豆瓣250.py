import requests
import parsel




# 1.找数据对应的地址
url = f'https://movie.douban.com/top250?start=0&filter='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

# 2. 发送请求
response = requests.get(url=url, headers=headers)
html_data = response.text
print(html_data)  # 在做数据解析之前, 一定要确认数据请求到了

# 3. 数据解析
# 3.1 转换数据类型
selector = parsel.Selector(html_data)
# 3.2 数据解析  二次提取
lis = selector.xpath('//ol/li')

for li in lis:  # 二次提取要基于当前节点开始
    title = li.xpath('.//div[@class="hd"]/a/span[1]/text()').get()

    # info = li.css('.bd p:nth-child(1)::text').get().strip()
    info = li.xpath('.//*[@class="bd"]//p[1]/text()').get().strip()

    # score = li.css('.rating_num::text').get()
    score = li.xpath('.//*[@class="rating_num"]/text()').get()

    # follow = li.css('.star>span:nth-child(4)::text').get()
    follow = li.xpath('.//*[@class="star"]/span[4]/text()').get()
    print(follow)







