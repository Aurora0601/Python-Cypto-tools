def simulate_encoding(plain_text):
    # 将明文转换为二进制数据
    binary_data = plain_text.encode('utf-8')

    # 初始化编码后的字符串
    encoded_data = ''

    # 用于存储当前行的编码字符，以便在达到固定长度时换行
    current_line = ''

    # 遍历二进制数据，每次处理3个字节（或数据末尾的剩余字节）
    for i in range(0, len(binary_data), 3):
        # 获取当前3字节（或更少）的数据块
        chunk = binary_data[i:i + 3]

        # 模拟编码过程：将每个字节转换为两个字符的字符串（这里用十六进制表示作为示例）
        # 注意：这不是真实的编码，只是用十六进制作为占位符来模拟编码后的字符串长度
        encoded_chunk = ''.join(f'{byte:02x}' for byte in chunk).ljust(6, ' ')  # 确保每个块占6个字符

        # 将编码后的块添加到当前行
        current_line += encoded_chunk

        # 如果当前行长度达到或超过45个字符，则将其添加到编码后的字符串中，并重置当前行
        if len(current_line) >= 45:
            encoded_data += current_line[:45] + '\n'  # 只取前45个字符并换行
            current_line = current_line[45:]  # 移除已添加到encoded_data的部分

    # 处理剩余的行（如果最后一行不足45个字符）
    if current_line:
        encoded_data += current_line.ljust(45, ' ') + '\n'  # 用空格填充到45个字符并换行
        # 如果不希望最后一行有多余的空格，可以移除它们：
        # encoded_data = encoded_data.rstrip() + '\n'  # 但这样会移除所有行尾的空格和换行符，需要额外处理
        # 或者更简单地，只添加非空部分而不填充空格：
        # if current_line.strip():  # 如果当前行不是空字符串（去除首尾空格后）
        #     encoded_data += current_line + '\n'  # 直接添加，不填充
    else:
        # 如果整个输入为空，则encoded_data将保持为空字符串，不需要额外的换行符
        pass

    # 由于我们可能在最后一行添加了一个额外的换行符，我们需要去除它（如果输入不为空）
    # 但由于上面的逻辑已经确保了只有在非空输入时才会添加换行符，且最后一行可能已经被处理，
    # 所以这里实际上不需要再次去除换行符。但如果我们想要确保没有多余的空行，可以这样做：
    # if encoded_data and encoded_data.endswith('\n'):
    #     encoded_data = encoded_data[:-1]
    # 然而，由于我们在处理每一行时都确保了完整的换行符，且最后一行是通过不同的逻辑处理的，
    # 所以上面的检查可能是多余的。在这个特定的例子中，我们可以省略它。

    # 返回一个模拟编码后的字符串
    return encoded_data.rstrip()  # 去除字符串末尾的所有空格和换行符（如果有的话）


# 输入明文
plain_text = input("请输入明文: ")

# 获取编码后的字符串
encoded_output = simulate_encoding(plain_text)

# 输出编码后的字符串
print("编码后的字符串:")
print(encoded_output)