"""
表情包爬取
将此页面下的前十页图片全部获取下来：https://fabiaoqing.com/biaoqing
"""
import re

import requests


for page in range(1, 11):
    print(f'========================正在抓取第 {page} 页数据=========================')
    response = requests.get(f'https://fabiaoqing.com/biaoqing/lists/page/{page}.html')
    html_data = response.text
    # print(html_data)

    # 解析图片地址
    # <img class="ui image lazy".*?src="(.*?)" titl.*?
    # <img class="ui image lazy" data-original="(.*?)" src=.*?
    result = re.findall('<img class="ui image lazy" data-original="(.*?)" src=.*?', html_data, re.S)
    # print(result)

    for img_url in result:
        img_data = requests.get(img_url).content  # 图片数据
        file_name = img_url.split('/')[-1]
        with open('img\\' + file_name, mode='wb') as f:
            print('正在下载:', file_name)
            f.write(img_data)


