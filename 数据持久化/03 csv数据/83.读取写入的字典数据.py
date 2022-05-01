import csv  # 内置模块

# with open('data2.csv', mode='r', encoding='utf-8', newline='') as f:
#     """
#     csv.DictReader(f)  创建一个字典读取对象
#     """
#     csv_read = csv.DictReader(f)
#     print(csv_read)
#
#     for i in csv_read:
#         print(i)

with open('data2.csv', mode='r', encoding='utf-8', newline='') as f:
    print(f.read())