import re

text = """
哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 5407753123456748960@qq.com
Super劫Zed: 2535513449@qq.com
Super劫Zed: 6789@qq.com
2018-8-8 16:00回复
我也说一句
"""

result = re.findall('\d*@qq.com', text, re.S)
print(result)


"""
{起始范围, 结束范围}  闭区间, 限制的前一个元字符匹配的个数
"""
result = re.findall('\d{5,11}@qq.com', text, re.S)
print(result)
