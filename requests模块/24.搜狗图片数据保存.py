"""
	- 将前三页的图片数据保存到文件夹里面
	    有错误需要解决报错<可以根据情况使用（异常捕获 + 请求参数）>
		

"""

import requests
requests.packages.urllib3.disable_warnings()

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

num = 1
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
        # print(img_url)
        try:
            img_data = requests.get(url=img_url, verify=False, timeout=3).content  # 请求的图片数据
            file_name = str(num) + '.jpg'  # 图片名字

            with open('img\\' + file_name, mode='wb') as f:
                print('保存完成:', file_name)
                f.write(img_data)
            num += 1
        except Exception as e:
            print(e)
