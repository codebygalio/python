import requests


url = 'http://www.gebiqu.com/biquge_207056/44547067.html'
response = requests.get(url)
print(response.status_code)

# 状态码: 申明请求的状态
"""
100 - 200   表示服务器成功的接受到了请求
200 - 299   表示请求成功
300 - 399   重定向(你需要请求的一个资源已经移动到了另外一个位置)
400 - 499   请求的地址在服务器中找不到资源<检查地址是否正确>
500 - 599   服务器内部错误, 是服务器的问题
"""