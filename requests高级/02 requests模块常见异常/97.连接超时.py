import requests

proxy_response = requests.get('http://134.175.188.27:5010/get', timeout=0.0001)
proxy = proxy_response.json()
print(proxy)

