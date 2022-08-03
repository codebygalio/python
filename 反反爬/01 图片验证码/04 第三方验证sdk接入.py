from chaojiying import Chaojiying_Client
import requests

response = requests.get('http://www.chaojiying.com/include/code/code.php?u=1')

with open('code1.png', mode='wb') as f:
    f.write(response.content)

client = Chaojiying_Client('hjx3136419', '123456', '907219')

r = client.PostPic(response.content, 1902)
print(r)
