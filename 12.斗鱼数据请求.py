import requests
import pprint


url = 'https://www.douyu.com/gapi/rkc/directory/mixList/2_1/2'
response = requests.get(url)
# json_data = response.text
json_data = response.json()  # 通过 json() 提取数据以后, 会在底层经过数据转换, 转换成python对象<字典和列表>
# print(json_data)
# print(type(json_data))

# pprint.pprint(json_data)

data_list = json_data['data']['rl']
# print(data_list)

for data in data_list:
    room_name = data['rn']
    nickname = data['nn']
    kind = data['c2name']
    hot = data['ol']
    print(room_name, nickname, kind, hot)

