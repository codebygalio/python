

ll = [
    [1,2,3,4,5],
    [6,7,8,9,3],
    [5,4,3,2,1],
]
# pandas
import csv  # 内置模块

with open('data.csv', mode='r', encoding='utf-8', newline='') as f:

    """
    csv.reader(f)   创建一个csv数据读取的对象, 括号内部传递文件对象
    """
    csv_read = csv.reader(f)
    for row in csv_read:
        print(row)


