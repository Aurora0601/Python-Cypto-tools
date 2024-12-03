import os

def generate_keystream(key, length):
    """
    生成密钥流。
    """
    keystream = []
    state = int.from_bytes(key, 'big')
    for _ in range(length):
        bit = (state >> 31) & 1
        state = ((state << 1) & 0xFFFFFFFF) | bit
        state ^= (bit & 0x7E) << 24 if bit else 0
        keystream.append(state & 0xFF)
    return bytes(keystream)

def decrypt(key, ciphertext_hex):
    """
    使用简化的流密码进行解密。
    """
    ciphertext = bytes.fromhex(ciphertext_hex)
    keystream = generate_keystream(key, len(ciphertext))
    plaintext_bytes = bytes([(p ^ k) for p, k in zip(ciphertext, keystream)])
    return plaintext_bytes.decode('utf-8', errors='ignore')

# 用户输入密文（十六进制字符串）和密钥（十六进制字符串）
ciphertext_hex = input("请输入密文（十六进制）：")
key_hex = input("请输入密钥（十六进制）：")
key = bytes.fromhex(key_hex)

# 进行解密
plaintext = decrypt(key, ciphertext_hex)
print("解密后的明文:", plaintext)
