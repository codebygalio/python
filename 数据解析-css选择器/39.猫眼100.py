"""
    使用 css 选择器将猫眼 100 十页全部电影信息全部提取出来。
    目标网址：https://m.maoyan.com/board/4

    name（电影名）
    star（主演）
    releasetime（上映时间）
    score（评分）
	
	提取出来print（）打印
"""
import requests
import parsel


# 1.找数据对应的地址
url = 'https://m.maoyan.com/board/4'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

# 2. 发送请求
response = requests.get(url=url, headers=headers)
html_data = response.text
# print(html_data)  # 在做数据解析之前, 一定要确认数据请求到了

# 3. 数据解析
# 3.1 转换数据类型
selector = parsel.Selector(html_data)
# 3.2 数据解析  二次提取
divs = selector.css('.board-card')  # 所有的div标签
# print(divs)
for div in divs:
    name = div.css('.title::text').get()
    star = div.css('.info>div.actors::text').get()
    releasetime = div.css('.date::text').get()
    score = div.css('.number::text').get()
    print(score)






