# decrypt.py
from binascii import unhexlify

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

def grain128_decrypt(key, iv, ciphertext):
    """Grain-128解密"""
    keystream = generate_keystream(key, iv, len(ciphertext))
    plaintext = bytes([p ^ k for p, k in zip(ciphertext, keystream)])
    return plaintext

# 用户输入密文、密钥和IV（十六进制字符串）
ciphertext_hex = input("请输入密文（十六进制）：")
key_hex = input("请输入密钥（十六进制）：")
iv_hex = input("请输入IV（十六进制）：")

# 将十六进制字符串转换为字节串
ciphertext = bytes.fromhex(ciphertext_hex)
key = bytes.fromhex(key_hex)
iv = bytes.fromhex(iv_hex)

# 进行Grain-128解密
plaintext = grain128_decrypt(key, iv, ciphertext)
print("解密后的明文：", plaintext.decode('utf-8'))