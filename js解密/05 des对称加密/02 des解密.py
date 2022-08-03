

# des 对象才能实现加密解密
from Cryptodome.Cipher import DES
key = b'zxcvbnma'
des = DES.new(key, DES.MODE_ECB)

text = b',\xdb\x8a\x9c\xf2yR\xf5~H\x9aF\xb7\x83U\xba'

# 传入文字进行解密
decode_text = des.decrypt(text)
print(decode_text)
print(decode_text.decode())
print(decode_text.decode().strip())

"""
    加密的秘钥, 加密的模式
    
    utf-8 
"""
