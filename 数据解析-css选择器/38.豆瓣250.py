"""
    使用 css 选择器将豆瓣250 十页的全部电影信息全部提取出来。
    目标网址：https://movie.douban.com/top250

    title（电影名）
    info（导演、主演、出版时间）
    score（评分）
    follow（评价人数）
	
	提取出来print（）打印
"""
import requests
import parsel



for page in range(0, 226, 25):
    print('*' * 50)
    # 1.找数据对应的地址
    url = f'https://movie.douban.com/top250?start={page}&filter='
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
    lis = selector.css('.grid_view>li')  # 所有的div标签
    # print(divs)
    for li in lis:
        title = li.css('.title::text').get()
        info = li.css('.bd p:nth-child(1)::text').get().strip()
        score = li.css('.rating_num::text').get()
        follow = li.css('.star>span:nth-child(4)::text').get()
        print(title, info, score, follow)






