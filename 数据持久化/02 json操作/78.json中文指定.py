import json  # 内置

data = {
    'name': '青灯教育',
    'address': '长沙',
    'tel': '12346789'
}

"""默认情况下json文件保存使用的是unicode编码"""
# ensure_ascii=False  在序列化操作的时候, 指定不使用默认编码
json_str = json.dumps(data, ensure_ascii=False)

# encoding='utf-8'  能够显示中文
with open('data.json', mode='w', encoding='utf-8') as f:
    f.write(json_str)

