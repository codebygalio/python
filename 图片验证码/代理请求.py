import requests

def get_proxy():
    url = 'http://tiqu.pyhttp.taolop.com/getip?count=1&neek=13873&type=2&yys=0&port=1&sb=&mr=2&sep=0&ts=1'
    json_data = requests.get(url=url).json()
    print(json_data)


    proxies = {
        "http": "http://" + json_data['data'][0]['ip'] + ':' +str(json_data['data'][0]['port']),
        "https": "http://" + json_data['data'][0]['ip'] + ':' + str(json_data['data'][0]['port']),
    }
    print(proxies)

    return proxies


# print(get_proxy())
if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    response = requests.get(url=url, proxies=get_proxy(), timeout=5)
    print(response.text)


