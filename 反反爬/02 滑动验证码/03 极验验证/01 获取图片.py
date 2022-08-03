import random
import re
import time
from io import BytesIO

import requests
from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='../chromedriver.exe')
driver.maximize_window()
driver.get('http://www.cnbaowen.net/api/geetest/')

# 获取拖拽对象
# 等待拖拽对象出现
try:
    hover_element = WebDriverWait(driver, 30, 0.5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'gt_slider_knob'))
    )
except TimeoutException as e:
    print("超时错误")

""" 1. 获取完整的图片的信息 """
# 获取图片地址
full_image = driver.find_elements_by_css_selector('.gt_cut_fullbg div')
# print(full_image)
# 图片位置信息
full_location_list = []
# 获取图片碎片
for background_image in full_image:
    # 当前碎片位置
    location = {}
    # 匹配当前图片碎片的地址，位置
    result = re.findall('background-image: url\("(.*?)"\); background-position: (.*?)px (.*?)px;',
                        background_image.get_attribute('style'))
    # print(result)
    location['x'] = int(result[0][1])
    location['y'] = int(result[0][2])

    full_image_url = result[0][0]
    # 将当前碎片信息添加到图片位置信息列表
    full_location_list.append(location)

# '替换url http://static.geetest.com/pictures/gt/579066de6/579066de6.webp'
full_image_url = full_image_url.replace('webp', 'jpg')

image_result = requests.get(full_image_url).content
with open('full_image.jpg', 'wb') as f:
    f.write(image_result)
# 是一张无序的图片
print('full_location_list', full_location_list)

""" 2. 获取缺少模板的图片的信息 """
cut_image = driver.find_elements_by_css_selector('.gt_cut_bg div')
print(cut_image)
# 图片位置信息
cut_location_list = []
# 获取图片碎片
for background_image in cut_image:
    # 当前碎片位置
    location = {}
    # 匹配当前图片碎片的地址，位置
    result = re.findall('background-image: url\("(.*?)"\); background-position: (.*?)px (.*?)px;',
                        background_image.get_attribute('style'))
    # print(result)
    location['x'] = int(result[0][1])
    location['y'] = int(result[0][2])

    cut_image_url = result[0][0]
    # 将当前碎片信息添加到图片位置信息列表
    cut_location_list.append(location)

cut_image_url = cut_image_url.replace('webp', 'jpg')
# '替换url http://static.geetest.com/pictures/gt/579066de6/579066de6.webp'
image_result = requests.get(cut_image_url).content
with open('cut_image.jpg', 'wb') as f:
    f.write(image_result)
# 是一张无序的图片
print('cut_location_list', cut_location_list)
