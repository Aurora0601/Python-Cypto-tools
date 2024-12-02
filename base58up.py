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

def encode_main():
    # 用户输入要编码的文本
    text_to_encode = input("请输入要编码的文本: ")
    # 将文本转换为bytes
    text_to_encode_bytes = text_to_encode.encode('utf-8')
    # 进行Base58编码
    encoded_text = base58_encode(text_to_encode_bytes)
    print("Base58编码后文本:", encoded_text)

if __name__ == "__main__":
    encode_main()