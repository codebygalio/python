"""
    使用 css 选择器将快代理中我需要的信息提取出来。
    目标网址：https://www.kuaidaili.com/free/
    
    需要解析以下数据:
        ip、
        port、
        类型
	
	提取出来print（）打印
"""

import requests
import parsel


# 1.找数据对应的地址
url = 'https://www.kuaidaili.com/free/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

# 2. 发送请求
response = requests.get(url=url, headers=headers)
html_data = response.text
print(html_data)  # 在做数据解析之前, 一定要确认数据请求到了

# 3. 数据解析
# 3.1 转换数据类型
selector = parsel.Selector(html_data)

# 3.2 数据解析  二次提取
trs = selector.css('.table.table-bordered.table-striped tbody tr')  # 所有的div标签
# print(divs)
for tr in trs:

    ip = tr.css('td:nth-child(1)::text').get()
    port = tr.css('td:nth-child(2)::text').get()
    type_ = tr.css('td:nth-child(4)::text').get()
    # port、
    # 类型
    print(ip, port, type_)