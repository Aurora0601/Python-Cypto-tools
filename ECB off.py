from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend


def decrypt_ecb(ciphertext, key):
    # 创建ECB模式的Cipher对象并解密
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # 去除填充并解码为字符串
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext.decode('utf-8')


def main():
    # 用户需要输入之前加密时使用的密钥（十六进制表示）
    key_hex = input("请输入用于解密的密钥（十六进制表示）: ")
    key = bytes.fromhex(key_hex)

    # 用户需要输入加密后的密文（十六进制表示）
    ciphertext_hex = input("请输入要解密的密文（十六进制表示）: ")
    ciphertext = bytes.fromhex(ciphertext_hex)

    # 解密密文
    decrypted_plaintext = decrypt_ecb(ciphertext, key)
    print("解密后的明文:", decrypted_plaintext)


if __name__ == "__main__":
    main()