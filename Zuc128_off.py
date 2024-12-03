# decrypt.py
from binascii import unhexlify

def zuc128_decrypt(key, iv, ciphertext):
    """ZUC-128解密"""
    # 初始化密钥流列表
    keystream = [0] * len(ciphertext)
    # ZUC-128的内部状态
    state = list(key) + list(iv) + [0, 0, 0, 0]  # 扩展状态以匹配ZUC-128的要求

    for i in range(len(ciphertext)):
        # F函数和反馈
        f = ((state[0] + state[1]) & 0xff) ^ state[3] ^ (state[2] & 0x80)
        keystream[i] = f
        state[3] = state[2]
        state[2] = state[1]
        state[1] = (state[0] + f) & 0xff
        state[0] = f

    # 将密钥流与密文进行XOR操作得到明文
    plaintext = bytes([ciphertext[i] ^ keystream[i] for i in range(len(ciphertext))])
    return plaintext

# 用户输入密文、密钥和IV（十六进制字符串）
ciphertext_hex = input("请输入密文（十六进制）：")
key_hex = input("请输入密钥（十六进制）：")
iv_hex = input("请输入IV（十六进制）：")

# 将十六进制字符串转换为字节串
ciphertext = bytes.fromhex(ciphertext_hex)
key = bytes.fromhex(key_hex)
iv = bytes.fromhex(iv_hex)

# 进行ZUC-128解密
plaintext = zuc128_decrypt(key, iv, ciphertext)
print("解密后的明文：", plaintext.decode('utf-8'))
