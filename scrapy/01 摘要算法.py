import hashlib
import json


d1 = {"name": "张三", "age": 18, "hobby": "吃"}
d2 = {"name": "李四", "age": 18, "hobby": "喝"}
d3 = {"name": "王五", "age": 18, "hobby": "玩"}
items = [d1, d2, d3]
print(items)


d4 = {"name": "赵柳", "age": 18, "hobby": "乐"}

if d4 not in items:
    items.append(d4)
    print('d4不存在于items')

# 创建一个摘要算法对象
md5 = hashlib.md5()
md5.update(json.dumps(d4).encode())  # 摘要算法, update() 需要传递字符串的二进制形式
print(md5.hexdigest())


# 同样的字符串进行摘要得到的结果是一样的
md5 = hashlib.md5()
md5.update(json.dumps(d4).encode())  # 摘要算法, update() 需要传递字符串的二进制形式
print(md5.hexdigest())


result1 = hashlib.md5(json.dumps(d1).encode()).hexdigest()
result2 = hashlib.md5(json.dumps(d2).encode()).hexdigest()
result3 = hashlib.md5(json.dumps(d3).encode()).hexdigest()

items_2 = [result1, result2, result3]
print(items_2)

