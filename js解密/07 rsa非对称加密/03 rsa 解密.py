from Cryptodome.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

# 1. 加载秘钥
pri_key = open('pri.bin').read()
# 2. 实例化一个秘钥对象
key = RSA.import_key(pri_key)


text = 'CvWBo8IdO2/LcGYVwxOO4XTJ3nZwYcfBxsrNaXmtguJuI3MM1AZqQZqoOk54X3ULkHYyZgz8NxZ2wU4P0i5aLR1uJMsHza0kgYPT6+VaARMI8RqXnllnB0iLW+gHRMeqCHst9vAruLb5lnY8gCEoIb7QyVC53glCmOBx2KPvy8E='
data = base64.b64decode(text.encode())
print(data)


# 3. 获取一个 rsa 对象
rsa = PKCS1_v1_5.new(key)

decode_rsa_data = rsa.decrypt(data, b'rsa')
print(decode_rsa_data)
print(decode_rsa_data.decode())

"""
    rsa 有两个秘钥,一个公钥一个私钥
"""