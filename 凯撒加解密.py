def caesar_cipher(text, shift, direction='encrypt'):
    """
    凯撒密码加密或解密函数
    :param text: 要加密或解密的文本
    :param shift: 移动的位数
    :param direction: 加密('encrypt')或解密('decrypt')
    :return: 加密或解密后的文本
    """
    result = ""
    for char in text:
        if char.isalpha():  # 检查字符是否为字母
            ascii_offset = 65 if char.isupper() else 97
            if direction == 'encrypt':
                result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:  # 解密
                result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += char  # 非字母字符不变
    return result

def main():
    # 用户输入明文
    plain_text = input("请输入明文: ")
    # 用户选择加密或解密
    direction = input("请选择加密(encrypt)或解密(decrypt): ")

    if direction.lower() == 'encrypt':
        # 用户输入位移数
        shift = int(input("请输入位移数: "))
        result_text = caesar_cipher(plain_text, shift)
        print("加密后文本:", result_text)
    elif direction.lower() == 'decrypt':
        print("所有可能的解密结果：")
        for i in range(26):  # 遍历所有26个可能的位移
            decrypted_text = caesar_cipher(plain_text, i, 'decrypt')
            print(f"位移 {i}: {decrypted_text}")
    else:
        print("无效的方向选择，请输入 'encrypt' 或 'decrypt'。")

if __name__ == "__main__":
    main()