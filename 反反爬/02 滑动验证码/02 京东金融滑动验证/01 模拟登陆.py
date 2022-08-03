import random
import time

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
