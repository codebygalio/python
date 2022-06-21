from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
driver.implicitly_wait(10)

driver.switch_to.frame(0)

# 找到可以拖拽的标签
drag = driver.find_element(By.CSS_SELECTOR, '#draggable')
# 找到可以放置的标签
drop = driver.find_element(By.CSS_SELECTOR, '#droppable')

ActionChains(driver).drag_and_drop(drag, drop).perform()
"""弹窗的处理"""

alert = driver.switch_to.alert  # switch_to.alert 切换到弹窗
print(alert.text)  # 打印弹窗的文本


alert.accept()  # 接受可用的弹窗, 相当于点击确认
# alert.dismiss()  # 接受可用的弹窗, 相当于点击取消

input()
driver.quit()



