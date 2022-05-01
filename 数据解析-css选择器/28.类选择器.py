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
	<p class="top">css标签选择器的介绍</p>
	<p class="top">标签选择器、类选择器、ID选择器</p>
	<a class="top" href="https://www.baidu.com"> 百度一下 </a>
	<span> 我是一个span标签</span>
</body>
</html>
"""
import parsel


selector = parsel.Selector(html)

"""
只有标签具有 class 属性, name才可以用类选择器进行解析提取
.   代表根据类属性提取
具有相同类属性的标签都会被提取
类选择器可以通过标签的类属性(class 属性)精确定位到你想要的标签
"""
result = selector.css('.top').getall()
print(result)
