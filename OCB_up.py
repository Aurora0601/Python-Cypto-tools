from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from binascii import hexlify


def aes_ocb_encrypt(key, nonce, plaintext):
    """
    使用AES-OCB算法对明文进行加密。
    """
    # 创建AES加密对象，使用OCB模式
    cipher = AES.new(key, AES.MODE_OCB, nonce=nonce)

    # 加密明文
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))

    return {
        'ciphertext': hexlify(ciphertext).decode('utf-8'),
        'tag': hexlify(tag).decode('utf-8')
    }


# 用户输入明文
plaintext = input("请输入明文：")

# 生成随机密钥和nonce（都是16字节）
key = get_random_bytes(16)  # AES-128
nonce = get_random_bytes(15)  # OCB要求nonce长度为15字节

# 进行OCB加密
result = aes_ocb_encrypt(key, nonce, plaintext)

print("加密后的密文（十六进制）:", result['ciphertext'])
print("使用的标签（十六进制）:", result['tag'])
print("使用的密钥（十六进制）:", hexlify(key).decode())
print("使用的nonce（十六进制）:", hexlify(nonce).decode())
