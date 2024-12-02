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

def encode_main():
    try:
        number = int(input("输入要加密的整数: "))
        encoded = base36_encode(number)
        print(f"加密后的Base36字符串: {encoded}")
    except ValueError as e:
        print(f"输入错误: {e}")

if __name__ == "__main__":
    encode_main()