import re
import requests
from fontTools.ttLib import TTFont


import numpy
from PIL import Image, ImageFont, ImageDraw


import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Cookie': '_lxsdk_cuid=175452aed4ac8-01969ffff888bb-5d462912-1fa400-175452aed4bc8; _lxsdk=175452aed4ac8-01969ffff888bb-5d462912-1fa400-175452aed4bc8; _hc.v=96aa71e1-8382-03c7-34df-9c6aa741c57c.1603183243; ctu=c4cbf7c8dc53a7adc479157bd67df302cebc68955c5409b35ba4244155865f45; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1603183243,1603194143; cye=changsha; cy=344; fspop=test; dplet=f2ffc70afac18217e257fd4ec422455c; dper=11dc7f78ecfeaa3b34db9a5bc08788b2d5641601db1284b6d92492bca49b136ed4db3b8d28d4f99043eb815e679b83283966a6ca705460c480c5fcec22cde12a6fef9c231ee15963047be204470f7ada61897937fd9b50ad6cbbf6a5814fb225; ll=7fd06e815b796be3df069dec7836c3df; ua=%E5%BF%99%E7%A2%8C%E7%9A%84%E8%BA%AF%E4%BD%93; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1603197098; _lxsdk_s=17545c65498-8cd-73-e7a%7C%7C397',
    'Host': 'www.dianping.com'
}


# 请求网页，获取下载数据
url = 'http://www.dianping.com/shop/22314796'
response = requests.get(url, headers=headers)
html = response.text
with open('替换数据之前.html', mode='w', encoding='utf-8') as f:
    f.write(html)

# TODO 下载css文件
# 请求css 获取字体下载地址
css_url = re.findall('//s3plus.meituan.net/v1/mss_\w+/svgtextcss/.*?\.css', html)
css_url = 'https:' + css_url[0]
# 下载css文件，获取字体文件
css_response = requests.get(css_url)
print('css下载地址', css_url)
print('css文件内容：', css_response.text)

# TODO 下载字体文件
# 取css文件里面匹配字体的下载链接
# @font-face\{font-family: "PingFangSC-Regular-review";.*?,url\("(.*?)"\);}
font_url = re.findall('@font-face\{font-family: "PingFangSC-Regular-review";.*?format.*?,url\("(.*?)"\);\}', css_response.text)
font_url = font_url[0]
# 获取字体的文件名
font_name = font_url.split('/')[-1]

# 下载并保存字体文件
font_response = requests.get('https:' + font_url)
with open(font_name, mode='wb') as f:
    f.write(font_response.content)

font_path = font_name
# 打开文件
font = TTFont(font_path)
font.saveXML('大众-字体.xml')
# 获取字体编码（特殊的编码）
code_list = font.getGlyphOrder()[2:]
print(code_list)

"""将字体绘制到图片 用于 ocr 识图"""
# 新建一张图片
im = Image.new("RGB", (1800, 1800), (255, 255, 255))
image_draw = ImageDraw.Draw(im)
# 绘制图片中, 显示的字体
font = ImageFont.truetype(font_path, 40)
count = 15
# 将需要转化的内容划分15等份， 否则会绘制在一行
array_list = numpy.array_split(code_list, count)

for i in range(len(array_list)):
    print('替换之前的', array_list[i])
    # 将js的unicode码转化为python的unicode 'unif6e8'  \\uf6e8
    new_list = [i.replace("uni", "\\u") for i in array_list[i]]
    print('替换之后的', new_list)

    # 将列表变为字符串
    text = "".join(new_list)
    print('列表变字符串', text)
    # encode decode
    # 把文字变成二进制
    # 将字符串进行反向编码
    text = text.encode('utf-8').decode('unicode_escape')
    print('反向编码之后的', text)
    # 将文件绘制到图片
    # 指定字体进行绘制
    image_draw.text((0, 100 * i), text, font=font, fill="#000000")
#
im.save("sss.jpg")  # 可以将图片保存到本地，以便于手动打开图片查看
# im.show()

result = pytesseract.image_to_string(im, lang="chi_sim")
print('ocr 识别出来的内容', result)
# 去除空白及换行
result_str = result.replace(" ", "").replace("\n", "")
# 将内容替换成网页的格式，准备去网页中进行替换
print(result_str)
print(code_list)
html_code_list = [i.replace("uni", "&#x") + ";" for i in code_list]

print(html_code_list)
map_dict = dict(zip(html_code_list, list(result_str)))
print(map_dict)

with open('替换数据之前.html', mode='r', encoding='utf-8') as f:
    text = f.read()

for key, value in map_dict.items():
    # print(key, value)
    text = text.replace(key, value)

with open('替换数据之后.html', mode='w', encoding='utf-8') as f:
    f.write(text)
