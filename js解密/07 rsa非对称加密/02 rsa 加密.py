from Cryptodome.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

text = '加密的内容'

# 加载秘钥, 使用公钥进行加密
pub_key = open('pub.pem').read()

key = RSA.import_key(pub_key)
# 生成加密对象
cipher = PKCS1_v1_5.new(key)

encode_rsa_data = cipher.encrypt(text.encode())
print(encode_rsa_data)
b64_data = base64.b64encode(encode_rsa_data)
print(b64_data)
print(b64_data.decode())
