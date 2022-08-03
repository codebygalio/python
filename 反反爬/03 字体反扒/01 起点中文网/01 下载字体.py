import requests
import re

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


