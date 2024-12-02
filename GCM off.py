from Crypto.Cipher import AES
from binascii import unhexlify


def aes_gcm_decrypt(key, nonce, ciphertext_hex, tag_hex, aad):
    """
    使用AES-GCM算法对密文进行解密。
    """
    # 将十六进制字符串转换为字节串
    ciphertext = unhexlify(ciphertext_hex)
    tag = unhexlify(tag_hex)
    nonce = unhexlify(nonce)

    # 创建AES解密对象，使用GCM模式
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

    # 设置关联数据
    cipher.update(aad.encode('utf-8'))

    try:
        # 解密并验证标签
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        return plaintext.decode('utf-8')
    except ValueError:
        print("解密失败或标签验证错误")
        return None


# 用户输入密文（十六进制字符串）、标签（十六进制字符串）、nonce（十六进制字符串）和关联数据（AAD）
ciphertext_hex = input("请输入密文（十六进制）：")
tag_hex = input("请输入标签（十六进制）：")
nonce_hex = input("请输入nonce（十六进制）：")
aad = input("请输入关联数据（AAD）：")

# 用户输入密钥（十六进制字符串）
key_hex = input("请输入密钥（十六进制）：")
key = unhexlify(key_hex)

# 进行GCM解密
plaintext = aes_gcm_decrypt(key, nonce_hex, ciphertext_hex, tag_hex, aad)

if plaintext:
    print("解密后的明文:", plaintext)