from Cryptodome.PublicKey import RSA

# 生成秘钥 1024
rsa = RSA.generate(1024)

print(rsa.export_key())
print(rsa.publickey().export_key())

with open('pri.bin', mode='wb') as f:
    f.write(rsa.export_key())
with open('pub.pem', mode='wb') as f:
    f.write(rsa.publickey().export_key())
