from Crypto.Cipher import ChaCha20
from binascii import unhexlify

def chacha20_decrypt(key, nonce, ciphertext_hex):
    """
    使用ChaCha20算法对密文进行解密。
    """
    ciphertext = unhexlify(ciphertext_hex)
    cipher = ChaCha20.new(key=key, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode('utf-8')

# 用户输入密文（十六进制字符串）、密钥（十六进制字符串）和nonce（十六进制字符串）
ciphertext_hex = input("请输入密文（十六进制）：")
key_hex = input("请输入密钥（十六进制）：")
nonce_hex = input("请输入nonce（十六进制）：")

# 将十六进制字符串转换为字节串
key = unhexlify(key_hex)
nonce = unhexlify(nonce_hex)

# 进行ChaCha20解密
plaintext = chacha20_decrypt(key, nonce, ciphertext_hex)
print("解密后的明文:", plaintext)