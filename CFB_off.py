from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from binascii import unhexlify

def cfb_decrypt(key, iv, ciphertext_hex):
    """
    使用AES-CFB算法对密文进行解密。
    """
    # 将十六进制的密文转换为字节
    ciphertext = unhexlify(ciphertext_hex)
    # 创建AES解密对象，使用CFB模式
    cipher = AES.new(key, AES.MODE_CFB, iv)
    # 解密密文，然后去除填充，得到原始明文
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext, AES.block_size).decode('utf-8')
    return plaintext

# 用户输入密钥、IV和密文
key_hex = input("请输入密钥（十六进制）：")
iv_hex = input("请输入IV（十六进制）：")
ciphertext_hex = input("请输入密文（十六进制）：")

# 将十六进制密钥和IV转换为字节
key = unhexlify(key_hex)
iv = unhexlify(iv_hex)

# 进行CFB解密
plaintext = cfb_decrypt(key, iv, ciphertext_hex)

print("解密后的明文:", plaintext)
