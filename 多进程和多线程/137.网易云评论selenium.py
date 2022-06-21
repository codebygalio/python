"""
目标网址:https://music.163.com/#/playlist?id=924680166

要求:
	1. 使用selenium
	2. 爬取前面5页的评论数据保存为txt文件
"""
import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def parse_data():
    """解析数据并且保存"""
    divs = driver.find_elements(By.CSS_SELECTOR, '.itm')

    for div in divs:
        cnt = div.find_element(By.CSS_SELECTOR, '.cnt.f-brk').text
        cnt = cnt.replace('\n', '')
        cnt = re.findall('：(.*)', cnt)[0]
        print(cnt)

        with open('contend.txt', mode='a', encoding='utf-8') as f:
            f.write(cnt + '\n')


driver = webdriver.Chrome()
driver.get('https://music.163.com/#/playlist?id=924680166')

# 切换进入到嵌套网页
driver.switch_to.frame(0)
print(driver.page_source)


for i in range(5):
    js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight'
    driver.execute_script(js)

    # 解析数据
    parse_data()
    # 点击下一页
    driver.find_element(By.CSS_SELECTOR, '.zbtn.znxt').click()
    time.sleep(2)

input()
driver.quit()


