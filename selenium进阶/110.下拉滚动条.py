import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.douban.com/')

"""执行浏览器的下拉操作"""
# 定义js语法
# document.documentElement.scrollTop  指定滚动条的位置, 适合固定长度的浏览器页面
# document.documentElement.scrollHeight 获取当前页面的最大高度
js = 'document.documentElement.scrollTop=2000'
js_all = 'document.documentElement.scrollTop = document.documentElement.scrollHeight'

# 执行js语法
driver.execute_script(js_all)

input()
driver.quit()

"""
登陆注册页面, 常见的情况
"""