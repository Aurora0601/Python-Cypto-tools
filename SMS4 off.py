from gmssl.sm4 import CryptSM4, SM4_DECRYPT
from Crypto.Util.Padding import unpad

def pkcs7_unpad(padded_data):
    """去除PKCS7填充"""
    padding_len = padded_data[-1]
    if padding_len < 1 or padding_len > 16:
        raise ValueError("Invalid padding")
    return padded_data[:-padding_len]

def sms4_decrypt(ciphertext, key):
    sm4_cipher = CryptSM4()
    sm4_cipher.set_key(key, SM4_DECRYPT)
    decrypted_padded_text = sm4_cipher.crypt_ecb(ciphertext)
    return pkcs7_unpad(decrypted_padded_text)

# 用户输入密钥和密文进行解密
key_hex = input("请输入密钥（十六进制）：")
ciphertext_hex = input("请输入要解密的密文（十六进制）：")

# 将十六进制字符串转换为字节
key = bytes.fromhex(key_hex)
ciphertext = bytes.fromhex(ciphertext_hex)

# 解密密文
try:
    decrypted = sms4_decrypt(ciphertext, key)
    print("解密后的明文:", decrypted.decode('utf-8'))
except ValueError as e:
    print("解密失败：", e)