def ascii_to_string(ascii_list):
    """将ASCII码列表转换为字符串"""
    return ''.join(chr(code) for code in ascii_list)


def string_to_ascii(input_string):
    """将字符串转换为ASCII码列表"""
    return [ord(char) for char in input_string]


def main():
    print("请选择操作:")
    print("1. 输入ASCII码列表转换为字符串")
    print("2. 输入字符串转换为ASCII码列表")

    choice = input("输入1或2: ")

    if choice == '1':
        # 提示用户输入ASCII码列表
        ascii_input = input("请输入ASCII码列表（以空格分隔）: ")
        # 将输入的字符串按空格分割成列表，并转换为整数
        ascii_list = list(map(int, ascii_input.split()))
        # 转换为字符串
        result_string = ascii_to_string(ascii_list)
        print("转换后的字符串:", result_string)

    elif choice == '2':
        # 提示用户输入字符串
        input_string = input("请输入字符串: ")
        # 转换为ASCII码列表
        result_ascii_list = string_to_ascii(input_string)
        print("转换后的ASCII码列表:", result_ascii_list)

    else:
        print("无效选择，请重新运行程序并选择1或2。")


if __name__ == "__main__":
    main()