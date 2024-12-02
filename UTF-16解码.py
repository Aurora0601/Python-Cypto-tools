import re


def decode_unicode_escape(escaped_string):
    # 使用正则表达式找到所有的 \uXXXX 序列
    matches = re.findall(r'\\u([\da-fA-F]{4})', escaped_string)

    # 将每个匹配的十六进制数转换为对应的 Unicode 字符
    unicode_chars = [chr(int(match, 16)) for match in matches]

    # 将字符列表组合成一个字符串
    decoded_string = ''.join(unicode_chars)

    return decoded_string


def main():
    # 提示用户输入带有 \u 前缀的 Unicode 码点字符串（密文）
    escaped_input = input("请输入带有 \\u 前缀的 Unicode 码点字符串（密文）: ")

    # 解码输入的密文
    decoded_string = decode_unicode_escape(escaped_input)

    # 输出解码后的字符串
    print("解码后的字符串:")
    print(decoded_string)


if __name__ == "__main__":
    main()