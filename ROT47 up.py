def rot47(text):
    """对输入的文本进行ROT47编码"""
    result = []
    for char in text:
        # 获取字符的ASCII码
        ascii_value = ord(char)

        # 对于ASCII值在33到126之间的字符进行ROT47编码
        if 33 <= ascii_value <= 126:
            # 进行循环移位
            rotated_value = (ascii_value - 33 + 47) % 94 + 33
            result.append(chr(rotated_value))
        else:
            # 对于ASCII值不在33到126之间的字符，保持不变（例如空格、换行符等）
            result.append(char)

    # 将结果列表转换为字符串并返回
    return ''.join(result)


def main():
    # 提示用户输入明文
    plaintext = input("请输入明文: ")

    # 对明文进行ROT47编码
    ciphertext = rot47(plaintext)

    # 输出密文
    print("ROT47编码后的密文:", ciphertext)


if __name__ == "__main__":
    main()