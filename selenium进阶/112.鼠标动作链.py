from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
driver.implicitly_wait(10)

driver.switch_to.frame(0)

# 找到可以拖拽的标签
drag = driver.find_element(By.CSS_SELECTOR, '#draggable')
# 找到可以放置的标签
drop = driver.find_element(By.CSS_SELECTOR, '#droppable')

"""根据动作链对象, 执行鼠标操作"""
# 1. 导入动作链对象
from selenium.webdriver import ActionChains
#
# # 2. 实例化一个动作链对象, 需要把浏览器对象绑定到动作链对象上
# action = ActionChains(driver)
#
# # 3. 根据动作链对象定义一个动作, 但是此动作还没有执行
# action.drag_and_drop(drag, drop)  # 把 drag 移动到 drop元素上
#
# # 4.执行动作链
# action.perform()

ActionChains(driver).drag_and_drop(drag, drop).perform()



input()
driver.quit()



