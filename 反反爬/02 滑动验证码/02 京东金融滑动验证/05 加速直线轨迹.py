zoom = 0.780600
distance = 138 * zoom
print(distance)

"""
根据偏移量和手动操作模拟计算移动轨迹
"""
# 移动轨迹
trace = []
# 减速阈值
mid = distance * 3 / 5
# 设置初始位置
current = 0
# 初始速度
v = 0
# 时间间隔
t = 1
# 多走一段
distance += 13

while current < distance:
    if current < mid:
        a = 2
    else:
        a = -4
    s = v * t + 0.5 * a * (t ** 2)
    v = v + a * t
    current += s
    trace.append(round(s))
# 固定回撤
back_tracks = [-3, -3, -2, -2, -1, -1, -1]
print({'forward_tracks': trace, 'back_tracks': back_tracks})
