"""
	目标地址：https://m.maoyan.com/board/4
	
	要求：
		1、请求到目标网址数据，需要在请求到的数据中看到当前页面所有的电影名字、主演、上映时间、评分等信息
		2、请列举在请求不到数据时，需要添加几个常见请求头字段

"""
import requests

url = 'https://m.maoyan.com/board/4'

headers = {
    # 'Cookie': 'uuid_n_v=v1; iuuid=9DED7A10B17C11ECB1EFC3BD08D8135DA8FA319C52714E4EBC6C74008CD8840E; ci=70%2C%E9%95%BF%E6%B2%99; ci=70%2C%E9%95%BF%E6%B2%99; ci=70%2C%E9%95%BF%E6%B2%99; webp=true; featrues=[object Object]; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1648790933,1650281353; _last_page=undefined; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1650281399; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=1803c6fc140c8-03e4923d825316-1734337f-1fa400-1803c6fc140c8; _lxsdk=DFFB9DB0BF0A11ECBDA61BE9D6AD8C6B46968BD137A143C489E0C13CD5AFC540; _lxsdk_s=1803c6fc141-d78-e7c-fc7%7C%7C3',
    # 'Host': 'm.maoyan.com',
    # 'Referer': 'https://www.baidu.com/link?url=UAGzcgsZD1cj39dE353A2BA3lO3UcVfrECMBkUte3PyCYykYDB5jwbJNwz3UEtfK&wd=&eqid=e16708fa00095e2700000006625d4bac',
    # 服务器在后台会校验的一个请求头字段
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
}

response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding
html_data = response.text
print(html_data)

"""
Cookie: 用户身份标识, 能不加尽量不要加
Host: 请求服务器的域名
Referer: 防盗链(告诉服务器,你是从哪一个页面跳转过来的)
User-Agent: 浏览器的身份标识
Origin: 资源起始位置  根目录
"""

# sign: 此字段有可能加密
