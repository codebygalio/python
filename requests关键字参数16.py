import requests

url = 'https://m.maoyan.com/board/4'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
}

response = requests.get(url=url, headers=headers)
"""
method: 请求方法 get post
url: 请求的地址

headers: (可选参数) 请求头字段参数(字典)
cookies: (可选参数) 可以用此参数传递cookies字段
proxies: (可选参数) ip代理的关键字参数, 服务器在响应数据的时候会拿到请求计算机的ip

params: (可选参数) 指定查询参数, 构建成字典
data: (可选参数) 指定请求参数, 构建成字典, 一般用于post请求
json: (可选参数) 请求的时候提交json数据向服务器请求, 一般用于post请求

timeout: (可选参数) 设置响应数据的时间, 一旦超过这个时间, 程序会报错
allow_redirects: (可选参数) 是否允许重定向, 300左右  http协议一下会自动重定向
verify: (可选参数) 是否验证证书<公钥 私钥>, http会默认验证证书, 可以关闭<True, False>

files: (可选参数) 提交文件
auth: (可选参数) 权限认证
"""
