import re

text = """
哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 540775360@qq.com
Super劫Zed: 2535513449@qq.com
Super劫Zed: 123456789@qq.com
2018-8-8 16:00回复
我也说一句
"""

"""
精确匹配: 首先会根据正则的语法匹配数据, 然后进行精确提取 
()      表示精确匹配, 匹配到数据后图区括号内的数据
"""
result = re.findall('Super劫Zed: (.*?)@qq.com', text, re.S)
print(result)
