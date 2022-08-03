import base64
import random
import re
import time
from PIL import Image

from selenium import webdriver
from selenium.webdriver import ChromeOptions


options = ChromeOptions()
# 禁用自动化栏
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(executable_path='../chromedriver.exe', options=options)
driver.maximize_window()
# 账户信息
username = '15140128843'
pwd = '123456'
url = 'https://union.jd.com/login'
# 打开浏览器网页
driver.get(url)
iframe = driver.find_element_by_css_selector('iframe')
print("切换到iframe")
driver.switch_to.frame(iframe)

"""模拟登陆"""
input_ele = driver.find_element_by_id("loginname")
input_ele.clear()

# 模拟认为输入账号密码
time.sleep(random.uniform(0.1, 0.5))
input_ele.send_keys(username[0:3])
time.sleep(random.uniform(0.5, 0.8))
input_ele.send_keys(username[3:])

# 模拟人输入密码
time.sleep(random.uniform(0.8, 1.2))
pwd_ele = driver.find_element_by_id("nloginpwd")
pwd_ele.clear()
pwd_ele.send_keys(pwd)

# 点击登录
print("点击登录")
time.sleep(random.uniform(0.2, 0.8))
login_ele = driver.find_element_by_id("paipaiLoginSubmit")
login_ele.click()

############################################
"""获取图片"""
"""下载图片到本地"""
time.sleep(3)
target = driver.find_element_by_css_selector('.JDJRV-bigimg img')
template = driver.find_element_by_css_selector('.JDJRV-smallimg img')

# 获取图片的 base64 数据
target_base64 = target.get_attribute('src')
template_base64 = template.get_attribute('src')

# 去掉格式内容
target_base64_str = re.sub(r'data:[a-z]*/[a-z]*;base64,', '', target_base64)
template_base64_str = re.sub(r'data:[a-z]*/[a-z]*;base64,', '', template_base64)


# 保存目标图片
target_img_name = 'target.png'
target_binary_content = base64.b64decode(target_base64_str)
with open(target_img_name, mode='wb') as f:
    f.write(target_binary_content)

# 保存模板图片
template_img_name = 'template.png'
template_binary_content = base64.b64decode(template_base64_str)
with open(template_img_name, mode='wb') as f:
    f.write(template_binary_content)


local_img = Image.open(target_img_name)
size_loc = local_img.size
zoom = 281 / int(size_loc[0])
print("计算缩放比例 zoom = %f" % round(zoom, 4))
