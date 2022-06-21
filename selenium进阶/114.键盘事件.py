# 在百度搜索框输入 python ，全选,复制,剪切,粘贴 跳转到搜狗输入框进行搜索
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys  # 导入键盘事件功能

# 在百度搜索框输入 python ，全选,复制,剪切,粘贴 跳转到搜狗输入框进行搜索
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 所有的键盘事件都是基于标签对象调用的
driver.find_element(By.CSS_SELECTOR, '#kw').send_keys('python')
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, '#kw').send_keys(Keys.CONTROL, 'a')  # 全选
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, '#kw').send_keys(Keys.CONTROL, 'c')  # 复制
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, '#kw').send_keys(Keys.CONTROL, 'x')  # 剪切
time.sleep(3)


driver.get('https://www.sogou.com/')

driver.find_element(By.CSS_SELECTOR, '#query').send_keys(Keys.CONTROL, 'v')  # 粘贴
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, '#query').send_keys(Keys.ENTER)  # 回车

input()
driver.quit()