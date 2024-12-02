from Crypto.Cipher import Salsa20
from binascii import unhexlify

def salsa20_decrypt(key, nonce, ciphertext_hex):
    """
    使用Salsa20算法对密文进行解密。
    """
    ciphertext = unhexlify(ciphertext_hex)
    cipher = Salsa20.new(key=key, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode('utf-8')

# 用户输入密文（十六进制字符串）、密钥（十六进制字符串）和nonce（十六进制字符串）
ciphertext_hex = input("请输入密文（十六进制）：")
key_hex = input("请输入密钥（十六进制）：")
nonce_hex = input("请输入nonce（十六进制）：")

# 将十六进制字符串转换为字节串
key = unhexlify(key_hex)
nonce = unhexlify(nonce_hex)

# 进行Salsa20解密
plaintext = salsa20_decrypt(key, nonce, ciphertext_hex)
print("解密后的明文:", plaintext)