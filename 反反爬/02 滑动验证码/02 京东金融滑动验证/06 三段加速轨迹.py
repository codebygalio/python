import random

distance = 138
zoom = 0.780600
distance = distance * zoom

"""
根据偏移量获取移动轨迹
三段加速轨迹
"""
track = []
# 0.1-0.2 之间取一个随机数作为第一段加速分割点
# 0.65-0.76 之间取一个随机数作为第二段加速分割点
# 0.84-0.88 之间取一个随机数作为第三段加速分割点
mid1 = round(distance * random.uniform(0.1, 0.2))
mid2 = round(distance * random.uniform(0.65, 0.76))
mid3 = round(distance * random.uniform(0.84, 0.88))
# 设置初始位置、初始速度、时间间隔
current, v, t = 0, 0, 0.2
distance = round(distance)

while current < distance:
    # 四段加速度
    if current < mid1:
        a = random.randint(10, 15)
    elif current < mid2:
        a = random.randint(30, 40)
    elif current < mid3:
        a = -70
    else:
        a = random.randint(-25, -18)

    # 初速度 v0
    v0 = v
    # 当前速度 v = v0 + at
    v = v0 + a * t
    v = v if v >= 0 else 0
    move = v0 * t + 1 / 2 * a * (t ** 2)
    move = round(move if move >= 0 else 1)
    # 当前次位移距离
    current += move
    # 加入轨迹
    track.append(move)

print("current={}, distance={}".format(current, distance))
print(track)
# 超出范围
back_tracks = []
out_range = distance - current
if out_range < -8:
    sub = int(out_range + 8)
    back_tracks = [-1, sub, -3, -1, -1, -1, -1]
elif out_range < -2:
    sub = int(out_range + 3)
    back_tracks = [-1, -1, sub]

move_dict = {'forward_tracks': track, 'back_tracks': back_tracks}
print(move_dict)
