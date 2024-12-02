import binascii


def base16_encode(data):
    """
    Base16编码函数
    :param data: 要编码的字符串（bytes类型）
    :return: Base16编码后的字符串
    """
    # 使用binascii模块进行编码
    encoded_data = binascii.b2a_hex(data)
    # 将编码后的bytes类型转换为str类型
    return encoded_data.decode('utf-8')


def base16_decode(data):
    """
    Base16解码函数
    :param data: 要解码的Base16编码字符串（str类型）
    :return: 解码后的原始字符串（bytes类型）
    """
    # 将输入的Base16编码字符串转换为bytes类型
    data_bytes = data.encode('utf-8')
    # 使用binascii模块进行解码
    decoded_data = binascii.a2b_hex(data_bytes)
    return decoded_data


def main():
    # 用户选择编码或解码
    direction = input("请选择编码(encode)或解码(decode): ")

    if direction.lower() == 'encode':
        # 用户输入要编码的文本
        text_to_encode = input("请输入要编码的文本: ")
        # 将文本转换为bytes
        text_to_encode_bytes = text_to_encode.encode('utf-8')
        # 进行Base16编码
        encoded_text = base16_encode(text_to_encode_bytes)
        print("Base16编码后文本:", encoded_text)
    elif direction.lower() == 'decode':
        # 用户输入要解码的Base16编码文本
        text_to_decode = input("请输入要解码的Base16编码文本: ")
        # 进行Base16解码
        decoded_text = base16_decode(text_to_decode)
        # 将bytes类型的解码结果转换为str类型的字符串
        print("Base16解码后文本:", decoded_text.decode('utf-8'))
    else:
        print("无效的方向选择，请输入 'encode' 或 'decode'。")


if __name__ == "__main__":
    main()