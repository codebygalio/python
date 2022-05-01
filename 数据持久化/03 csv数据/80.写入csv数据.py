"""
csv数据, 所有数据用逗号分隔
张三,男,180
李四,女,160
王五,男,168
"""

ll = [
    [1,2,3,4,5],
    [6,7,8,9,3],
    [5,4,3,2,1],
]

import csv  # 内置模块

with open('data.csv', mode='a', encoding='utf-8', newline='') as f:

    """
    newline=''      指定新行, 可以解决默认的数据空行
    csv.writer() 创建一个csv数据写入的对象, 括号内部传递文件对象
    writerow() 整行写入数据, 括号内部中需要传一个数据容器(列表, 元组)
    """
    csv_write = csv.writer(f)
    for i in ll:

        csv_write.writerow(i)
