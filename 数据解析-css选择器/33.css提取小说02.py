import requests
import parsel


response = requests.get('https://www.bige3.com/book/1031/1.html')
data = response.text

# 解析数据
# 1.转化数据类型
selector = parsel.Selector(data)
# 2. 根据对象提取数据
result = selector.css('.content>h1.wap_none::text').get()
print(result)


# 一旦html中有br标签在提取的标签里面, 就需要用 getall() 获取标签数据
result2 = selector.css('#chaptercontent::text').getall()
print(result2)



