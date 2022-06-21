from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://gitee.com/')
driver.implicitly_wait(10)  # 隐式等待
driver.maximize_window()  # 最大化浏览器

driver.find_element(By.CSS_SELECTOR, '.item.git-nav-user__login-item').click()

driver.find_element(By.CSS_SELECTOR, '#git-login #user_login').send_keys('2535513449@qq.com')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#user_password').send_keys('hjx_3136419')
time.sleep(2)
driver.find_element(By.NAME, 'commit').click()

"""根据动作链执行坐标点击操作"""
from selenium.webdriver import ActionChains

time.sleep(2) # 需要强制等待, 因为页面跳转需要时间
ActionChains(driver).move_by_offset(1070, 850).click().perform()

input()
driver.quit()