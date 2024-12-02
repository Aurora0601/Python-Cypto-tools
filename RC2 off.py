from Crypto.Cipher import ARC2
from Crypto.Util.Padding import unpad
from binascii import unhexlify

def rc2_decrypt(key, ciphertext_hex):
    """
    使用RC2算法对密文进行解密。
    """
    # 将十六进制的密文转换为字节
    ciphertext = unhexlify(ciphertext_hex)
    # 创建RC2解密对象，使用ECB模式
    cipher = ARC2.new(key, ARC2.MODE_ECB)
    # 解密密文，然后去除填充，得到原始明文
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext, ARC2.block_size).decode('utf-8')
    return plaintext

# 用户输入密钥和密文
key_input = input("请输入密钥（十六进制）：")
ciphertext_hex = input("请输入密文（十六进制）：")

# 将十六进制密钥转换为字节
key = unhexlify(key_input)

# 进行RC2解密
plaintext = rc2_decrypt(key, ciphertext_hex)

print("解密后的明文:", plaintext)