from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://gitee.com/')
driver.implicitly_wait(10)  # 隐式等待
driver.maximize_window()  # 最大化浏览器

"""找到登陆按钮点击, 进入到登陆页面"""
driver.find_element(By.CSS_SELECTOR, '.item.git-nav-user__login-item').click()

"""输入用户名及密码, 点击登陆按钮"""
# 找到用户名输入框输入用户名
driver.find_element(By.CSS_SELECTOR, '#git-login #user_login').send_keys('2535513449@qq.com')
time.sleep(2)

# # 找到密码输入框输入密码
driver.find_element(By.CSS_SELECTOR, '#user_password').send_keys('hjx_3136419')
time.sleep(2)

# 点击登陆按钮
driver.find_element(By.NAME, 'commit').click()


"""获取登陆以后的cookies"""
print(driver.get_cookies())

cookies_dict = {}
for dict_ in driver.get_cookies():
    cookies_dict.update(dict_)

print(cookies_dict)

input()
driver.quit()