import base64


def base64_encode(data):
    """
    Base64编码函数
    :param data: 要编码的字符串（str类型）
    :return: Base64编码后的字符串
    """
    # 将输入的字符串转换为bytes类型
    data_bytes = data.encode('utf-8')
    # 使用base64模块进行编码
    encoded_data = base64.b64encode(data_bytes)
    # 将编码后的bytes类型转换为str类型
    return encoded_data.decode('utf-8')


def base64_decode(data):
    """
    Base64解码函数
    :param data: 要解码的Base64编码字符串（str类型）
    :return: 解码后的原始字符串
    """
    # 将输入的Base64编码字符串转换为bytes类型
    data_bytes = data.encode('utf-8')
    # 使用base64模块进行解码
    decoded_data = base64.b64decode(data_bytes)
    # 将解码后的bytes类型转换为str类型
    return decoded_data.decode('utf-8')


def main():
    # 用户选择编码或解码
    direction = input("请选择编码(encode)或解码(decode): ")

    if direction.lower() == 'encode':
        # 用户输入要编码的文本
        text_to_encode = input("请输入要编码的文本: ")
        # 进行Base64编码
        encoded_text = base64_encode(text_to_encode)
        print("Base64编码后文本:", encoded_text)
    elif direction.lower() == 'decode':
        # 用户输入要解码的Base64编码文本
        text_to_decode = input("请输入要解码的Base64编码文本: ")
        # 进行Base64解码
        decoded_text = base64_decode(text_to_decode)
        print("Base64解码后文本:", decoded_text)
    else:
        print("无效的方向选择，请输入 'encode' 或 'decode'。")


if __name__ == "__main__":
    main()