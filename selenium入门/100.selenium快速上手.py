# pip install selenium
from selenium import webdriver  # 导入浏览器功能

# 1. 实例化一个浏览器对象
driver = webdriver.Chrome()

# 2. 使用浏览器对象根据地址发送请求, 执行自动化
driver.get('https://www.baidu.com/')

input('我阻塞了浏览器的关闭')
# 3. 关闭浏览器
driver.quit()  # 退出浏览器

"""
一旦通过浏览器对象请求某个页面以后
咱们后续的一些列操作, 和我们平常操作浏览器的顺序是一样的
我们的代码逻辑顺序和我们操作浏览器的顺序也是大致一样的
"""

