# https://data.stats.gov.cn/

import requests
requests.packages.urllib3.disable_warnings()  # 忽略警告


# requests默认会验证请求地址的证书, 验证不通过程序就会报错 requests.exceptions.SSLError  ca <数字证书认证机构>
url = 'https://data.stats.gov.cn/'
response = requests.get(url=url, verify=False)  # verify=False 取消证书认证, 默认是True
print(response.text)