"""
爬取《剑来》前面十章的小说数据,分别保存在不同的txt文件下

	-- 网址： https://www.bige7.com/book/1031/

"""

# 1. 在小说列表页中解析每一个章节的部分地址(取前十章)
# 循环请求每个章节的数据, 保存下来

import requests
import re
import os


response = requests.get('https://www.bige7.com/book/1031/')
html = response.text
# print(html)  # 文本数据

# 解析部分章节地址
# <dd><a href ="(.*?)">.*?</a></dd>
result_list = re.findall('<dd><a href ="(.*?)">.*?</a></dd>', html, re.S)
# print(result_list)
# print(result_list[:10])

# 创建文件夹
if not os.path.exists('剑来'):  # 如果没有 剑来 文件夹在此项目路径中
    os.mkdir('剑来')

# https://www.bige7.com/
for result in result_list[:10]:
    # 拼接全部地址
    all_url = 'https://www.bige7.com' + result
    # print(all_url)

    response_2 = requests.get(all_url)
    data = response_2.text

    # 解析章节名字, 作为保存的文件名
    # <h1 class="wap_none">(.*?)</h1>
    title = re.findall('<h1 class="wap_none">(.*?)</h1>', data, re.S)[0]

    # 解析的章节内容
    result_contend = re.findall('<div id="chaptercontent" class=".*?">(.*?)</p></div>', data, re.S)
    contend = result_contend[0].replace('<br /><br />', '\n')

    # 保存数据
    with open('剑来\\' + title, mode='w', encoding='utf-8') as f:
        print('正在保存:', title)
        f.write(contend)


