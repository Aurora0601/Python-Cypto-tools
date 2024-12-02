from Crypto.Cipher import Salsa20
from Crypto.Random import get_random_bytes
from binascii import hexlify

def salsa20_encrypt(key, nonce, plaintext):
    """
    使用Salsa20算法对明文进行加密。
    """
    cipher = Salsa20.new(key=key, nonce=nonce)
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    return hexlify(ciphertext).decode('utf-8')

# 用户输入明文
plaintext = input("请输入明文：")

# 生成随机密钥和nonce（都是32字节）
key = get_random_bytes(32)  # Salsa20的密钥长度为256位
nonce = get_random_bytes(8)  # Salsa20的nonce长度为64位

# 进行Salsa20加密
ciphertext_hex = salsa20_encrypt(key, nonce, plaintext)
print("加密后的密文（十六进制）:", ciphertext_hex)
print("使用的密钥（十六进制）:", hexlify(key).decode())
print("使用的nonce（十六进制）:", hexlify(nonce).decode())