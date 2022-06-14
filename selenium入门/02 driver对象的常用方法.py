import time

from selenium import webdriver  # 导入浏览器功能

driver = webdriver.Chrome()

# get()  通过driver对象请求指定网址的网页
driver.get('https://www.baidu.com/')

# save_screenshot()  截取网页页面图片, 括号内部指定图片的名字
driver.save_screenshot('百度.png')

# page_source 查看请求页面渲染以后的数据
# 使用selenium获取的数据以代码获取的数据为准
# print(driver.page_source)

# with open('a.html', mode='w', encoding='utf-8') as f:
#     f.write(driver.page_source)

# get_cookies() 查看页面请求以后的 cookies, 常用与模拟登陆后获取cookies值
print(driver.get_cookies())

print(driver.current_url)  # 查看当前页面的url地址

driver.maximize_window()  # 最大化浏览器

time.sleep(3)

driver.minimize_window()  # 最小化浏览器

input('我阻塞了浏览器的关闭')
driver.quit()  # 退出浏览器


