def string_to_hex_escape(input_string):
    # 使用列表推导式和 ord 函数来获取每个字符的 ASCII/Unicode 码点，并将其格式化为 \xHH 形式
    hex_escape_string = ''.join(f'\\x{ord(char):02x}' for char in input_string)
    return hex_escape_string


def main():
    # 提示用户输入字符串
    input_string = input("请输入字符串: ")

    # 转换字符串为十六进制转义序列
    hex_escape_string = string_to_hex_escape(input_string)

    # 输出结果
    print("字符串的十六进制转义序列表示形式:")
    print(hex_escape_string)


# 程序入口
if __name__ == "__main__":
    main()