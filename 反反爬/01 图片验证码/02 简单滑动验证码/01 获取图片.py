import base64
import os
import random
import time
import re

from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait

# 账户信息
username = '15111111111'
pwd = '123456'

# 打开窗口
url = 'https://union.jd.com/login'
options = ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

driver.get(url)
time.sleep(1)
# 找到“嵌套”的iframe
iframe = driver.find_element_by_xpath('//iframe')
print("切换到iframe")
driver.switch_to.frame(iframe)
"""填写账号"""
print("填写账号开始")
input_ele = driver.find_element_by_id("loginname")
input_ele.clear()
# username
# 模拟认为输入账号密码
time.sleep(random.uniform(0.1, 0.5))
input_ele.send_keys(username[0:3])
time.sleep(random.uniform(0.5, 0.8))
input_ele.send_keys(username[3:])
# pwd
if pwd:
    time.sleep(random.uniform(0.8, 1.2))
    pwd_ele = driver.find_element_by_id("nloginpwd")
    pwd_ele.clear()
    pwd_ele.send_keys(pwd)
print("点击登录")
time.sleep(random.uniform(0.2, 0.8))
login_ele = driver.find_element_by_id("paipaiLoginSubmit")
login_ele.click()

""""""


def base64_to_image(base64_code, img_name):
    """
    base64转image
    :param base64_code:
    :param img_name: 图片所在的path
    :return:
    """
    dir_path = re.sub(r'/([a-z]|_|-)*.(png|jp(e)?g)$', '', img_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    img_data = base64.b64decode(base64_code)
    file = open(img_name, 'wb')
    file.write(img_data)
    file.close()
    return img_name


"""获取滑动验证图片"""
time.sleep(3)
target_path = 'target.png'
template_path = 'template.png'
target = driver.find_element_by_xpath("//div[@class='JDJRV-bigimg']/img")
template = driver.find_element_by_xpath("//div[@class='JDJRV-smallimg']/img")
if target and template:
    print("开始下载图片")
    target_base64 = target.get_attribute('src')
    template_base64 = template.get_attribute('src')
    target_base64_str = re.sub(r'data:[a-z]*/[a-z]*;base64,', '', target_base64)
    template_base64_str = re.sub(r'data:[a-z]*/[a-z]*;base64,', '', template_base64)
    # save
    base64_to_image(target_base64_str, target_path)
    base64_to_image(template_base64_str, template_path)

    time.sleep(1)

    # zoom
    local_img = Image.open(target_path)
    size_loc = local_img.size
    zoom = 281 / int(size_loc[0])
    print("计算缩放比例 zoom = %f" % round(zoom, 4))
