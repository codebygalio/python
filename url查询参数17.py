# https://pic.sogou.com/pics?query=%E9%A3%8E%E6%99%AF&mood=7&dm=0&mode=1

"""
? 前面是请求地址, 后面是一系列的查询参数
& 分割每一个查询参数
查询参数都是二值型的数据  key=value

"""

import requests

url = 'https://pic.sogou.com/pics?'

# 在请求的时候构建查询参数
params = {
    'query': '风景',
    'mood': '7',
    'dm': '0',
    'mode': '1'
}
# ? 可加可不加
# params 传递查询参数
response = requests.get(url=url, params=params)
print(response.request.url)


"""url编码问题"""
# http协议是不支持中文的, 如果地址中包含了中文, 会把中文经过url编码
# url编码后由 % 字母 和 数字组成  http://www.jsons.cn/urlencode
print(requests.utils.quote('风景'))  # 把中文进行url编码
print(requests.utils.unquote('%E9%A3%8E%E6%99%AF'))  # 将url编码形式进行解码