from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad


# 3DES解密函数
def des3_decrypt(ciphertext, key, iv):
    """
    使用3DES算法解密密文。

    参数:
    ciphertext -- 要解密的密文，必须是字节类型。
    key       -- 3DES解密使用的密钥，长度为24字节。
    iv        -- 初始化向量，长度为8字节。

    返回:
    解密后的明文，字节类型。
    """
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext)
    unpadded_text = unpad(decrypted, DES3.block_size)
    return unpadded_text


# 用户需要提供相同的密钥和IV进行解密
iv_for_demo = bytes.fromhex(input("请输入初始化向量（十六进制）："))
key_for_demo = bytes.fromhex(input("请输入密钥（十六进制）："))
ciphertext_for_demo = bytes.fromhex(input("请输入要解密的密文（十六进制）："))

# 解密密文
decrypted = des3_decrypt(ciphertext_for_demo, key_for_demo, iv_for_demo)

# 显示解密后的明文
print("解密后的明文:", decrypted.decode('utf-8'))
