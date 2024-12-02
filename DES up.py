from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# DES加密函数
def des_encrypt(plaintext, key):
    """
    使用DES算法加密明文。

    参数:
    plaintext -- 要加密的明文，必须是字节类型。
    key       -- DES加密使用的密钥，长度为8字节。

    返回:
    加密后的密文，字节类型。
    """
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext, DES.block_size)
    encrypted = cipher.encrypt(padded_text)
    return encrypted

def encrypt_main():
    # 用户输入明文
    plaintext = input("请输入明文：").encode('utf-8')

    # 生成8字节长度的随机密钥
    key = get_random_bytes(8)

    # 加密明文
    encrypted = des_encrypt(plaintext, key)

    # 显示加密后的密文
    print("加密后的密文（十六进制）:", encrypted.hex())

    # 保存密钥和密文，以便解密时使用
    print("请保存以下密钥和密文，以便将来解密：")
    print("密钥（十六进制）:", key.hex())
    print("密文（十六进制）:", encrypted.hex())

if __name__ == "__main__":
    encrypt_main()