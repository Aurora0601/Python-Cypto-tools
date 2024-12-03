def xor_decrypt(ciphertext, key):
    # 将密文和密钥转换成二进制格式，然后进行异或操作
    plaintext = ''.join(chr(ord(char) ^ key) for char in ciphertext)
    return plaintext

# 用户输入密文和密钥
ciphertext = input("请输入密文: ")
key = int(input("请输入密钥（一个整数）: "))

# 解密
plaintext = xor_decrypt(ciphertext, key)
print("解密后的明文:", plaintext)
