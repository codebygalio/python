from selenium import webdriver
from selenium.webdriver.common.by import By  # 导入定位器功能

driver = webdriver.Chrome()
driver.get('https://www.douban.com/')

# print(driver.page_source)
"""定位标签"""  # 根据方法定位标签返回的都是标签对象  <selenium.webdriver.remote.webelement.WebElement
# 根据标签的 id 属性值定位标签
result = driver.find_element(By.ID, 'anony-sns')
print(result)

# 根据标签的 name 属性值定位标签
result2 = driver.find_element(By.NAME, 'description')
print(result2)

# 根据标签的 class 属性值定位标签
result3 = driver.find_element(By.CLASS_NAME, 'anony-nav-links')
print(result3)

# 根据标签包含的文本内容获取标签(精确匹配)
result4 = driver.find_element(By.LINK_TEXT, '下载豆瓣 App')
print(result4)

# 根据标签包含的文本内容获取标签(模糊匹配)
result5 = driver.find_element(By.PARTIAL_LINK_TEXT, '豆瓣')
print(result5)

print('-' * 50)
# 根据标签的名字获取标签
# find_elements 根据规则获取符合规则的所有标签
result6 = driver.find_elements(By.TAG_NAME, 'div')
print(result6)
print(len(result6))

# 根据css选择器定位标签, 只能定位标签, 不能通过css语法取标签包含的文本以及属性值
result7 = driver.find_elements(By.CSS_SELECTOR, '.lnk-app')
print(result7)

# 根据xpath定位标签, 只能定位标签, 不能通过xpath语法取标签包含的文本以及属性值
result8 = driver.find_elements(By.XPATH, '//div[@class="anony-nav-links"]/ul/li[1]/a')
print(result8)





input()
driver.quit()