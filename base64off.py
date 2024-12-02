import base64

def base64_decode(data):
    """
    Base64解码函数
    :param data: 要解码的Base64编码字符串（str类型）
    :return: 解码后的原始字符串
    """
    # 将输入的Base64编码字符串转换为bytes类型
    data_bytes = data.encode('utf-8')
    try:
        # 使用base64模块进行解码
        decoded_data = base64.b64decode(data_bytes)
        # 将解码后的bytes类型转换为str类型
        return decoded_data.decode('utf-8')
    except base64.binascii.Error as e:
        print("解码错误：", e)
        return None

def decode_main():
    text_to_decode = input("请输入要解码的Base64编码文本: ")
    decoded_text = base64_decode(text_to_decode)
    if decoded_text:
        print("Base64解码后文本:", decoded_text)

if __name__ == "__main__":
    decode_main()