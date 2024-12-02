import base91

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

def decode_main():
    text_to_decode = input("请输入要解码的Base91编码文本: ")
    decoded_text = base91_decode(text_to_decode)
    print("Base91解码后文本:", decoded_text)

if __name__ == "__main__":
    decode_main()