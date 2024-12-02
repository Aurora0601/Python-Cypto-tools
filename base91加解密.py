import base91


def base91_encode(data):
    """
    Base91编码函数
    :param data: 要编码的字符串（str类型）
    :return: Base91编码后的字符串
    """
    # 将输入的字符串转换为bytes类型
    data_bytes = data.encode('utf-8')
    # 使用base91模块进行编码
    encoded_data = base91.encode(data_bytes)
    return encoded_data


def base91_decode(data):
    """
    Base91解码函数
    :param data: 要解码的Base91编码字符串（str类型）
    :return: 解码后的原始字符串
    """
    # 使用base91模块进行解码
    decoded_data = base91.decode(data)
    # 将解码后的bytes类型转换为str类型的字符串
    return decoded_data.decode('utf-8')


def main():
    # 用户选择编码或解码
    direction = input("请选择编码(encode)或解码(decode): ")

    if direction.lower() == 'encode':
        # 用户输入要编码的文本
        text_to_encode = input("请输入要编码的文本: ")
        # 进行Base91编码
        encoded_text = base91_encode(text_to_encode)
        print("Base91编码后文本:", encoded_text)
    elif direction.lower() == 'decode':
        # 用户输入要解码的Base91编码文本
        text_to_decode = input("请输入要解码的Base91编码文本: ")
        # 进行Base91解码
        decoded_text = base91_decode(text_to_decode)
        print("Base91解码后文本:", decoded_text)
    else:
        print("无效的方向选择，请输入 'encode' 或 'decode'。")


if __name__ == "__main__":
    main()