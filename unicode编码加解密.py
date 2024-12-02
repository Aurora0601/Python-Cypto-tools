def unicode_encode(data):
    """
    将字符串转换为其Unicode表示形式
    :param data: 要编码的字符串（str类型）
    :return: Unicode表示形式的字符串
    """
    # 使用ord函数获取每个字符的Unicode码点，并转换为十六进制
    return ' '.join(f'\\u{ord(c):04x}' for c in data)


def unicode_decode(data):
    """
    将Unicode表示形式转换回原始字符串
    :param data: Unicode表示形式的字符串（str类型）
    :return: 原始字符串
    """
    # 将Unicode码点转换为字符串
    return bytes.fromhex(data.replace('\\u', '')).decode('unicode_escape')


def main():
    # 用户选择编码或解码
    direction = input("请选择编码(encode)或解码(decode): ")

    if direction.lower() == 'encode':
        # 用户输入要编码的文本
        text_to_encode = input("请输入要编码的文本: ")
        # 进行Unicode编码
        encoded_text = unicode_encode(text_to_encode)
        print("Unicode编码后文本:", encoded_text)
    elif direction.lower() == 'decode':
        # 用户输入要解码的Unicode编码文本
        text_to_decode = input("请输入要解码的Unicode编码文本: ")
        # 进行Unicode解码
        decoded_text = unicode_decode(text_to_decode)
        print("Unicode解码后文本:", decoded_text)
    else:
        print("无效的方向选择，请输入 'encode' 或 'decode'。")


if __name__ == "__main__":
    main()