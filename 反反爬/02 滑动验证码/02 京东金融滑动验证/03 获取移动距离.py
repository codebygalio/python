import numpy as np
import cv2

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

