def encode_to_unicode_escape(plaintext):
    # 创建一个列表来存储带有 \u 前缀的码点字符串
    escaped_code_points = []

    # 遍历明文中的每个字符
    for char in plaintext:
        # 获取字符的 Unicode 码点
        code_point = ord(char)
        # 将码点格式化为 \uXXXX 形式
        escaped_string = f'\\u{code_point:04x}'  # 使用小写十六进制，并填充到4位
        # 将格式化后的字符串添加到列表中
        escaped_code_points.append(escaped_string)

    # 将带有 \u 前缀的码点字符串列表连接成一个单一的字符串
    # 使用空格或其他分隔符分隔，这里我们使用空格
    escaped_output = ' '.join(escaped_code_points)

    return escaped_output


def main():
    # 提示用户输入明文
    plaintext = input("请输入明文: ")

    # 编码并格式化输出，带有 \u 前缀
    escaped_output = encode_to_unicode_escape(plaintext)

    # 打印格式化后的输出
    print("编码并格式化后的输出（带 \\u 前缀）:")
    print(escaped_output)  # 正确调用 print 函数，并使用正确的变量名 escaped_output


# 程序入口
if __name__ == "__main__":
    main()