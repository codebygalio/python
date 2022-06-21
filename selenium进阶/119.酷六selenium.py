"""
目标网址: https://www.ku6.com/detail/71

作业要求:
    1.用 selenium 采集所需要的数据
    2.需要数据如下所示
        title 视频的标题
        img_url 视频图片对应的url地址
        detail_url 视频详情页url地址
    3.保存为csv数据
请在下方编写代码
"""
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By

# 1.实例化浏览器对象
driver = webdriver.Chrome()

# 2.请求网页数据
driver.get('https://www.ku6.com/detail/71')
# print(driver.page_source)

"""数据提取和解析"""
# 二次解析
divs = driver.find_elements(By.CSS_SELECTOR, '.video-item')
print(divs)
print(len(divs))

for div in divs:
    title = div.find_element(By.CSS_SELECTOR, 'h3>a').text
    img_url = div.find_element(By.CSS_SELECTOR, '.video-image-warp>img').get_attribute('src')
    detail_url = div.find_element(By.CSS_SELECTOR, '.video-image-warp').get_attribute('href')
    print(title, img_url, detail_url, sep=' | ')

    with open('data.csv', mode='a', encoding='utf-8', newline='') as f:
        csv_write = csv.writer(f)
        csv_write.writerow([title, img_url, detail_url])



input()
# 3.关闭浏览器
driver.quit()


