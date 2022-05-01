"""
    目标网址: http://www.win4000.com/zt/dongman.html
    
    需求:
        "动漫桌面壁纸" 文字下面有很多动漫图集
        1、用xpath采集数据
        2、采集以下信息
            采集动漫图集的标题
            采集动漫图集中图片对应的url地址
            
        解析到数据用print()函数打印
"""
import requests
import parsel


# 1.请求地址
url = 'http://www.win4000.com/zt/dongman.html'
headers = {
    'Cookie': 't=fee6ba90c53a5884db542eb619592896; r=5891; XSRF-TOKEN=eyJpdiI6IlVrQjdqaUJUT2JuWG90M1hCZjVaOEE9PSIsInZhbHVlIjoibm5TamVqREh2SVZUQlZtQkxVVGZhbzlSZnRuaGNsRjFVajBZaTF0Y0kwMGczV3IxOFF4MW1VMU1VY2x4emd0MGRpRWh1XC9BYVluQjJkc1htbnB6eXlXQ0VEUTh3TVN1OG5zOUF5UCs0Yk9YWTZOT1ZTMUx2ekw5ZURmbjJzbUNSIiwibWFjIjoiMjExMmE1OWFjZDM1MzM4MGM2ZjY0MzlmNDFjOWZlZDNlZjM1NTE3ODk1MzU5MTk5MmViMGMxN2QzNmY2NjBlNSJ9; win4000_session=eyJpdiI6Im5US2dSMmtsUHJGTktHT01LU251bkE9PSIsInZhbHVlIjoid1wvME9MRnpndDNJT1BaYlVVTFwvYTd0eXlSbWRJWjFySWlXZmtNQWxOZldkRGlhY090dERmR2J0a3JkSkdnNUIyeDZKNG5FS0ZxWWlDSWVcL2FmNk95TFZcL0crSGNNdTNsOFZQcU85bW05YkJIY1hGdnFPZkt0NzFkMzBuTmZxNkZNIiwibWFjIjoiNWYyZDY2NzUyZjI3OGJmMTRlODFmNDQ5MzBiOTA0Nzk4MmM4MDI2Mjk4ZjJiYzFmMWQ4MmFlMDk2NmRhMmVhYyJ9',
    'Host': 'www.win4000.com',
    'Referer': 'http://www.win4000.com/zt/dongman.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}

# 2.发送请求
response = requests.get(url=url, headers=headers)
html_data = response.text
print(html_data)

# 3. 数据解析
selector = parsel.Selector(html_data)
lis = selector.xpath('//div[@class="list_cont Left_list_cont  Left_list_cont1"]//ul/li')

for li in lis:
    title = li.xpath('./a/@title').get()
    img_url = li.xpath('./a/img/@data-src').get()
    print(img_url)