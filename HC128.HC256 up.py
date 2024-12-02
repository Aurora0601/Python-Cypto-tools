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

def encrypt(key, plaintext):
    """
    使用简化的流密码进行加密。
    """
    plaintext_bytes = plaintext.encode('utf-8')
    keystream = generate_keystream(key, len(plaintext_bytes))
    ciphertext = bytes([(p ^ k) for p, k in zip(plaintext_bytes, keystream)])
    return ciphertext.hex()

# 用户输入明文
plaintext = input("请输入明文：")

# 生成随机密钥（16字节）
key = os.urandom(16)

# 进行加密
ciphertext_hex = encrypt(key, plaintext)
print("加密后的密文（十六进制）:", ciphertext_hex)
print("使用的密钥（十六进制）:", key.hex())