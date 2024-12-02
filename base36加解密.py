import string

# Base36字符集
BASE36_CHARSET = string.digits + string.ascii_uppercase
# 映射表
BASE36_VALUES = {char: i for i, char in enumerate(BASE36_CHARSET)}
BASE36_INVERSE = {i: char for i, char in enumerate(BASE36_CHARSET)}


def base36_encode(number):
    """将整数编码为Base36字符串"""
    if number == 0:
        return '0'
    encoded = ''
    while number:
        encoded = BASE36_INVERSE[number % 36] + encoded
        number //= 36
    return encoded


def base36_decode(encoded):
    """将Base36字符串解码为整数"""
    number = 0
    for char in encoded:
        if char not in BASE36_VALUES:
            raise ValueError(f"Invalid Base36 character: {char}")
        number = number * 36 + BASE36_VALUES[char]
    return number


def main():
    print("请选择操作:")
    print("1. 加密（编码为Base36）")
    print("2. 解密（从Base36解码）")

    choice = input("输入选项（1或2）: ")

    if choice == '1':
        try:
            number = int(input("输入要加密的整数: "))
            encoded = base36_encode(number)
            print(f"加密后的Base36字符串: {encoded}")
        except ValueError as e:
            print(f"输入错误: {e}")
    elif choice == '2':
        encoded = input("输入要解密的Base36字符串: ")
        try:
            decoded = base36_decode(encoded)
            print(f"解密后的整数: {decoded}")
        except ValueError as e:
            print(f"解码错误: {e}")
    else:
        print("无效的选项，请选择1或2。")


if __name__ == "__main__":
    main()