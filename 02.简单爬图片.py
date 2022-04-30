# -*- coding: utf-8 -*-
import requests
import re


response = requests.get('https://www.hexuexiao.cn/a/124525-2.html')

# 取出文本数据以后, 一定要确认数据是否请求到了<重要>
data = response.text
# print(data)


"""
正则表达式匹配数据:
<a class="btn btn-default btn-xs" href="(.*?)" role=.*?

<a class="btn btn-default btn-xs" href="(.*?)" role="button" target="_blank">
"""

# re.findall(正则匹配规则, 需要匹配的数据, 匹配模式)
result = re.findall('<a class="btn btn-default btn-xs" href="(.*?)" role="button" target="_blank">', data, re.S)
print(result)

# 图片地址
img_url = result[0]
print(img_url)

# 准备图片名字
img_name = img_url.split('/')[-1]

# 根据地址请求图片数据, 图片视频音频属于二进制数据
# content 从响应体中获取二进制数据
img_data = requests.get(img_url).content
print(img_data)

with open(img_name, mode='wb') as f:
    f.write(img_data)
