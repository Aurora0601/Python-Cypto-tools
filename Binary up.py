def binary_encode(input_string):
    """
    将输入的字符串进行二进制编码。
    """
    # 将每个字符转换为其二进制表示
    encoded_bytes = ''.join(format(ord(char), '08b') for char in input_string)
    return encoded_bytes

# 提示用户输入明文
user_input = input("请输入明文（原始字符串）：")
encoded_string = binary_encode(user_input)

print("二进制编码后的字符串:", encoded_string)