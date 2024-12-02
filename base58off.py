import base58

def base58_decode(data):
    """
    Base58解码函数
    :param data: 要解码的Base58编码字符串（str类型）
    :return: 解码后的原始字符串（bytes类型）
    """
    # 使用base58模块进行解码
    decoded_data = base58.b58decode(data)
    return decoded_data

def decode_main():
    # 用户输入要解码的Base58编码文本
    text_to_decode = input("请输入要解码的Base58编码文本: ")
    # 进行Base58解码
    decoded_text = base58_decode(text_to_decode)
    # 将bytes类型的解码结果转换为str类型的字符串
    print("Base58解码后文本:", decoded_text.decode('utf-8'))

if __name__ == "__main__":
    decode_main()