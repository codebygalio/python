import json  # 内置

data = {
    'name': '青灯教育',
    'address': '长沙',
    'tel': '12346789'
}

data2 = [
    '青灯教育',
    '长沙',
    '12346789'
]

"""
json序列化操作: 把一个对象转换成了json字符串
"""
json_str = json.dumps(data)
print(json_str)
print(type(json_str))


"""
json反序列化操作: 把json字符串转换成对象
loads()  括内部传字符串
"""
json_obj = json.loads(json_str)
print(json_obj)
print(type(json_obj))

"""
字典和列表对象是可以直接进行序列化和反序列化操作
"""
