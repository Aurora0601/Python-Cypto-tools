from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from binascii import hexlify


def aes_eax_encrypt(key, plaintext, aad):
    """
    使用AES-EAX算法对明文进行加密。
    """
    # 生成随机nonce，EAX模式要求nonce是随机的，但不需要保密
    nonce = get_random_bytes(16)

    # 创建AES加密对象，使用EAX模式
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    # 设置关联数据
    cipher.update(aad.encode('utf-8'))

    # 加密明文
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))

    return {
        'ciphertext': hexlify(ciphertext).decode('utf-8'),
        'tag': hexlify(tag).decode('utf-8'),
        'nonce': hexlify(nonce).decode('utf-8')
    }


# 用户输入明文和关联数据
plaintext = input("请输入明文：")
aad = input("请输入关联数据（AAD）：")

# 生成随机密钥（16字节）
key = get_random_bytes(16)  # AES-128

# 进行EAX加密
result = aes_eax_encrypt(key, plaintext, aad)

print("加密后的密文（十六进制）:", result['ciphertext'])
print("使用的标签（十六进制）:", result['tag'])
print("使用的nonce（十六进制）:", result['nonce'])
print("使用的密钥（十六进制）:", hexlify(key).decode())
