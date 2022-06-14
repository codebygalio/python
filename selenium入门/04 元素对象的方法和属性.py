from selenium import webdriver
from selenium.webdriver.common.by import By  # 导入定位器功能

driver = webdriver.Chrome()
driver.get('https://www.douban.com/')

"""
text    标签对象的属性, 可以根据标签对象提取包含的文本内容, 支持链式调用
"""
# result7 = driver.find_element(By.CSS_SELECTOR, '.lnk-app')
# print(result7)
# print(result7.text)
result7 = driver.find_element(By.CSS_SELECTOR, '.lnk-app').text

print(result7)

"""
get_attribute(属性名)
    方法, 根据属性名获取标签的属性值
"""
result7 = driver.find_element(By.CSS_SELECTOR, '.lnk-app').get_attribute('href')
print(result7)

"""输入框操作"""
"""
send_keys(数入内容)
    根据输入框标签对象, 在输入框中输入关键字
    支持链式调用
"""
driver.find_element(By.CSS_SELECTOR, '.inp>input').send_keys('奇迹笨小孩')


"""点击操作"""
"""
click()   执行标签对象的点击事件操作, 支持链式调用
"""
driver.find_element(By.CSS_SELECTOR, '.bn>input').click()


input()
driver.quit()