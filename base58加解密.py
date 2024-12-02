import base58


def base58_encode(data):
    """
    Base58编码函数
    :param data: 要编码的字符串（bytes类型）
    :return: Base58编码后的字符串
    """
    # 使用base58模块进行编码
    encoded_data = base58.b58encode(data)
    # 将编码后的bytes类型转换为str类型
    return encoded_data.decode('utf-8')


def base58_decode(data):
    """
    Base58解码函数
    :param data: 要解码的Base58编码字符串（str类型）
    :return: 解码后的原始字符串（bytes类型）
    """
    # 使用base58模块进行解码
    decoded_data = base58.b58decode(data)
    return decoded_data


def main():
    # 用户选择编码或解码
    direction = input("请选择编码(encode)或解码(decode): ")

    if direction.lower() == 'encode':
        # 用户输入要编码的文本
        text_to_encode = input("请输入要编码的文本: ")
        # 将文本转换为bytes
        text_to_encode_bytes = text_to_encode.encode('utf-8')
        # 进行Base58编码
        encoded_text = base58_encode(text_to_encode_bytes)
        print("Base58编码后文本:", encoded_text)
    elif direction.lower() == 'decode':
        # 用户输入要解码的Base58编码文本
        text_to_decode = input("请输入要解码的Base58编码文本: ")
        # 进行Base58解码
        decoded_text = base58_decode(text_to_decode)
        # 将bytes类型的解码结果转换为str类型的字符串
        print("Base58解码后文本:", decoded_text.decode('utf-8'))
    else:
        print("无效的方向选择，请输入 'encode' 或 'decode'。")


if __name__ == "__main__":
    main()