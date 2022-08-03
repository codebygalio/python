from Cryptodome.Cipher import AES
from Cryptodome import Random


# 加密的明文
data = '加密的内容'

# 加密的参数: 16(aes-128) 24(aes-192) 32(aes-256)
key = b'this is a 16 key'
# 随机生成一个秘钥
# iv 混淆的加盐 salt 加料
iv = Random.new().read(AES.block_size)
print('盐', iv)
# 创建一个 aes 对象 (秘钥,模式,加盐)
aes = AES.new(key, AES.MODE_CFB, iv)

# 加密内容
encrypt_data = aes.encrypt(data.encode())
# 把秘钥与数据一起返回
print(encrypt_data)
print(encrypt_data + iv)

