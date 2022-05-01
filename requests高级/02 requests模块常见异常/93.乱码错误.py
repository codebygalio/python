import requests


url = 'https://www.shuquge.com/txt/8659/index.html'

response = requests.get(url=url)
response.encoding = 'utf-8'  # 指定响应体编码
html_data = response.text
print(html_data)

# response.encoding = response.apparent_encoding  # 自动识别响应体编码
# response.encoding = 'utf-8'