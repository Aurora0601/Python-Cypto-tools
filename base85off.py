BASE85_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()-_=+[]{}|;:,.<>?/"
BASE85_DICT = {char: index for index, char in enumerate(BASE85_CHARS)}

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

def decode_main():
    encoded_input = input("请输入Base85编码的字符串: ")
    decoded_data = base85_decode(encoded_input)
    print("解密后的明文:", decoded_data.decode('utf-8'))

if __name__ == "__main__":
    decode_main()