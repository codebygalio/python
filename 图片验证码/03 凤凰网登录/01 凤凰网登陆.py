import time
import base64
from constants import FENG_USERNAME, FENG_PASSWORD
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.ifeng.com/')
driver.implicitly_wait(10)
driver.maximize_window()

"""找到右上角登陆按钮点击"""
driver.find_element(By.CSS_SELECTOR, '.login_in_2x-3NxtSKIw').click()
time.sleep(3)

"""进入到嵌套网页"""
iframe_label = driver.find_element(By.CSS_SELECTOR, '.box-1pZSPyeN div iframe')
driver.switch_to.frame(iframe_label)

"""点击账号登陆"""
driver.find_element(By.CSS_SELECTOR, '.loginById-3RQW_VIV ').click()

"""找到用户名和密码框输入数据"""
username_input = driver.find_element(By.CSS_SELECTOR, '.loginById-3HzkdnTl>div>div>input')
username_input.send_keys(FENG_USERNAME)
time.sleep(1)

pwd_input = driver.find_element(By.CSS_SELECTOR, '.password-3DqV-_Zl.clearfix>div>div>input')
pwd_input.send_keys(FENG_PASSWORD)
time.sleep(1)

"""处理验证码<保存, 识别>"""
img_label = driver.find_element(By.CSS_SELECTOR, '.codeImg-2pONyHUT>img')
img_str = img_label.get_attribute('src')
print('取到的src属性:', img_str)
base64_str = img_str.split(',')[-1]
print('字符串形式的图片:', base64_str)

# 把字符串形式的图片转成二进制, 保存下来
img_data = base64.b64decode(base64_str)
with open('yzm.png', mode='wb') as f:
    f.write(img_data)

"""自动识别验证码"""
from img_parsel import base64_api

result = base64_api('yzm.png')
print('验证码的识别结果为:', result)
time.sleep(1)

"""输入验证码"""
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.vCode-1FqhwIJ9.clearfix>div>div>input').send_keys(result)

"""点击登陆"""
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.submmitBtn-2AmMFR0C').click()

input()
driver.quit()

