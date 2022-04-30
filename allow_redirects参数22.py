import requests

url = 'http://github.com/'
response = requests.get(url=url, allow_redirects=False)  # allow_redirects=False 阻止重定向
print(response.status_code)
