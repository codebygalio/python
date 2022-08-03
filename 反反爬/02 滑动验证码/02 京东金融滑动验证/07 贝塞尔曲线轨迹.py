import random

import numpy as np
import matplotlib.pyplot as plt

distance = 134


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
plt.figure()
plt.plot(xs, ys, 'b')  # 原曲线

# 在10-15步之间滑动完毕
num = random.randint(10, 15)
# 调用公式求出贝塞尔曲线的结果
b_xs, b_ys = bezier_curve(xs, ys, num)
# 或者 bezier曲线
plt.plot(b_xs, b_ys, 'r')
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
plt.plot(b_xs, diff_y_shake, 'y')
plt.show()
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
