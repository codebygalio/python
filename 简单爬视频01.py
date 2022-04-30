import requests
import re  # 正则表达式模块, 内置


response = requests.get('https://video-qn.ibaotu.com/19/83/83/49Z888piC4I8.mp4')
# print(response)

data = response.content  # 二进制数据提取
# print(data)


with open('视频.mp4', mode='wb') as f:  # 二进制数据没有编码
    f.write(data)
