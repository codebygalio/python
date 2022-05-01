import re

text = """
哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 5407753123@qq.com
Super劫Zed: 0535513449@qq.com
Super劫Zed: 1789344934@qq.com
2018-8-8 16:00回复
我也说一句
"""
# QQ号正则
result = re.findall('[0123456789]*@qq.com', text, re.S)
print(result)
result = re.findall('[123456789][0123456789]*@qq.com', text, re.S)
print(result)
result = re.findall('[1-9][0-9]*@qq.com', text, re.S)
print(result)

# result = re.findall('[1-9]\\d{4,10}', text, re.S)
# print(result)

