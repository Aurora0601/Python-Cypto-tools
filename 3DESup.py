from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes


# 3DES加密函数
def des3_encrypt(plaintext, key, iv):
    """
    使用3DES算法加密明文。

    参数:
    plaintext -- 要加密的明文，必须是字节类型。
    key       -- 3DES加密使用的密钥，长度为24字节。
    iv        -- 初始化向量，长度为8字节。

    返回:
    加密后的密文，字节类型。
    """
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    padded_text = pad(plaintext, DES3.block_size)
    encrypted = cipher.encrypt(padded_text)
    return cipher.iv, encrypted


# 用户输入明文
plaintext = input("请输入明文：").encode('utf-8')

# 生成随机密钥（3DES需要24字节的密钥）
key = get_random_bytes(24)

# 生成随机初始化向量IV
iv = get_random_bytes(DES3.block_size)

# 加密明文
iv_encrypted, encrypted = des3_encrypt(plaintext, key, iv)

# 显示加密后的密文和初始化向量
print("初始化向量（十六进制）:", iv_encrypted.hex())
print("加密后的密文（十六进制）:", encrypted.hex())

# 保存密钥，以便解密时使用
print("请保存以下密钥，以便将来解密：")
print("密钥（十六进制）:", key.hex())
