import requests


url = 'http://www.gebiqu.com/biquge_207056/44547067.html'
response = requests.get(url)
"""
response.encoding  指定响应体编码
apparent_encoding  自动获取响应体编码
"""
# response.encoding = response.apparent_encoding  # 自定识别响应体编码

response.encoding = 'utf-8'  # 手动查询指定编码
print(response.text)