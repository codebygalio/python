import csv
import json

import requests
import parsel

# 1.找数据对应的地址
url = 'https://m.maoyan.com/board/4'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

# 2. 发送请求
response = requests.get(url=url, headers=headers)
html_data = response.text

# 3. 数据解析
selector = parsel.Selector(html_data)
divs = selector.css('.board-card')  # 所有的div标签

with open('猫眼.csv', mode='a', encoding='utf-8', newline='') as f:
    f.write('电影名字,主演,上映时间,评分\n')
    csv_write = csv.writer(f)

    for div in divs:
        name = div.css('.title::text').get()
        star = div.css('.info>div.actors::text').get()
        releasetime = div.css('.date::text').get()
        score = div.css('.number::text').get()
        print(name, star, releasetime, score)

        csv_write.writerow([name, star, releasetime, score])
