from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.douban.com/')

driver.find_element(By.CSS_SELECTOR, '#anony-nav ul>li:nth-child(1)>a').click()

# window_handles 获取浏览器所有页面, 返回窗口列表
windows = driver.window_handles
print(windows)

time.sleep(3)

# switch_to 跳转
driver.switch_to.window(windows[0])


input()
driver.quit()