def xor_encrypt(plaintext, key):
    # 将明文和密钥转换成二进制格式，然后进行异或操作
    ciphertext = ''.join(chr(ord(char) ^ key) for char in plaintext)
    return ciphertext

# 用户输入明文和密钥
plaintext = input("请输入明文: ")
key = int(input("请输入密钥（一个整数）: "))

# 加密
ciphertext = xor_encrypt(plaintext, key)
print("加密后的密文:", ciphertext)