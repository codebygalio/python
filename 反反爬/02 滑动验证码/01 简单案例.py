from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://member.zjtcn.com/common/login.html')
driver.maximize_window()
"""实现滑动操作"""

hover = driver.find_element_by_css_selector('.ui-slider-btn')

# 动作链（ActionChains）进行滑动
action = webdriver.ActionChains(driver)
# 点击并且不释放
action.click_and_hold(hover).perform()
# 移动 340 40

# 释放
action.release().perform()
