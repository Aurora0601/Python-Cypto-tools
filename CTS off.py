from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from binascii import unhexlify


def cts_decrypt(key, iv, ciphertext_hex):
    """
    使用AES-CBC算法对密文进行解密，并进行CTS处理。
    """
    # 将十六进制字符串转换为字节串
    ciphertext = unhexlify(ciphertext_hex)
    # 创建AES解密对象，使用CBC模式
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 进行CTS处理
    if len(ciphertext) % AES.block_size == 0:
        # 将最后两个块交换位置
        last_block = ciphertext[-AES.block_size:]
        second_last_block = ciphertext[-2 * AES.block_size:-AES.block_size]
        temp = second_last_block
        second_last_block = last_block
        last_block = temp
        ciphertext = ciphertext[:-2 * AES.block_size] + second_last_block + last_block

    # 解密
    padded_plaintext = cipher.decrypt(ciphertext)
    # 去除填充
    plaintext = unpad(padded_plaintext, AES.block_size).decode('utf-8')
    return plaintext


# 用户输入密文（十六进制字符串）、密钥（十六进制字符串）和IV（十六进制字符串）
ciphertext_hex = input("请输入密文（十六进制）：")
key_hex = input("请输入密钥（十六进制）：")
iv_hex = input("请输入IV（十六进制）：")

# 将十六进制字符串转换为字节串
key = unhexlify(key_hex)
iv = unhexlify(iv_hex)

# 进行CTS解密
plaintext = cts_decrypt(key, iv, ciphertext_hex)

print("解密后的明文:", plaintext)