import string

# 定义Base62字符集
BASE62_CHARS = string.ascii_letters + string.digits
BASE62_VALUES = {char: value for value, char in enumerate(BASE62_CHARS)}

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

def decode_main():
    encoded_input = input("请输入Base62编码的字符串: ")
    decoded_data = base62_decode(encoded_input)
    if decoded_data:
        print(f"解密后的明文: {decoded_data.decode('utf-8')}")

if __name__ == "__main__":
    decode_main()