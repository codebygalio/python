import requests

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/84.0.4128.3 Safari/537.36'
	}
response = requests.get('http://www.shuquge.com/txt/8659/index.html', headers=headers)
response.encoding = response.apparent_encoding
html = response.text
print(html)

"""
请求头参数中, 空格不能多不能少
"""