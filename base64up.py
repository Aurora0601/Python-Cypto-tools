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

def encode_main():
    text_to_encode = input("请输入要编码的文本: ")
    encoded_text = base64_encode(text_to_encode)
    print("Base64编码后文本:", encoded_text)

if __name__ == "__main__":
    encode_main()