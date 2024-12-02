import string

# Base36字符集
BASE36_CHARSET = string.digits + string.ascii_uppercase
# 映射表
BASE36_VALUES = {char: i for i, char in enumerate(BASE36_CHARSET)}
BASE36_INVERSE = {i: char for i, char in enumerate(BASE36_CHARSET)}

def base36_decode(encoded):
    """将Base36字符串解码为整数"""
    number = 0
    for char in encoded:
        if char not in BASE36_VALUES:
            raise ValueError(f"Invalid Base36 character: {char}")
        number = number * 36 + BASE36_VALUES[char]
    return number

def decode_main():
    encoded = input("输入要解密的Base36字符串: ")
    try:
        decoded = base36_decode(encoded)
        print(f"解密后的整数: {decoded}")
    except ValueError as e:
        print(f"解码错误: {e}")

if __name__ == "__main__":
    decode_main()