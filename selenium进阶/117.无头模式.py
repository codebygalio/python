from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 导入浏览器的选项功能

chrome_options = Options()  # 实例化一个配置对象
chrome_options.add_argument('--headless')  # --headless  添加无头模式配置


driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.baidu.com')
print(driver.page_source)

input()
driver.quit()

"""
无头模式的配置, 一本用于项目逻辑代码写完后添加, 因为我们需要在编辑代码的时候看浏览器的页面效果

优点:
    不会打开浏览器, 没有渲染步骤, 所以执行的速度相对块
"""
