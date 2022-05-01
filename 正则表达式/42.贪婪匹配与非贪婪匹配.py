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
贪婪匹配:  默认的匹配模式, 一次性尽可能多的匹配数据

.*?    非贪婪模式, 匹配一次返回一次
?      匹配1次或者0次
? 是非贪婪模式, 会尽可能少的匹配数
"""
result = re.findall('Super劫Zed: .*@qq.com', text, re.S)
print(result)
print(len(result))

result = re.findall('Super劫Zed: .*?@qq.com', text, re.S)
print(result)
