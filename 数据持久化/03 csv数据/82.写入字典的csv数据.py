import csv

list_dict = [
    {'name': '张三', 'age': 18, 'sex': '男'},
    {'name': '李四', 'age': 22, 'sex': '女'},
    {'name': '王五', 'age': 24, 'sex': '男'}
]

with open('data2.csv', mode='a', encoding='utf-8', newline='') as f:

    """
    DictWriter 创建一个写入字典数据的csv对象, 括号中第一个参数传文件对象, 第二个参数传字典的键
    
    """
    field = ['name', 'age', 'sex']  # 字典的键用列表收集
    csv_write = csv.DictWriter(f, fieldnames=field)

    # 根据提供的字典的键, 写入表头, 只有字典写入对象才有这个方法
    # csv_write.writeheader()

    for i in list_dict:
        csv_write.writerow(i)