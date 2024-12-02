# encrypt.py
from Crypto.Random import get_random_bytes

def grain_v1_encrypt(key, iv, plaintext):
    """Grain v1加密"""
    # 这里使用简化的方法生成密钥流，实际应用中需要替换为正确的Grain v1密钥流生成算法
    keystream = bytes([x ^ y for x, y in zip(iv, key)]) * (len(plaintext) // len(iv) + 1)
    ciphertext = bytes([p ^ k for p, k in zip(plaintext, keystream[:len(plaintext)])])
    return ciphertext

# 用户输入明文
plaintext = input("请输入明文：").encode('utf-8')

# 生成随机密钥和IV
key = get_random_bytes(16)  # 128位密钥
iv = get_random_bytes(12)  # 96位IV

# 进行Grain v1加密
ciphertext = grain_v1_encrypt(key, iv, plaintext)
print("加密后的密文：", ciphertext.hex())
print("使用的密钥（十六进制）:", key.hex())
print("使用的IV（十六进制）:", iv.hex())