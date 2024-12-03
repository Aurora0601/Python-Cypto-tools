from gmssl.sm4 import CryptSM4, SM4_ENCRYPT
from Crypto.Random import get_random_bytes

def pkcs7_pad(data):
    """PKCS7填充"""
    padding = 16 - len(data) % 16
    return data + bytes([padding]) * padding

def sms4_encrypt(plaintext, key):
    sm4_cipher = CryptSM4()
    sm4_cipher.set_key(key, SM4_ENCRYPT)
    padded_text = pkcs7_pad(plaintext)
    encrypted = sm4_cipher.crypt_ecb(padded_text)
    return encrypted

# 用户输入明文
plaintext = input("请输入明文：").encode('utf-8')

# 生成随机密钥（SMS4需要16字节的密钥）
key = get_random_bytes(16)

# 保存密钥（在实际应用中，密钥应该安全存储，而不是直接打印出来）
print("请保存以下密钥，以便将来解密：")
print("密钥（十六进制）:", key.hex())

# 加密明文
encrypted = sms4_encrypt(plaintext, key)

# 显示加密后的密文
print("加密后的密文（十六进制）:", encrypted.hex())
