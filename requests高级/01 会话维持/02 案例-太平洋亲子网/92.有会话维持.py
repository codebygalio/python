
"""
个人中心地址: https://my.pcbaby.com.cn/user/adminIndex.jsp
"""

import requests

session = requests.Session()

"""1, 发送登陆的请求, 获取用户登陆的状态"""
data = {
    'return': 'https://my.pcbaby.com.cn/user/msg.jsp',
    'bindUrl': 'https://my.pcbaby.com.cn/passport/bindMobile.jsp?return=https://my.pcbaby.com.cn/user/msg.jsp',
    'username': 'mb51222353',
    'password': '123456..',
    'auto_login': '30',
    'checkbox': 'on',
}

login_url = 'https://passport3.pcbaby.com.cn/passport3/passport/login_ajax_do_new.jsp?req_enc=UTF-8'
# 发送post登陆请求
login_response = session.post(url=login_url, data=data)
print(login_response.status_code)


"""2, 使用会话维持对象请求个人中心页面"""
my_home_url = 'https://my.pcbaby.com.cn/user/adminIndex.jsp'
response_my = session.get(url=my_home_url)
# print(response.text)
print(response_my.status_code)

with open('我的个人中心页面.html', mode='w', encoding='gb2312') as f:
    f.write(response_my.text)

"""
会话维持
    维持用户登陆的状态, 请求需要用户状态权限的网页
"""

