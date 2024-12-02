import string

# 定义Base62字符集
BASE62_CHARS = string.ascii_letters + string.digits
BASE62_VALUES = {char: value for value, char in enumerate(BASE62_CHARS)}


def base62_encode(data):
    """将字节数据编码为Base62字符串。"""
    num = int.from_bytes(data, 'big')  # 将字节数据转换为一个大整数
    encoded_str = ''
    while num > 0:
        num, remainder = divmod(num, 62)
        encoded_str = BASE62_CHARS[remainder] + encoded_str
    # 如果编码后的字符串为空，则返回'0'（表示输入数据为0字节或空）
    return encoded_str if encoded_str else '0'


def base62_decode(encoded):
    """将Base62字符串解码为字节数据。"""
    num = 0
    for char in encoded:
        num = num * 62 + BASE62_VALUES[char]

    # 计算原始数据的位数长度
    bit_length = len(encoded) * 6

    # 计算原始数据的字节长度（向上取整）
    byte_length = (bit_length + 7) // 8  # 相当于math.ceil(bit_length / 8)

    # 尝试将整数转换为字节数据
    try:
        decoded_bytes = num.to_bytes(byte_length, 'big')
    except OverflowError:
        # 这通常不应该发生，因为Python的int是任意精度的
        # 但如果发生了，可能是因为某种内部限制或bug
        print("解码错误：整数太大，无法转换为字节数据。")
        return None

    # 如果解码后的字节数据以空字节结尾（由于不完整的6位组），则去除它们
    # 注意：这假设输入是有效的Base62编码，并且没有额外的填充字符
    while decoded_bytes and decoded_bytes[-1] == 0:
        decoded_bytes = decoded_bytes[:-1]

    return decoded_bytes


def main():
    print("请选择操作:")
    print("1. 加密 (Encode to Base62)")
    print("2. 解密 (Decode from Base62)")
    choice = input("输入1或2: ")

    if choice == '1':
        # 输入明文并转换为字节数据
        plaintext = input("请输入明文: ")
        data_bytes = plaintext.encode('utf-8')

        # 加密（编码）
        encoded_data = base62_encode(data_bytes)
        print(f"加密后的Base62字符串: {encoded_data}")

    elif choice == '2':
        # 输入Base62编码的字符串
        encoded_input = input("请输入Base62编码的字符串: ")

        # 解密（解码）
        decoded_data = base62_decode(encoded_input)
        print(f"解密后的明文: {decoded_data.decode('utf-8')}")

    else:
        print("无效的选择，请输入1或2。")


if __name__ == "__main__":
    main()
