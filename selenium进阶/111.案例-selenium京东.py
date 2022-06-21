import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def get_product(key):
    """指定关键字搜索商品"""
    # 找到搜索框输入商品关键字
    driver.find_element(By.CSS_SELECTOR, '#key').send_keys(key)
    # 点击搜索按钮
    driver.find_element(By.CSS_SELECTOR, '.button').click()


def drop_down():
    """模拟人去质性页面的下拉操作"""
    for h in range(1, 11, 2):  # 13579  控制下拉的次数, 5次下拉
        time.sleep(0.5)
        j = h / 9  # 分数  1
        js_all = f'document.documentElement.scrollTop = document.documentElement.scrollHeight*{j}'
        driver.execute_script(js_all)

def parse_data():
    """解析商品数据"""
    lis = driver.find_elements(By.CSS_SELECTOR, '.gl-item')

    for li in lis:
        title = li.find_element(By.CSS_SELECTOR, 'div.p-name>a>em').text
        title = title.replace('京东超市', '').replace('京品电脑', '').replace('\n', '')
        price = li.find_element(By.CSS_SELECTOR, 'div.p-price>strong>i').text
        deal = li.find_element(By.CSS_SELECTOR, 'div.p-commit>strong').text
        store_name = li.find_element(By.CSS_SELECTOR, '.J_im_icon>a').text
        print(title, price, deal, store_name, sep=' | ')

        with open('京东数据.csv', mode='a', encoding='utf-8', newline="") as f:
            csv_write = csv.writer(f)
            csv_write.writerow([title, price, deal, store_name])


def get_next():
    """找下一页标签进行点击操作"""
    driver.find_element(By.CSS_SELECTOR, '.pn-next>em').click()

if __name__ == '__main__':
    word = input('请输入您要搜索商品的关键字:')

    chrome_options = Options()  # 实例化一个配置对象
    chrome_options.add_argument('--headless')  # --headless  添加无头模式配置

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.jd.com/')
    driver.implicitly_wait(10)
    driver.maximize_window()

    # 调用搜索商品的函数功能
    get_product(word)

    for i in range(100):
        # 调用页面下拉操作的函数
        drop_down()
        # 调用解析商品数据的方法
        parse_data()
        # 执行下一页点击函数
        get_next()

    input()
    driver.quit()
