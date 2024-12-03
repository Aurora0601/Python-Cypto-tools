from Crypto.Cipher import AES
from binascii import unhexlify


def aes_ocb_decrypt(key, nonce, ciphertext_hex, tag_hex):
    """
    使用AES-OCB算法对密文进行解密。
    """
    # 将十六进制字符串转换为字节串
    ciphertext = unhexlify(ciphertext_hex)
    tag = unhexlify(tag_hex)
    nonce = unhexlify(nonce)

    # 创建AES解密对象，使用OCB模式
    cipher = AES.new(key, AES.MODE_OCB, nonce=nonce)

    try:
        # 解密并验证标签
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        return plaintext.decode('utf-8')
    except ValueError:
        print("解密失败或标签验证错误")
        return None


# 用户输入密文（十六进制字符串）、标签（十六进制字符串）和nonce（十六进制字符串）
ciphertext_hex = input("请输入密文（十六进制）：")
tag_hex = input("请输入标签（十六进制）：")
nonce_hex = input("请输入nonce（十六进制）：")

# 用户输入密钥（十六进制字符串）
key_hex = input("请输入密钥（十六进制）：")
key = unhexlify(key_hex)

# 进行OCB解密
plaintext = aes_ocb_decrypt(key, nonce_hex, ciphertext_hex, tag_hex)

if plaintext:
    print("解密后的明文:", plaintext)
