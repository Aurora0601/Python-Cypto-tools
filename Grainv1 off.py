# decrypt.py
from binascii import unhexlify

def grain_v1_decrypt(key, iv, ciphertext):
    """Grain v1解密"""
    # 这里使用简化的方法生成密钥流，实际应用中需要替换为正确的Grain v1密钥流生成算法
    keystream = bytes([x ^ y for x, y in zip(iv, key)]) * (len(ciphertext) // len(iv) + 1)
    plaintext = bytes([p ^ k for p, k in zip(ciphertext, keystream[:len(ciphertext)])])
    return plaintext

# 用户输入密文、密钥和IV（十六进制字符串）
ciphertext_hex = input("请输入密文（十六进制）：")
key_hex = input("请输入密钥（十六进制）：")
iv_hex = input("请输入IV（十六进制）：")

# 将十六进制字符串转换为字节串
ciphertext = unhexlify(ciphertext_hex)
key = unhexlify(key_hex)
iv = unhexlify(iv_hex)

# 进行Grain v1解密
plaintext = grain_v1_decrypt(key, iv, ciphertext)
print("解密后的明文：", plaintext.decode('utf-8'))