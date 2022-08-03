import requests
import re
from fontTools.ttLib import TTFont

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}
response = requests.get('https://book.qidian.com/info/1013919744', headers=headers)

with open('old.html', mode='w', encoding='utf-8') as f:
    f.write(response.text)

font_link = re.findall("format\('eot'\); src: url\('(.*?)'\) format\('woff'\),", response.text)
font_link = font_link[0]

response_woff = requests.get(font_link)
font_name = font_link.split('/')[-1]
with open(font_name, mode='wb') as f:
    f.write(response_woff.content)


base_font = TTFont(font_name)
# 将字体关系保存为 xml 格式
base_font.saveXML('font.xml')
# 获取映射规则
map_list = base_font.getBestCmap()
# 字符编码：字符内容
print(map_list)

# 需要把英文转化为中文
# 映射规则是不变了
eng_2_num = {
    'period': ".", 'two': '2',
    'zero': '0', 'five': '5',
    'nine': "9", 'seven': '7',
    'one': '1', 'three': '3',
    'six': '6', 'four': '4',
    'eight': '8'
}

for key in map_list.keys():
    map_list[key] = eng_2_num[map_list[key]]
print(map_list)

old_html = open('old.html', mode='r', encoding='utf-8').read()

for key, value in map_list.items():
    print(key, value)
    # &#100530;
    old_html = old_html.replace('&#'+str(key)+';', value)

with open('替换之后的代码.html', mode='w', encoding='utf-8') as f:
    f.write(old_html)

