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
::      表示属性提取器, 当获取到标签以后, 对标签特定的内容进行提取(标签包含的内容, 标签的属性值)
text    提取标签包含的文本
"""
result = selector.css('a::text').getall()
# print(result)

"""
::attr(href)        根据标签中包含的属性名字提取属性值
href                属性名字
"""
result2 = selector.css('a::attr(href)').getall()
print(result2)