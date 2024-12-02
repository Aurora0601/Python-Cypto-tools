def encrypt(plain_text, num_rails):
    """
    栅栏密码加密函数
    :param plain_text: 明文
    :param num_rails: 栅栏数
    :return: 加密后的密文
    """
    # 计算每行的长度，并用@填充不足的部分
    rail_length = (len(plain_text) + num_rails - 1) // num_rails
    plain_text += '@' * (rail_length * num_rails - len(plain_text))

    cipher_text = [''] * num_rails
    rail_index = 0
    for char in plain_text:
        cipher_text[rail_index] += char
        rail_index = (rail_index + 1) % num_rails
    result = ''.join(cipher_text)
    return result


def decrypt(cipher_text, num_rails):
    """
    栅栏密码解密函数
    :param cipher_text: 密文
    :param num_rails: 栅栏数
    :return: 解密后的明文
    """
    rail_length = len(cipher_text) // num_rails
    plain_text = [''] * len(cipher_text)

    for i in range(len(cipher_text)):
        rail_index = i % num_rails
        position = (i // num_rails) + (rail_index * rail_length)
        plain_text[position] = cipher_text[i]

    # 移除末尾的@符号
    result = ''.join(plain_text).rstrip('@')
    return result


def main():
    # 用户选择加密或解密
    direction = input("请选择加密(encrypt)或解密(decrypt): ")
    if direction.lower() == 'encrypt':
        # 用户输入明文和栅栏数
        plain_text = input("请输入明文: ")
        num_rails = int(input("请输入栅栏数: "))
        cipher_text = encrypt(plain_text, num_rails)
        print("加密后文本:", cipher_text)
    elif direction.lower() == 'decrypt':
        # 用户输入密文和栅栏数
        cipher_text = input("请输入密文: ")
        num_rails = int(input("请输入栅栏数: "))
        plain_text = decrypt(cipher_text, num_rails)
        print("解密后文本:", plain_text)
    else:
        print("无效的方向选择，请输入 'encrypt' 或 'decrypt'。")


if __name__ == "__main__":
    main()