from selenium import webdriver

driver = webdriver.Chrome()

# 放到实例化浏览器对象后
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => false
    })
  """
})


driver.get('http://epub.cnipa.gov.cn/Ipc')
print(driver.page_source)

input()
driver.quit()

"""
    不是所有的检测方式都是这个, js检测
"""

