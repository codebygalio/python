"""
目标站点:https://news.163.com/

往下翻有 要闻 这个新闻类目

    需求:
        爬取网易新闻 要闻 类目第一页数据，将数据保存为 Excel 表格
        保存字段需要以下内容

            title  
            channelname  
            docurl  
            imgurl  
            source  
            tlink
"""
import json
import re
import requests
import openpyxl


# 1.请求地址
url = 'https://news.163.com/special/cm_yaowen20200213/?callback=data_callback'

# 2. 发送请求
response = requests.get(url=url)
data_str = response.text
# print(data_str)

# 3.数据解析
"""规范的json数据提取出来"""
json_str = re.findall('data_callback\((.*?)\)', data_str, re.S)[0]  # --> str
# print(json_str)

"""把json字符串进行反序列化操作"""
# str --> 对象
json_list = json.loads(json_str)
# print(json_list)
# print(type(json_list))

work = openpyxl.Workbook()
sheet = work['Sheet']
# sheet = work.create_sheet('Sheet')
sheet.append(['标题', '新闻分类', '详情页地址', '图片地址', '新闻来源', '详情页'])


for item in json_list:
    # print(item)
    title = item['title']
    channelname = item['channelname']
    docurl = item['docurl']
    imgurl = item['imgurl']
    source = item['source']
    tlink = item['tlink']
    print(title, channelname, docurl, imgurl, source, tlink)

    sheet.append([title, channelname, docurl, imgurl, source, tlink])

work.save('网易新闻.xlsx')

