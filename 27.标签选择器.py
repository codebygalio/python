# 简化的html标签
html = """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>标签选择器</title>
</head>
<style>
	p{
		color: #f00;
		font-size: 16px;
	}
</style>
<body>
	<p>css标签选择器的介绍</p>
	<p>标签选择器、类选择器、ID选择器</p>
	<a href="https://www.baidu.com">百度一下</a>
	<span> 我是一个span标签</span>
</body>
</html>
"""
# 数据解析模块, 内置 css选择器,xpath,正则
# bs4 lxml ...
import parsel  # 第三方模块, pip install parsel


# 1. 转换数据类型  str --> object<对象>
selector = parsel.Selector(html)
# print(selector)

# 2.根据转换的对象调用方法提取, object<对象>就具有数据解析的方法
"""
p   在css语法中, 是用标签的名字解析, 取值, 取出来的内容任然是一个对象<Selector>
    解析所有符合规则的标签

get()       从解析的数据中返回第一个数据, 并且直接返回第一个标签对应的字符串
getall()    从解析的数据中返回所有符合条件的标签, 返回的是一个列表
"""
# result = selector.css('p').get()
result = selector.css('a').getall()
print(result)
print(type(result))