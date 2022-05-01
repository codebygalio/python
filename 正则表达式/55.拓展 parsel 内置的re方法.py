import parsel
import requests

url = f'https://movie.douban.com/top250?start=0&filter='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

response = requests.get(url=url, headers=headers)
html_data = response.text

selector = parsel.Selector(html_data)
lis = selector.css('.grid_view>li')  # 所有的div标签
for li in lis:
    follow = li.css('.star>span:nth-child(4)::text').re('\d+')[0]  # 评价人数
    print(follow)

# parsel中调用re方法, 要根据selector对象调用, 直接在方法中写正则规则就行
# 返回的是一个列表