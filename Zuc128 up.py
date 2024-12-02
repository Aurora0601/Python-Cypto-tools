# encrypt.py
import os

def zuc128_encrypt(key, iv, plaintext):
    """ZUC-128加密"""
    # 初始化密钥流列表
    keystream = [0] * len(plaintext)
    # ZUC-128的内部状态
    state = list(key) + list(iv) + [0, 0, 0, 0]  # 扩展状态以匹配ZUC-128的要求

    for i in range(len(plaintext)):
        # F函数和反馈
        f = ((state[0] + state[1]) & 0xff) ^ state[3] ^ (state[2] & 0x80)
        keystream[i] = f
        state[3] = state[2]
        state[2] = state[1]
        state[1] = (state[0] + f) & 0xff
        state[0] = f

    # 将密钥流与明文进行XOR操作得到密文
    ciphertext = bytes([plaintext[i] ^ keystream[i] for i in range(len(plaintext))])
    return ciphertext

# 用户输入明文
plaintext = input("请输入明文：").encode('utf-8')

# 生成随机密钥和IV
key = os.urandom(16)  # 128位密钥
iv = os.urandom(16)  # 128位IV

# 进行ZUC-128加密
ciphertext = zuc128_encrypt(key, iv, plaintext)
print("加密后的密文（十六进制）：", ciphertext.hex())
print("使用的密钥（十六进制）:", key.hex())
print("使用的IV（十六进制）:", iv.hex())