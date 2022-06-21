from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  # 导入下拉框功能

driver = webdriver.Chrome()
driver.get('https://www.jq22.com/demo/shengshiliandong/')

# 找 <select> 标签对应的对象
sel = driver.find_element(By.CSS_SELECTOR, '#s_province')

# 实例化下拉框对象
select = Select(sel)

# 根据索引取下拉框, 从1开始
select.select_by_index(1)  # 北京市
time.sleep(3)

# 根据下拉框标签的 value取值
select.select_by_value('河北省')  # 河北省
time.sleep(3)

#  根据下拉框标签的文本取值
select.select_by_visible_text('吉林省')  # 吉林省

input()
driver.quit()