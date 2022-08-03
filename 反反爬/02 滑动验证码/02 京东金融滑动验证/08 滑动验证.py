import base64
import random
import re
import time
from PIL import Image
import numpy as np
import cv2

from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains

options = ChromeOptions()
# 禁用自动化栏
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(executable_path='../chromedriver.exe', options=options)
driver.maximize_window()
# 账户信息
username = '15140128843'
pwd = '123456'
url = 'https://union.jd.com/login'
# 打开浏览器网页
driver.get(url)
iframe = driver.find_element_by_css_selector('iframe')
print("切换到iframe")
driver.switch_to.frame(iframe)

"""模拟登陆"""
input_ele = driver.find_element_by_id("loginname")
input_ele.clear()

# 模拟认为输入账号密码
time.sleep(random.uniform(0.1, 0.5))
input_ele.send_keys(username[0:3])
time.sleep(random.uniform(0.5, 0.8))
input_ele.send_keys(username[3:])

# 模拟人输入密码
time.sleep(random.uniform(0.8, 1.2))
pwd_ele = driver.find_element_by_id("nloginpwd")
pwd_ele.clear()
pwd_ele.send_keys(pwd)

# 点击登录
print("点击登录")
time.sleep(random.uniform(0.2, 0.8))
login_ele = driver.find_element_by_id("paipaiLoginSubmit")
login_ele.click()

############################################
"""获取图片"""
"""下载图片到本地"""
time.sleep(3)
target = driver.find_element_by_css_selector('.JDJRV-bigimg img')
template = driver.find_element_by_css_selector('.JDJRV-smallimg img')

# 获取图片的 base64 数据
target_base64 = target.get_attribute('src')
template_base64 = template.get_attribute('src')

# 去掉格式内容
target_base64_str = re.sub(r'data:[a-z]*/[a-z]*;base64,', '', target_base64)
template_base64_str = re.sub(r'data:[a-z]*/[a-z]*;base64,', '', template_base64)

# 保存目标图片
target_img_name = 'target.png'
target_binary_content = base64.b64decode(target_base64_str)
with open(target_img_name, mode='wb') as f:
    f.write(target_binary_content)

# 保存模板图片
template_img_name = 'template.png'
template_binary_content = base64.b64decode(template_base64_str)
with open(template_img_name, mode='wb') as f:
    f.write(template_binary_content)

local_img = Image.open(target_img_name)
size_loc = local_img.size
zoom = 281 / int(size_loc[0])
print("计算缩放比例 zoom = %f" % round(zoom, 4))

"""模板匹配（用于寻找缺口）"""
# 等待匹配图片路径
img_target_path = 'target.png'
img_template_path = 'template.png'
# 等待匹配图片
img_target = cv2.imread(img_target_path)
img_template = cv2.imread(img_template_path)

""" 滑块处理 """
# 误差来源就在于滑块的背景图为透明
# 将图片灰度化
gray = cv2.cvtColor(img_template, cv2.COLOR_BGR2GRAY)
cv2.imwrite('temp-gray1.png', gray)
# 灰化背景（将黑色内容变成灰色）
width, heigth = gray.shape
for h in range(heigth):
    for w in range(width):
        if gray[w, h] == 0:
            gray[w, h] = 96

cv2.imwrite('temp-gray2.png', gray)

# 去滑块的前景噪声内核
binary = cv2.inRange(gray, 96, 96)
kernel = np.ones((8, 8), np.uint8)
cv2.imwrite('temp-kernel.png', kernel)
# 开运算去除白色噪点
tpl = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
cv2.imwrite('temp-gray3.png', tpl)

"""模板处理"""
# 图片高斯滤波
blurred = cv2.GaussianBlur(img_target, (3, 3), 0)
cv2.imwrite("target-blurred1.png", blurred)

# 图片灰度化
target_img_gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
cv2.imwrite("target-blurred2.png", target_img_gray)

# 获取图片的宽与高
width, height = tpl.shape[:2]

# 灰度化模板匹配
result = cv2.matchTemplate(target_img_gray, tpl, cv2.TM_CCOEFF_NORMED)  # 使用灰度化图片
print("result = {}".format(len(np.where(result >= 0.5)[0])))

# 查找数组中匹配的最大值
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(min_val, max_val, min_loc, max_loc)

# 返回 左 上 角
left_up = max_loc
# 计算 右 下 角
right_down = (left_up[0] + height, left_up[1] + width)
print(right_down)

# 将匹配到的图片在图像中的绘制出来
cv2.rectangle(img_target, left_up, right_down, (7, 279, 151), 2)
print('匹配结果区域起点x坐标为：%d' % max_loc[0])
cv2.imwrite('dectected.png', img_target)

distance = max_loc[0] * zoom


# #################贝塞尔曲线公式 开始##########
# n表示阶数
# k表示索引
def one_bezier_curve(a, b, t):
    return (1 - t) * a + t * b


def n_bezier_curve(xs, n, k, t):
    if n == 1:
        return one_bezier_curve(xs[k], xs[k + 1], t)
    else:
        return (1 - t) * n_bezier_curve(xs, n - 1, k, t) + t * n_bezier_curve(xs, n - 1, k + 1, t)


def bezier_curve(xs, ys, num):
    """
    :param xs: x 轴位置
    :param ys: y 轴位置
    :param num: 构建的贝塞尔曲线返回的次数
    :return:
    """
    b_xs, b_ys = [], []
    n = 5  # 采用5次bezier曲线拟合
    t_step = 1.0 / (num - 1)
    # t_step = 1.0 / num
    t = np.arange(0.0, 1 + t_step, t_step)
    for each in t:
        b_xs.append(n_bezier_curve(xs, n, 0, each))
        b_ys.append(n_bezier_curve(ys, n, 0, each))
    return b_xs, b_ys


# #################贝塞尔曲线公式 结束##########


def get_random_range(min_, max_):
    """获取指定范围里面的小数"""
    ran = random.random()
    if max_ > ran > min_:
        return ran
    else:
        return get_random_range(min_, max_)


# 时间/移动次数
xs = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
# 0.4-0.7   0.8-0.9
ys = [0, 0, distance * get_random_range(0.4, 0.8), distance, distance, distance]

# # 贝塞尔曲线的 基础线
# plt.figure()
# plt.plot(xs, ys, 'b')  # 原曲线

# 在10-15步之间滑动完毕
num = random.randint(10, 15)
# 调用公式求出贝塞尔曲线的结果
b_xs, b_ys = bezier_curve(xs, ys, num)
# 或者 bezier曲线
# plt.plot(b_xs, b_ys, 'r')
# plt.show()
print('贝塞尔曲线Y点位置：', b_ys)
print('贝塞尔曲线X点位置：', b_xs)
# 每次移动距离
diff_y = list(map(lambda i: b_ys[i + 1] - b_ys[i], range(len(b_ys) - 1)))
print('由Y位置求出每次移动的距离：', diff_y)

# ########## 计算抖动上下抖动 开始 ########
# 求每次移动的平均值
mid = sum(diff_y) / len(diff_y)
# 将每次移动小于平均值的当前次设置符号位负
symbol = list(map(lambda i: 1 if i > mid else -1, diff_y))
# 移动的距离相比点位会少一个，所以在最前面插入 0
symbol.insert(0, 1)
print(symbol)
# 每一次移动的立方根作为抖动，立方根算抖动
diff_three_sqrt = list(map(lambda i: pow(abs(i), get_random_range(0.22, 0.35)), diff_y))
# 为了绘制立方根，需要加一个数字
diff_three_sqrt.insert(0, 0)
# 每次抖动之后的位移
diff_shake_y = list(map(lambda i: diff_three_sqrt[i] * symbol[i], range(len(diff_three_sqrt))))
# 每次抖动的距离
print('每次抖动的距离：', diff_shake_y)
diff_y_shake = list(map(lambda i: sum(diff_shake_y[:i]) + diff_shake_y[i], range(len(diff_shake_y))))
print('抖动的总距离（用于绘图）：', diff_y_shake)
# 黄色抖动线
# plt.plot(b_xs, diff_y_shake, 'y')
# plt.show()
# ########## 计算抖动上下抖动 结束 ########
diff_shake_y = diff_shake_y[1:]

# 清除贝塞尔曲线的小数位，因为selenium只能滑动整数
forward_tracks = []
temp = 0
for i in diff_y:
    # 遍历每一次移动的距离，然后进程 round
    t_i = round(i)
    temp += i - t_i
    forward_tracks.append(t_i)

# 计算清除之后不需要回调绘制补充的距离
back_tracks = [distance - sum(forward_tracks)]
tracks = {'forward_tracks': forward_tracks, 'back_tracks': back_tracks, 'forward_tracks_y': diff_shake_y}
print(tracks)
print('tracks', sum(tracks['forward_tracks']))

"""移动滑块"""
time.sleep(1)
slider = driver.find_element_by_css_selector('.JDJRV-slide-btn')
ActionChains(driver).click_and_hold(slider).perform()

# 正向滑动
for track_x, track_y in zip(tracks['forward_tracks'], tracks['forward_tracks_y']):
    ActionChains(driver).move_by_offset(xoffset=track_x, yoffset=track_y).perform()

# 反向滑动
for back_tracks in tracks['back_tracks']:
    yoffset_random = random.uniform(-2, 2)
    ActionChains(driver).move_by_offset(xoffset=back_tracks, yoffset=yoffset_random).perform()

ActionChains(driver).release().perform()
