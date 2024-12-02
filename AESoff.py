from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# AES解密函数
def aes_decrypt(ciphertext, key, iv):
    # 创建一个新的AES cipher
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 解密
    decrypted = cipher.decrypt(ciphertext)
    # 去除填充
    unpadded_text = unpad(decrypted, AES.block_size)
    return unpadded_text

# 用户需要提供相同的密钥和IV进行解密
iv_for_demo = bytes.fromhex(input("请输入初始化向量（十六进制）："))
key_for_demo = bytes.fromhex(input("请输入密钥（十六进制）："))
ciphertext_for_demo = bytes.fromhex(input("请输入要解密的密文（十六进制）："))

# 解密密文
decrypted = aes_decrypt(ciphertext_for_demo, key_for_demo, iv_for_demo)

# 显示解密后的明文
print("解密后的明文:", decrypted.decode('utf-8'))
