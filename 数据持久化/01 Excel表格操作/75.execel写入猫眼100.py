import requests
import parsel


# 1.找数据对应的地址
url = 'https://m.maoyan.com/board/4'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

# 2. 发送请求
response = requests.get(url=url, headers=headers)
html_data = response.text

"""
# 1. 创建工作簿对象
# 2. 根据工作簿对象创建表
# 3. 数据写入表格
# 4. 保存表格文件
"""
import openpyxl

work = openpyxl.Workbook()
sheet1 = work.create_sheet('表1')

# 3. 数据解析
selector = parsel.Selector(html_data)
divs = selector.css('.board-card')  # 所有的div标签
for div in divs:

    name = div.css('.title::text').get()
    star = div.css('.info>div.actors::text').get()
    releasetime = div.css('.date::text').get()
    score = div.css('.number::text').get()
    print(name, star, releasetime, score)

    sheet1.append([name, star, releasetime, score])

sheet1.append(['name', 'star', 'releasetime', 'score'])

work.save('猫眼.xlsx')

"""
操作表格模块:
openpyxl
jwt
xlrd
xlwt
xlutils


"""
