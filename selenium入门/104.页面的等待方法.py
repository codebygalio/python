from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.jd.com/')

# 隐式等待
# 智能化等待, 在设置的时间之前加载完了, 那么不会死等下去
# 超过时间会报错
# 隐式等待只需设置一次，后面的代码都遵循这个规则
driver.implicitly_wait(10)

# 强制等待, 死等, 针对动态渲染数据的网站会用到
time.sleep(3)

result = driver.find_element(By.CSS_SELECTOR, '#navitems-group1>li:nth-child(3)>a').text
print(result)


input()
driver.quit()