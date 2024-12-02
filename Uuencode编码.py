def simulate_custom_encoding(plain_text):
    """
    模拟自定义编码过程，将每个字母替换为字母表中的下一个字符，非字母字符保持不变。

    参数:
    plain_text (str): 要编码的明文。

    返回:
    str: 编码后的字符串。
    """
    encoded_text = []
    for char in plain_text:
        if 'A' <= char <= 'Z':
            encoded_char = chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            encoded_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
        else:
            encoded_char = char
        encoded_text.append(encoded_char)
    return ''.join(encoded_text)


# 主程序
if __name__ == "__main__":
    # 输入明文
    plain_text = input("请输入明文: ")

    # 获取编码后的字符串
    encoded_output = simulate_custom_encoding(plain_text)

    # 输出编码后的字符串
    print("编码后的字符串:")
    print(encoded_output)