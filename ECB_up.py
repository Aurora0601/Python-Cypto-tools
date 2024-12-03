from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os


def encrypt_ecb(plaintext, key):
    # AES块大小为16字节，因此需要进行填充
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext.encode('utf-8')) + padder.finalize()

    # 创建ECB模式的Cipher对象并加密
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    return ciphertext


def main():
    # 生成一个随机的AES密钥（AES-256，密钥长度为32字节）
    key = os.urandom(32)
    print("密钥（十六进制表示，用于解密）:", key.hex())

    # 提示用户输入明文
    plaintext = input("请输入要加密的明文（中文也可以）: ")

    # 加密明文
    ciphertext = encrypt_ecb(plaintext, key)
    print("加密后的密文（十六进制表示）:", ciphertext.hex())


if __name__ == "__main__":
    main()
