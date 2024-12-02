from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from binascii import hexlify


def cts_encrypt(key, iv, plaintext):
    """
    使用AES-CBC算法对明文进行加密，并进行CTS处理。
    """
    # 创建AES加密对象，使用CBC模式
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 对明文进行填充，然后加密
    padded_plaintext = pad(plaintext.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)

    # 进行CTS处理
    if len(ciphertext) % AES.block_size == 0:
        # 将最后两个块交换位置
        last_block = ciphertext[-AES.block_size:]
        second_last_block = ciphertext[-2 * AES.block_size:-AES.block_size]
        ciphertext = ciphertext[:-2 * AES.block_size] + last_block + second_last_block

    return hexlify(ciphertext).decode('utf-8')


# 用户输入明文
plaintext = input("请输入明文（原始字符串）：")

# 生成随机密钥和IV（都是16字节）
key = get_random_bytes(16)
iv = get_random_bytes(AES.block_size)

# 进行CTS加密
ciphertext_hex = cts_encrypt(key, iv, plaintext)

print("加密后的密文（十六进制）:", ciphertext_hex)
print("使用的密钥（十六进制）:", hexlify(key).decode())
print("使用的IV（十六进制）:", hexlify(iv).decode())