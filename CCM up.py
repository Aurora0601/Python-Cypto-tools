from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from binascii import hexlify

def aes_ccm_encrypt(key, nonce, plaintext, aad):
    """
    使用AES-CCM算法对明文进行加密。
    """
    # 创建AES加密对象，使用CCM模式
    cipher = AES.new(key, AES.MODE_CCM, nonce=nonce)
    # 设置关联数据
    cipher.update(aad.encode('utf-8'))
    # 加密明文
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))
    # 返回密文和标签的十六进制字符串
    return hexlify(ciphertext).decode('utf-8'), hexlify(tag).decode('utf-8')

# 用户输入明文和关联数据
plaintext = input("请输入明文：")
aad = input("请输入关联数据（AAD）：")

# 生成随机密钥和nonce（都是16字节）
key = get_random_bytes(16)  # AES-128
nonce = get_random_bytes(12)  # 常用的nonce长度

# 进行CCM加密
ciphertext_hex, tag_hex = aes_ccm_encrypt(key, nonce, plaintext, aad)

print("加密后的密文（十六进制）:", ciphertext_hex)
print("使用的标签（十六进制）:", tag_hex)
print("使用的密钥（十六进制）:", hexlify(key).decode())
print("使用的nonce（十六进制）:", hexlify(nonce).decode())