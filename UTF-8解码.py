def hex_escape_string_to_utf8(hex_escape_string):
    # 由于 \x 转义序列在字符串字面量中不被直接解释，我们需要先将其转换为实际的字节序列
    # 方法是去除 \x 前缀，并将剩余的十六进制字符串传递给 bytes.fromhex()
    # 但是，由于字符串本身包含 \x，我们需要先对其进行处理
    # 一种简单的方法是使用字符串替换和正则表达式，但这里我们可以直接分割字符串

    # 创建一个空字节数组
    byte_array = bytearray()

    # 分割字符串，每次遇到 \x 就分割，但我们要两个一组（即 \xHH）
    for i in range(0, len(hex_escape_string), 4):  # 4 是因为 \x 占 2 个字符，HH 占 2 个字符
        hex_pair = hex_escape_string[i + 2:i + 4]  # 获取 HH 部分
        byte_value = int(hex_pair, 16)  # 将 HH 转换为整数（十六进制）
        byte_array.append(byte_value)  # 将整数添加到字节数组中

    # 或者，更简洁但可能稍慢的方法是使用正则表达式和 bytes.fromhex() 的组合，
    # 但这里为了展示手动处理的过程，我们使用上面的方法。

    # 不过，为了完整性，我也提供使用正则表达式的方法：
    # import re
    # match = re.findall(r'\\x([0-9a-fA-F]{2})', hex_escape_string)
    # byte_array = bytes.fromhex(''.join(match))

    # 将字节数组转换为字节序列，并解码为 UTF-8 字符串（在这个例子中，实际上是 ASCII）
    utf8_string = byte_array.decode('utf-8')

    return utf8_string


def main():
    # 提示用户输入包含 \x 转义序列的字符串
    hex_escape_string = input("请输入包含 \\x 转义序列的字符串: ")

    # 解码并输出结果
    utf8_string = hex_escape_string_to_utf8(hex_escape_string)
    print("解码后的字符串:")
    print(utf8_string)


# 程序入口
if __name__ == "__main__":
    main()