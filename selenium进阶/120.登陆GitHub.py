"""
目标网址: https://github.com/login 模拟登录

作业要求:
    1.用 selenium 模拟登录GitHub(首先自己注册一个账号)
温馨提示:
    这个网站加载速度很慢, 最好设置时间长一点的等待
请在下方编写代码
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 1.实例化浏览器对象
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# 2.请求网页数据
driver.get('https://github.com/login')
# print(driver.page_source)

"""模拟登陆"""
# 找到用户名输入框输入用户名
driver.find_element(By.CSS_SELECTOR, '#login_field').send_keys('zz')
time.sleep(3)

# 找到密码输入框输入密码
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('xx')
time.sleep(3)

# 点击登陆按钮
driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary.btn-block.js-sign-in-button').click()


input()
# 3.关闭浏览器
driver.quit()


