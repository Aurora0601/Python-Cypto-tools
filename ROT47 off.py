def rot47_decrypt(ciphertext):
    """
    使用ROT47算法解密密文。

    参数:
    ciphertext -- 要解密的密文，必须是字符串类型。

    返回:
    解密后的明文，字符串类型。
    """
    plaintext = ""
    for char in ciphertext:
        if 33 <= ord(char) <= 126:  # 检查字符是否在ASCII码的可打印范围内
            decrypted_char = chr(33 + ((ord(char) - 33 - 47) % 94))
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext


# 用户输入密文进行解密
ciphertext = input("请输入要解密的密文：")
decrypted_text = rot47_decrypt(ciphertext)
print("解密后的明文:", decrypted_text)