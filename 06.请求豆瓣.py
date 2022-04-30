# https://movie.douban.com/top250


"""
   
    Origin  资源的起始位置
    User-Agent  浏览器的身份标识
    Host    请求服务器的域名是哪个
    Referer 当前请求是从哪里过来的?
    Cookies 用户身份标识<能不加就不加>

"""

# 构建的请求头, 用于请求的伪装
import requests

headers = {
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cache-Control': 'no-cache',
    # 'Connection': 'keep-alive',
    # 'Cookie': 'bid=JOjnHzNKNdU; __gads=ID=390a3a70609550e8-22df6781f5d10053:T=1649854444:RT=1649854444:S=ALNI_MZfvUIHFs1pOYgYSuPbsvh7fVT9Yw; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1650026272%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DcKXgBx9eo7ttOSYASFpeklnrlErk1XVldUc1oJEediMeAuyaGW2gvQrSt78wZ_xo%26wd%3D%26eqid%3D8fb7ffa800080cd9000000066259671d%22%5D; _pk_id.100001.4cf6=5a00c88162b3f1ff.1649854444.3.1650026272.1649856678.; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1895635950.1649854444.1649856678.1650026272.3; __utmb=30149280.0.10.1650026272; __utmc=30149280; __utmz=30149280.1650026272.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.913704788.1649854444.1649856678.1650026272.3; __utmb=223695111.0.10.1650026272; __utmc=223695111; __utmz=223695111.1650026272.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    'Host': 'movie.douban.com',
    # 'Pragma': 'no-cache',
    'Referer': 'https://www.baidu.com/link?url=cKXgBx9eo7ttOSYASFpeklnrlErk1XVldUc1oJEediMeAuyaGW2gvQrSt78wZ_xo&wd=&eqid=8fb7ffa800080cd9000000066259671d',
    # 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'Sec-Fetch-Dest': 'document',
    # 'Sec-Fetch-Mode': 'navigate',
    # 'Sec-Fetch-Site': 'cross-site',
    # 'Sec-Fetch-User': '?1',
    # 'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
}

url = 'https://movie.douban.com/top250'
# 添加请求头参数, 指定请求头伪装
response = requests.get(url, headers=headers)
html_data = response.text
print(html_data)
