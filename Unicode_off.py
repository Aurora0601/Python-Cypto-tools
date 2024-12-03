def unicode_decode(data):
    """
    将Unicode表示形式转换回原始字符串
    :param data: Unicode表示形式的字符串（str类型）
    :return: 原始字符串
    """
    # 将Unicode码点转换为字符串
    return data.encode().decode('unicode_escape')

def decode_main():
    text_to_decode = input("请输入要解码的Unicode编码文本: ")
    decoded_text = unicode_decode(text_to_decode)
    print("Unicode解码后文本:", decoded_text)

if __name__ == "__main__":
    decode_main()
