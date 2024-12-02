def binary_decode(input_string):
    """
    将输入的二进制编码的字符串进行解码。
    """
    # 将二进制字符串转换回原始字符串
    bytes_array = [int(input_string[i:i+8], 2) for i in range(0, len(input_string), 8)]
    decoded_string = ''.join(chr(byte) for byte in bytes_array)
    return decoded_string

# 提示用户输入二进制编码后的字符串
encoded_input = input("请输入二进制编码后的字符串：")
decoded_string = binary_decode(encoded_input)

print("解码后的明文字符串:", decoded_string)