def caesar_cipher_encrypt(text, shift):
    """
    凯撒密码加密函数
    :param text: 要加密的文本
    :param shift: 移动的位数
    :return: 加密后的文本
    """
    result = ""
    for char in text:
        if char.isalpha():  # 检查字符是否为字母
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char  # 非字母字符不变
    return result

def encrypt_main():
    plain_text = input("请输入明文: ")
    shift = int(input("请输入位移数: "))
    encrypted_text = caesar_cipher_encrypt(plain_text, shift)
    print("加密后文本:", encrypted_text)

if __name__ == "__main__":
    encrypt_main()