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

    return ''.join(cipher_text)


def main():
    # 用户输入明文和栅栏数
    plain_text = input("请输入明文: ")
    num_rails = int(input("请输入栅栏数: "))
    cipher_text = encrypt(plain_text, num_rails)
    print("加密后文本:", cipher_text)


if __name__ == "__main__":
    main()