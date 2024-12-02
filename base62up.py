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

def encode_main():
    plaintext = input("请输入明文: ")
    data_bytes = plaintext.encode('utf-8')
    encoded_data = base62_encode(data_bytes)
    print(f"加密后的Base62字符串: {encoded_data}")

if __name__ == "__main__":
    encode_main()