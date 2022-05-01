text = """
回复(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 540775360@qq.com
2018-8-8 16:00回复
我也说一句

RAVV2017
物联硕士4
以上的邮箱，已发，还需要的请回复邮箱。两套物联网学习资料。

回复(4)7楼2018-07-04 16:06

儒雅的刘飞3
初识物联1
397872410@qq.com，谢谢楼主

收起回复8楼2018-07-04 16:20

RAVV2017: 已发送，麻烦请查收，谢谢
2018-7-4 16:23回复
我也说一句

该来的总会来
物联博士5
1459543548@qq.com
谢谢谢谢

回复9楼2018-07-04 17:18来自Android客户端
BLACKPINK_罗捷
深入物联2
1228074244@qq.com
"""

import re

"""
.    在默认的模式下, 能够匹配除了换行符以外的任意字符
re. S  能够让 . 匹配匹配到换行符
一个点只能匹配一个字符串
如果没有加 () , 那么约束字符也会返回结果
"""
result = re.findall('Super劫Zed: ................', text)
print(result)

"""
\d  匹配一个数字字符
\D  匹配一个非数字字符
"""
result = re.findall('Super劫Zed: \d\d\d\d\d\d\d\d\d', text)
print(result)
result = re.findall('Super劫Zed: \d\d\d\d\d\d\d\d\d\D\D\D\D\D\D\D\D', text)
print(result)
print('-' *50)

"""
\s  匹配一个空白字符(换行 制表符 tab键)
\S  匹配一个非空白字符
"""
# findall 会返回所有符合条件的字符串
result = re.findall('\s', text)
print(result)
result = re.findall('\S', text)
print(result)
print('-' *50)


"""
\w  匹配单词字符  a-z A-Z _ 各个国家地区的语言文字
\W  匹配非单词字符  

"""
result = re.findall('\w', text)
print(result)
result = re.findall('\W', text)
print(result)
print('-' *50)


"""
*   匹配前一个字符的零次或者多次(字符最少出现的次数可以是零次)
+   匹配前一个字符的一次或者多次(字符最少出现的次数是1次)

.*  匹配零次或者多次
.+  匹配一次或者多次
"""

result = re.findall('Super劫Zed: \d*', text)
print(result)
result = re.findall('Super劫Zed: \d+', text)
print(result)


result = re.findall('Super劫Zed: \s*', text)
print(result)
result = re.findall('Super劫Zed: \s+', text)
print(result)

