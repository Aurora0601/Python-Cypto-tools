import binascii

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

def decode_main():
    # 用户输入要解码的Base16编码文本
    text_to_decode = input("请输入要解码的Base16编码文本: ")
    # 进行Base16解码
    decoded_text = base16_decode(text_to_decode)
    # 将bytes类型的解码结果转换为str类型的字符串
    print("Base16解码后文本:", decoded_text.decode('utf-8'))

if __name__ == "__main__":
    decode_main()