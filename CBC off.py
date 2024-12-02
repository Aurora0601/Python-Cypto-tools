from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def decrypt_cbc(ciphertext_with_iv, key):
    # 提取IV（前16字节）和密文（剩余部分）
    iv = ciphertext_with_iv[:16]  # 直接使用16作为IV的长度
    ciphertext = ciphertext_with_iv[16:]

    # 创建CBC模式的Cipher对象并解密
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
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

    # 用户需要输入加密后的密文（包括IV，十六进制表示）
    ciphertext_with_iv_hex = input("请输入要解密的密文（包括IV，十六进制表示）: ")
    ciphertext_with_iv = bytes.fromhex(ciphertext_with_iv_hex)

    # 解密密文
    decrypted_plaintext = decrypt_cbc(ciphertext_with_iv, key)
    print("解密后的明文:", decrypted_plaintext)

if __name__ == "__main__":
    main()