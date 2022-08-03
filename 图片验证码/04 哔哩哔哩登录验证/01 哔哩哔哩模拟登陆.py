import time
import base64
from constants import BILIBILI_USERNAME, BILIBILI_PASSWORD
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.get('https://passport.bilibili.com/login')
driver.implicitly_wait(10)
driver.maximize_window()

"""找到用户名和密码输入框, 输入数据"""
driver.find_element(By.CSS_SELECTOR, '#login-username').send_keys(BILIBILI_USERNAME)
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, '#login-passwd').send_keys(BILIBILI_PASSWORD)
time.sleep(2)

# 点击登陆按钮, 弹出验证码
driver.find_element(By.CSS_SELECTOR, '.btn.btn-login').click()
time.sleep(2)  # 一定要强制等待, 需要时间渲染验证码

"""处理验证码"""
img_label = driver.find_element(By.CSS_SELECTOR, '.geetest_widget.geetest_medium_fontsize')

# 可以直接根据标签对象进行截图操作
time.sleep(2)
img_label.screenshot('yzm.png')
time.sleep(2)
print('正在保存验证码...')


"""识别验证码"""
from img_parsel import base64_api

code_result_list = base64_api('yzm.png')
print('验证码识别结果为:', code_result_list)  # 结果: 90,65|179,164|77,205

result_list = code_result_list.split('|')  # ['90,65', '179,164', '77,205']

for result in result_list:
    x = result.split(',')[0]
    y = result.split(',')[1]

    ActionChains(driver).move_to_element_with_offset(img_label, int(x), int(y)).click().perform()

time.sleep(5)
# 点击确认
driver.find_element(By.CSS_SELECTOR, '.geetest_commit_tip').click()
input()
driver.quit()

