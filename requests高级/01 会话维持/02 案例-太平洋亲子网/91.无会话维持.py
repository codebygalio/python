
"""
个人中心地址: https://my.pcbaby.com.cn/user/adminIndex.jsp
"""

import requests

my_home_url = 'https://my.pcbaby.com.cn/user/adminIndex.jsp'
response = requests.get(url=my_home_url, allow_redirects=False)
print(response.text)
print(response.status_code)

with open('my.html', mode='w', encoding='gb2312') as f:
    f.write(response.text)

