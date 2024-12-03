from Crypto.Cipher import ARC4
from Crypto.Random import get_random_bytes

def rc4_encrypt(plaintext, key):
    """
    使用RC4算法加密明文。

    参数:
    plaintext -- 要加密的明文，必须是字节类型。
    key       -- RC4加密使用的密钥。

    返回:
    加密后的密文，字节类型。
    """
    cipher = ARC4.new(key)
    return cipher.encrypt(plaintext)

def encrypt_main():
    # 用户输入明文
    plaintext = input("请输入明文：").encode('utf-8')

    # 生成随机密钥
    key = get_random_bytes(16)  # RC4密钥长度可以是1到256字节

    # 保存密钥
    print("请保存以下密钥，以便将来解密：")
    print("密钥（十六进制）:", key.hex())

    # 加密明文
    encrypted = rc4_encrypt(plaintext, key)

    # 显示加密后的密文
    print("加密后的密文（十六进制）:", encrypted.hex())

if __name__ == "__main__":
    encrypt_main()
