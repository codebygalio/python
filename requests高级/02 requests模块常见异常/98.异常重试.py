import requests


try:
    proxy_response = requests.get('http://134.175.188.27:5010/get', timeout=0.0001)
    proxy = proxy_response.json()
    print(proxy)

except Exception as e:
    print('========= 这是第 2 次执行 ==========')
    proxy_response = requests.get('http://134.175.188.27:5010/get', timeout=0.0001)
    proxy = proxy_response.json()
    print(proxy)
