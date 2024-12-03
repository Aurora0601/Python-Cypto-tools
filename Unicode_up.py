def unicode_encode(data):
    """
    将字符串转换为其Unicode表示形式
    :param data: 要编码的字符串（str类型）
    :return: Unicode表示形式的字符串
    """
    # 使用ord函数获取每个字符的Unicode码点，并转换为十六进制
    return ' '.join(f'\\u{ord(c):04x}' for c in data)

def encode_main():
    text_to_encode = input("请输入要编码的文本: ")
    encoded_text = unicode_encode(text_to_encode)
    print("Unicode编码后文本:", encoded_text)

if __name__ == "__main__":
    encode_main()
