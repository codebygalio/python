import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'Cookie': '_lxsdk_cuid=1755981708ec8-06c03062fd7db8-303464-1fa400-1755981708ec8; _lxsdk=1755981708ec8-06c03062fd7db8-303464-1fa400-1755981708ec8; _hc.v=65cda5c1-0a03-0f36-1de0-f01cbe490d2d.1603524457; ua=%E5%BF%99%E7%A2%8C%E7%9A%84%E8%BA%AF%E4%BD%93; ctu=c4cbf7c8dc53a7adc479157bd67df302c09b43065872e990f99f55425ecda108; cy=344; cye=changsha; fspop=test; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1603524457,1604321856,1604490910; dplet=5f0c0291347d5c1874e028665f458f67; dper=11dc7f78ecfeaa3b34db9a5bc08788b26d4c0925c3ede17591ab7a64175bed1a2190bb8bcac5a5b1ea493bf3b7a00e83a73605a88e07e1ad21630796e2be6b6eca39e888866442c8869551f1cd362815a3c3fb348b37f6491f386e23e466d6d0; ll=7fd06e815b796be3df069dec7836c3df; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1604491134; _lxsdk_s=175931c56d8-0a7-588-21f%7C%7C229',
    'Host': 'www.dianping.com'
}

url = "http://www.dianping.com/shop/130096343/review_all"

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
html = response.text
with open('-01 大众网址源码.html', mode='w', encoding='utf-8') as f:
    f.write(html)

# 请求网址，获取css样式文件地址
css_url = re.findall(
    'type="text/css" href="(//s3plus.meituan.net/v1/mss_\w+/svgtextcss/.*?\.css)"',
    html)[0]
css_url = 'http:' + css_url
print('css_url', css_url)
"""应该是获取所有的类名映射规则"""
# 请求 css 文件，匹配替换类名
# class 属性可能会发送变动
css_response = requests.get(css_url)
# 保存 css字体样式
with open('-02 字体映射关系.css', mode='wb') as f:
    f.write(css_response.content)

"""映射关系文档获取"""
svg_url = re.findall(r'svgmtsi.*?background-image: url\((.*?)\);', css_response.text, re.S)[0]
# 获取替换类的前缀
svg_prefix = re.findall(r'svgmtsi\[class\^="(\w+)"\]', css_response.text, re.S)[0]
svg_url = 'http:' + svg_url
print('svg_url', svg_url)
svg_response = requests.get(svg_url)
svg_response.encoding = 'utf-8'
svg_html = svg_response.text

#  .jjubsf{background:-140.0px -1739.0px;
pattern = re.compile('.(%s\w+)\{background:-(\d+\.\d+)px -(\d+\.\d+)px;\}' % svg_prefix)
class_map = re.findall(pattern, css_response.text)
class_map = [[cla_map[0], int(float(cla_map[1])), int(float(cla_map[2]))] for cla_map in class_map]
print('class_map', class_map)

# 保存 svg 映射关系
with open('-03 svg映射关系.html', mode='w', encoding='utf-8') as f:
    f.write(svg_html)
