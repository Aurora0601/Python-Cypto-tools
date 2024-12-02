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

def encode_main():
    text_to_encode = input("请输入要编码的文本: ")
    encoded_text = base91_encode(text_to_encode)
    print("Base91编码后文本:", encoded_text)

if __name__ == "__main__":
    encode_main()