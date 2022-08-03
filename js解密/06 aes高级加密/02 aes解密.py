from Cryptodome.Cipher import AES

key = b'this is a 16 key'
data = b"U\xb9j\xee\xab\xc7^\xafH8YZ\x95\xe8A\xb9gc\xa4*\x95X'\xb3\xcb]\xe5\xc6i\xb1H?\xeeX-"

# iv
aes = AES.new(key, AES.MODE_CFB, data[-16:])

data = aes.decrypt(data[:-16])
print(data)
print(data.decode())


"""
    解密的时候不需要管具体加密的秘钥与盐
    能找到盐与秘钥,只要能解密就行
"""