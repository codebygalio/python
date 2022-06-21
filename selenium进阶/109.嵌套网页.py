import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://music.163.com/#/song?id=1450083773')

# 当前这个网页有没有嵌套网页
"""进入嵌套网页有两种方式"""

"""方式1: 根据嵌套网页的索引今日到嵌套网页"""
# 所有嵌套网页的标签对应的是 <iframe>
# driver.switch_to 可以切换进入到嵌套网页
# switch_to.frame(0) 根据嵌套网页的顺序进入到嵌套网页
# frame(0)  根据索引今日到嵌套网页, 索引是从零开始的, 超出了当前嵌套网页的数量就会报错
# driver.switch_to.frame(1)

"""方式2: 根据嵌套网页的<iframe>标签对象进入到嵌套网页"""
iframe_label = driver.find_element(By.CSS_SELECTOR, '#g_iframe')
driver.switch_to.frame(iframe_label)
time.sleep(2)

driver.switch_to.parent_frame()  # 从子网页切换到父级网页

print(driver.page_source)
input()
driver.quit()

"""
登陆注册页面, 常见的情况
"""