def decrypt(cipher_text, num_rails):
    """
    栅栏密码解密函数
    :param cipher_text: 密文
    :param num_rails: 栅栏数
    :return: 解密后的明文
    """
    rail_length = len(cipher_text) // num_rails
    plain_text = [''] * len(cipher_text)
    used_chars = [False] * len(cipher_text)  # 跟踪哪些字符已被使用

    # 由于填充的@可能在每行的末尾，我们需要按顺序填充明文
    for i in range(len(cipher_text)):
        rail_index = i % num_rails
        # 计算在明文中的位置，但要考虑@可能导致的长度不一致
        # 我们使用一个循环来找到第一个未使用的位置
        for j in range(rail_length):
            position = (j * num_rails) + rail_index
            if not used_chars[position]:
                plain_text[position] = cipher_text[i]
                used_chars[position] = True
                break

    # 移除末尾的@符号（如果有的话）
    result = ''.join(plain_text).rstrip('@')

    # 由于我们可能填充了额外的@，我们需要移除它们导致的多余空格
    # 但由于我们按顺序填充，且没有跳过任何位置，所以实际上这一步可能是多余的，
    # 因为rstrip('@')已经足够。但为了清晰，我还是保留了这个步骤的注释。

    return result


def main():
    # 用户输入密文和栅栏数
    cipher_text = input("请输入密文: ")
    num_rails = int(input("请输入栅栏数(与加密时相同): "))
    plain_text = decrypt(cipher_text, num_rails)
    print("解密后文本:", plain_text)


if __name__ == "__main__":
    main()
