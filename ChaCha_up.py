from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
from binascii import hexlify

def chacha20_encrypt(key, nonce, plaintext):
    """
    使用ChaCha20算法对明文进行加密。
    """
    cipher = ChaCha20.new(key=key, nonce=nonce)
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    return hexlify(ciphertext).decode('utf-8')

# 用户输入明文
plaintext = input("请输入明文：")

# 生成随机密钥和nonce（都是32字节）
key = get_random_bytes(32)  # ChaCha20的密钥长度可以是128位或256位，这里使用256位
nonce = get_random_bytes(12)  # nonce长度为12字节

# 进行ChaCha20加密
ciphertext_hex = chacha20_encrypt(key, nonce, plaintext)
print("加密后的密文（十六进制）:", ciphertext_hex)
print("使用的密钥（十六进制）:", hexlify(key).decode())
print("使用的nonce（十六进制）:", hexlify(nonce).decode())
