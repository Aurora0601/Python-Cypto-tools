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

def encode_main():
    # 用户输入要编码的文本
    text_to_encode = input("请输入要编码的文本: ")
    # 将文本转换为bytes
    text_to_encode_bytes = text_to_encode.encode('utf-8')
    # 进行Base16编码
    encoded_text = base16_encode(text_to_encode_bytes)
    print("Base16编码后文本:", encoded_text)

if __name__ == "__main__":
    encode_main()