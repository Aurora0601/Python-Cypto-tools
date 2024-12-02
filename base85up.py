BASE85_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()-_=+[]{}|;:,.<>?/"
BASE85_DICT = {char: index for index, char in enumerate(BASE85_CHARS)}

def base85_encode(data):
    """
    将字节数据编码为Base85字符串。

    参数:
    data (bytes): 要编码的字节数据。

    返回:
    str: 编码后的Base85字符串。
    """
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("输入数据必须是字节或字节数组")

    encoded = []
    accumulator = 0
    bits_left = 0

    for byte in data:
        accumulator = (accumulator << 8) + byte
        bits_left += 8

        while bits_left >= 5:
            encoded_char_index = accumulator >> (bits_left - 5)
            encoded.append(BASE85_CHARS[encoded_char_index])
            accumulator &= (1 << (bits_left - 5)) - 1
            bits_left -= 5

    # 处理剩余位，用'~'填充
    if bits_left > 0:
        encoded.append(BASE85_CHARS[accumulator << (5 - bits_left)])
        encoded.extend('~' * (5 - bits_left))

    return ''.join(encoded)

def encode_main():
    plaintext = input("请输入明文: ")
    data_bytes = plaintext.encode('utf-8')
    encoded_data = base85_encode(data_bytes)
    print("加密后的Base85字符串:", encoded_data)

if __name__ == "__main__":
    encode_main()