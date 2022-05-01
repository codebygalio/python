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
	<p class="top" id="contend">css标签选择器的介绍</p>
	<p class="top">标签选择器、类选择器、ID选择器</p>
	<a class="top" href="https://www.baidu.com"> 百度一下 </a>
	<span id="contend"> 我是一个span标签</span>
</body>
</html>
"""
import parsel


selector = parsel.Selector(html)

"""
:       表示伪类选择器, 在同级标签中选择第几个
(2) 选择满足条件的第二个, 从1开始数
伪类选择器功能也是定位标签, 后面跟上属性提取器
"""
result = selector.css('p:nth-child(2)::text').getall()
print(result)
