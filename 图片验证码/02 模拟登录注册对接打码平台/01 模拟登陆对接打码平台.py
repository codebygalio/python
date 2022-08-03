import requests

#  创建一个会话维持对象, 接下来所有的请求可以用会话维持对象请求, 去维持咱们用户状态
session = requests.Session()

"""请求验证码保存"""
img_url = 'http://admin.qingdengedu.com/passport/getCaptcha?0.2911440945152233'
cookies = {'Cookie': 'session=eyJfZmxhc2hlcyI6W3siIHQiOlsibWVzc2FnZSIsIuivt-eZu-W9leS7peiuv-mXruatpOmhtemdoiJdfV0sIl9mcmVzaCI6ZmFsc2UsImNvZGUiOiIxNDQxIn0.YmvgTA.WU3Px3iQOLV3v9dFrzATKSCJ7cs'}
# 在第一次请求的时候携带cookies
response = session.get(url=img_url, cookies=cookies)
img_data = response.content
print('第一次请求的cookies:', response.cookies.get_dict())

with open('yzm.jpg', mode='wb') as f:
    f.write(img_data)

# """手动输入验证码"""
# code = input('请输入验证码:')
# print('您输入的验证码为:', code)

"""自动识别验证码"""
from img_parsel import base64_api  # 导入识别验证码的函数
result = base64_api('yzm.jpg')
print('验证码识别结果:', result)

"""发送模拟登陆的请求"""
# 构建请求参数
data = {
'username': 'admin',
'password': '123456',
'captcha': result
}

login_url = 'http://admin.qingdengedu.com/api/v1/passport/login'
# 在第二次请求的时候, 携带第一次响应返回的cookies
login_response = session.post(url=login_url, data=data)
print(login_response.json())