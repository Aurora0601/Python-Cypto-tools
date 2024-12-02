from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# AES加密函数
def aes_encrypt(plaintext, key):
    # 生成随机初始化向量IV
    iv = get_random_bytes(AES.block_size)
    # 创建一个新的AES cipher
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 对明文进行填充
    padded_text = pad(plaintext, AES.block_size)
    # 加密
    encrypted = cipher.encrypt(padded_text)
    # 返回初始化向量和密文
    return iv, encrypted

# 用户输入明文
plaintext = input("请输入明文：").encode('utf-8')

# 生成随机密钥（这里使用AES-256，所以密钥长度为32字节）
key = get_random_bytes(32)

# 加密明文
iv, encrypted = aes_encrypt(plaintext, key)

# 显示加密后的密文和初始化向量
print("初始化向量（十六进制）:", iv.hex())
print("加密后的密文（十六进制）:", encrypted.hex())

# 保存密钥，以便解密时使用
print("请保存以下密钥，以便将来解密：")
print("密钥（十六进制）:", key.hex())
