import requests

url = 'https://pic.sogou.com/napi/pc/searchList'

def get_params(page):
    params = {
        'mode': '1',
        'mood': '7',
        'dm': '0',
        'start': str(page),
        'xml_len': '48',
        'query': '风景',
    }
    return params

for i in range(48, 145, 48):
    params = get_params(i)
    # print(params)
    response = requests.get(url=url, params=params)
    json_data = response.json()
    # print(json_data)

    # 数据解析
    data_list = json_data['data']['items']
    print('\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    for data in data_list:
        img_url = data['picUrl']
        print(img_url)