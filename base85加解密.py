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


def base85_decode(encoded):
    """
    将Base85字符串解码为字节数据。

    参数:
    encoded (str): 要解码的Base85字符串。

    返回:
    bytes: 解码后的字节数据。
    """
    encoded = encoded.rstrip('~')  # 移除尾部的'~'填充字符
    decoded = bytearray()
    accumulator = 0
    bits_left = 0

    for char in encoded:
        if char not in BASE85_DICT:
            raise ValueError(f"无效的Base85字符: {char}")

        accumulator = (accumulator << 5) + BASE85_DICT[char]
        bits_left += 5

        while bits_left >= 8:
            decoded.append((accumulator >> (bits_left - 8)) & 0xFF)
            accumulator &= (1 << (bits_left - 8)) - 1
            bits_left -= 8

    # 检查填充是否正确（剩余位应该全为0）
    if bits_left > 0 and accumulator != 0:
        raise ValueError("无效的Base85编码（填充错误）")

    return bytes(decoded)



def main():
    print("请选择操作:")
    print("1. 加密 (Encode)")
    print("2. 解密 (Decode)")
    choice = input("输入1或2: ")

    if choice == '1':
        # 输入明文并转换为字节数据
        plaintext = input("请输入明文: ")
        data_bytes = plaintext.encode('utf-8')

        # 加密（编码）
        encoded_data = base85_encode(data_bytes)
        print(f"加密后的Base85字符串: {encoded_data}")

    elif choice == '2':
        # 输入Base85编码的字符串
        encoded_input = input("请输入Base85编码的字符串: ")

        # 解密（解码）
        decoded_data = base85_decode(encoded_input)
        print(f"解密后的明文: {decoded_data.decode('utf-8')}")

    else:
        print("无效的选择，请输入1或2。")


if __name__ == "__main__":
    main()