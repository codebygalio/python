import json  # 内置

data = {
    'name': '青灯教育',
    'address': '长沙',
    'tel': '12346789'
}

json_str = json.dumps(data)

with open('data.json', mode='w', encoding='utf-8') as f:
    f.write(json_str)

