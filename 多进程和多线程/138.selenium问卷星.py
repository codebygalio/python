import random
import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => false
    })
  """
})
driver.get('https://www.wjx.cn/jq/87910206.aspx')

"""
一个题目一个题目的选择
"""

"""
单选题: [0,1,2,3,4,5,6,7,8,9]
多选题: [10, 11]
"""

divs = driver.find_elements(By.CSS_SELECTOR, '.div_question')
print(divs)

one_choice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 先解决单选题
for i in one_choice:
    lis = divs[i].find_elements(By.CSS_SELECTOR, 'ul li')
    # 随机选择一个
    random.choice(lis).click()  # 随机点击

# 解决多选题
any_choice = [10, 11]
for j in any_choice:
    lis = divs[j].find_elements(By.CSS_SELECTOR, 'ul li')
    # 随机选择三个  # sample 随机选择不同的的元素
    lis_result = random.sample(lis, k=3)  # k=3 随机在 lis 中选择三项
    for k in lis_result:
        k.click()


# 点击提交
driver.find_element(By.CSS_SELECTOR, '#submit_button').click()
time.sleep(3)

# 点击人机验证
driver.find_element(By.CSS_SELECTOR, '.sm-ico .sm-ico-wave').click()
time.sleep(3)


input()
driver.quit()
