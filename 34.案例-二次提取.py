import requests
import parsel


response = requests.get('https://www.quge3.com/book/1031/')
data = response.text

# 解析数据

selector = parsel.Selector(data)

# 获取所有符合条件的标签  第一次提取
dds = selector.css('.listmain dl dd')
print(dds)

# 二次提取
for dd in dds:  # 遍历dds中每一个 Selector 对象
    title = dd.css('a::text').get()
    href = dd.css('a::attr(href)').get()
    print(title, href)




