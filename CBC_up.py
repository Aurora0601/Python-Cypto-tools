from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

def encrypt_cbc(plaintext, key):
    # 生成一个随机的初始化向量（IV）
    iv = os.urandom(16)  # 正确的IV大小应该是16字节

    # AES块大小为16字节，因此需要进行填充
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext.encode('utf-8')) + padder.finalize()

    # 创建CBC模式的Cipher对象并加密
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    # 返回密文和IV（通常IV需要与密文一起存储或传输，以便解密时使用）
    return iv + ciphertext

def main():
    # 生成一个随机的AES密钥（AES-256，密钥长度为32字节）
    key = os.urandom(32)
    print("密钥（十六进制表示，用于解密）:", key.hex())

    # 提示用户输入明文
    plaintext = input("请输入要加密的明文（中文也可以）: ")

    # 加密明文
    ciphertext_with_iv = encrypt_cbc(plaintext, key)
    print("加密后的密文（包括IV，十六进制表示）:", ciphertext_with_iv.hex())

if __name__ == "__main__":
    main()
