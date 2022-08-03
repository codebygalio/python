from Cryptodome.Cipher import DES


def pad(text):
    """
        将 text 八位数的整数倍
    :param text:
    :return:
    """
    # 如果 text 的长度不是八的整数倍, 就多加一位
    while len(text) % 8 != 0:
        text += ' '
    return text


# key 加密的秘钥 秘钥是由限制的,限制八位长度
key = b'zxcvbnma'

# 得到一个加密对象
des = DES.new(key, DES.MODE_ECB)

# 对数据进行加密, 数据长度必须是八位数的加密秘钥整数倍
#

hello = 'hello world !'
hello = pad(hello)

encrypt_text = des.encrypt(hello.encode('utf-8'))
print(encrypt_text)
