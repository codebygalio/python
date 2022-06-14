from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
time.sleep(3)

driver.get('http://news.baidu.com/')
time.sleep(3)

driver.back()  # 回退到上一个页面
time.sleep(3)

driver.forward()  # 前进到下一个页面
time.sleep(3)

driver.refresh()  # 刷新页面

input()
driver.quit()