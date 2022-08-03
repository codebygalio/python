"""
GET http://api.cportal.cctv.com/api/rest/articleInfo?id=ArtiBwZ7JgNhEbzEwY9bHzmW190101&cb=test.setMyArticalContent HTTP/1.1
Host: api.cportal.cctv.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Linux; Android 5.1.1; SEA-AL10 Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 CntvNews
Accept: */*
Referer: http://app.cctv.com/special/cportal/detail/arti/index.html?id=ArtiBwZ7JgNhEbzEwY9bHzmW190101&isfromapp=1&version=808&allow_comment=1
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,en-US;q=0.8
Cookie: cna=yVQgGD4kRk0CAa8K7pKzSJ2F; sca=340926b0
X-Requested-With: cn.cntvnews
"""
import requests
import pprint
import parsel
article_url = 'http://api.cportal.cctv.com/api/rest/articleInfo'

params = {
    'id': 'ArtiBwZ7JgNhEbzEwY9bHzmW190101',
    # 'cb': 'test.setMyArticalContent'
}

headers = {
    "Host": "api.cportal.cctv.com",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SEA-AL10 Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 CntvNews",
    "Accept": "*/*",
    "Referer": "http://app.cctv.com/special/cportal/detail/arti/index.html?id=ArtiBwZ7JgNhEbzEwY9bHzmW190101&isfromapp=1&version=808&allow_comment=1",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,en-US;q=0.8",
    "Cookie": "cna=yVQgGD4kRk0CAa8K7pKzSJ2F; sca=340926b0",
    "X-Requested-With": "cn.cntvnews",
}


response = requests.get(article_url, params=params, headers=headers)
# print(response.text)
data = response.json()
# pprint.pprint(response.json())
html = data['content']
# print(html)
sel = parsel.Selector(html)

text = sel.css('::text').getall()
print("\n".join(text))
