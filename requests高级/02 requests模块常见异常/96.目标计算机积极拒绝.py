import requests

proxy_response = requests.get('http://134.175.188.27:5010/get')
proxy = proxy_response.json()
print(proxy)

"""
requests.exceptions.ConnectionError: 连接报错

目标服务器器没有相关数据了: 如果识别咱们不正常的请求, 可能会针对我们请求的ip进行封锁, 咱们就得不到数据了
客户端的问题: 网络的连通性不好
服务器可能宕机

"""