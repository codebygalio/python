"""
目标站点:https://news.163.com/

往下翻有 要闻 这个新闻类目

    需求:
        爬取网易新闻 要闻 类目第一页数据，将数据保存为csv格式
        保存字段需要以下内容

            title  
            channelname  
            docurl  
            imgurl  
            source  
            tlink
"""

# 1.请求地址
import csv
import json
import re
import requests

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

with open('网易新闻.csv', mode='a', encoding='utf-8', newline="") as f:
    f.write('标题,新闻分类,详情页地址,图片地址,新闻来源,详情页\n')
    writer = csv.writer(f)

    for item in json_list:
        # print(item)
        title = item['title']
        channelname = item['channelname']
        docurl = item['docurl']
        imgurl = item['imgurl']
        source = item['source']
        tlink = item['tlink']
        print(title, channelname, docurl, imgurl, source, tlink)

        writer.writerow([title, channelname, docurl, imgurl, source, tlink])


