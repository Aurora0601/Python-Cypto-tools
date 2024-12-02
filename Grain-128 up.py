# encrypt.py
import os

def generate_keystream(key, iv, length):
    """生成密钥流"""
    state = list(key) + list(iv)
    keystream = [0] * length
    for i in range(length):
        keystream[i] = state[0]
        t = (state[0] + state[1] + state[2] + state[3]) % 256
        state[0] = state[1]
        state[1] = state[2]
        state[2] = state[3]
        state[3] = t
    return bytes(keystream)

def grain128_encrypt(key, iv, plaintext):
    """Grain-128加密"""
    keystream = generate_keystream(key, iv, len(plaintext))
    ciphertext = bytes([p ^ k for p, k in zip(plaintext, keystream)])
    return ciphertext

# 用户输入明文
plaintext = input("请输入明文：").encode('utf-8')

# 生成随机密钥和IV
key = os.urandom(16)  # 128位密钥
iv = os.urandom(16)  # 128位IV

# 进行Grain-128加密
ciphertext = grain128_encrypt(key, iv, plaintext)
print("加密后的密文（十六进制）：", ciphertext.hex())
print("使用的密钥（十六进制）:", key.hex())
print("使用的IV（十六进制）:", iv.hex())