def hex_encode(input_string):
    """
    将输入的字符串进行十六进制编码。
    """
    # 将字符串转换为字节，然后进行十六进制编码
    encoded_bytes = input_string.encode('utf-8')
    # 将字节转换为十六进制字符串
    encoded_string = encoded_bytes.hex()
    return encoded_string

# 提示用户输入明文
user_input = input("请输入明文（原始字符串）：")
encoded_string = hex_encode(user_input)

print("十六进制编码后的字符串:", encoded_string)
