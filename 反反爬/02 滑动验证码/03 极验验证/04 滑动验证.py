import random
import re
import time
from io import BytesIO

import numpy as np
import requests
from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
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

"""还原大图"""
full_image = Image.open('full_image.jpg')

new_im = Image.new('RGB', (260, 116))

# 把无序的图片 切成52张小图片
im_list_upper = []
im_list_down = []
# print(location_list)
for location in full_location_list:
    # print(location['y'])
    if location['y'] == -58:  # 上半边
        # 浏览器显示是负坐标系
        # full_image.crop 剪切图片
        im_list_upper.append(full_image.crop((abs(location['x']), 58, abs(location['x']) + 10, 116)))
    if location['y'] == 0:  # 下半边
        im_list_down.append(full_image.crop((abs(location['x']), 0, abs(location['x']) + 10, 58)))

x_offset = 0
for im in im_list_upper:
    # 把小图片放到 新的空白图片上
    new_im.paste(im, (x_offset, 0))
    x_offset += im.size[0]

x_offset = 0
for im in im_list_down:
    new_im.paste(im, (x_offset, 58))
    x_offset += im.size[0]

new_im.save('full_images2.png')

"""还原小图"""
cut_image = Image.open('cut_image.jpg')
new_im = Image.new('RGB', (260, 116))
im_list_upper = []
im_list_down = []
# print(location_list)
for location in cut_location_list:
    # print(location['y'])
    if location['y'] == -58:  # 上半边
        im_list_upper.append(cut_image.crop((abs(location['x']), 58, abs(location['x']) + 10, 116)))
    if location['y'] == 0:  # 下半边
        im_list_down.append(cut_image.crop((abs(location['x']), 0, abs(location['x']) + 10, 58)))

x_offset = 0
for im in im_list_upper:
    new_im.paste(im, (x_offset, 0))  # 把小图片放到 新的空白图片上
    x_offset += im.size[0]

x_offset = 0
for im in im_list_down:
    new_im.paste(im, (x_offset, 58))
    x_offset += im.size[0]

new_im.save('cut_images2.png')


def get_distance():
    full_image = Image.open('full_images2.png')
    cut_image = Image.open('cut_images2.png')
    # print('size', image1.size)
    # rgb的差值不超过这一个范围 误差范围
    threshold = 50
    for i in range(0, full_image.size[0]):  # 260
        for j in range(0, full_image.size[1]):  # 160
            pixel1 = full_image.getpixel((i, j))
            pixel2 = cut_image.getpixel((i, j))
            # 对比每一个点的三原色
            res_R = abs(pixel1[0] - pixel2[0])  # 计算RGB差
            res_G = abs(pixel1[1] - pixel2[1])  # 计算RGB差
            res_B = abs(pixel1[2] - pixel2[2])  # 计算RGB差
            if res_R > threshold and res_G > threshold and res_B > threshold:
                return i

distance = get_distance() - 4


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

# 贝塞尔曲线的 基础线
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
slider = driver.find_element_by_css_selector('.gt_slider_knob')
ActionChains(driver).click_and_hold(slider).perform()

# 正向滑动
for track_x, track_y in zip(tracks['forward_tracks'], tracks['forward_tracks_y']):
    ActionChains(driver).move_by_offset(xoffset=track_x, yoffset=track_y).perform()
# 反向滑动
for back_tracks in tracks['back_tracks']:
    yoffset_random = random.uniform(-2, 2)
    ActionChains(driver).move_by_offset(xoffset=back_tracks, yoffset=yoffset_random).perform()

ActionChains(driver).release().perform()

