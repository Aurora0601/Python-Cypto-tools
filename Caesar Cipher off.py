def caesar_cipher_decrypt(text, shift):
    """
    凯撒密码解密函数
    :param text: 要解密的文本
    :param shift: 移动的位数
    :return: 解密后的文本
    """
    result = ""
    for char in text:
        if char.isalpha():  # 检查字符是否为字母
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += char  # 非字母字符不变
    return result

def decrypt_main():
    plain_text = input("请输入明文: ")
    print("所有可能的解密结果：")
    for i in range(26):  # 遍历所有26个可能的位移
        decrypted_text = caesar_cipher_decrypt(plain_text, i)
        print(f"位移 {i}: {decrypted_text}")

if __name__ == "__main__":
    decrypt_main()