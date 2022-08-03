zoom = 0.780600
distance = 138 * zoom
print(distance)

"""
根据偏移量获取移动轨迹
匀速轨迹
"""
# 移动的轨迹
track = []
# 设置初始位置
current = 0
# 初始速度
v = 10
# 时间间隔/移动次数
t = 1

while current < distance:
    # s = v0 *t + 0.5 * a * t * t
    s = v * t
    current += s
    track.append(s)

tracks = {'forward_tracks': track}
print(tracks)
