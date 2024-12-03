def hex_decode(input_string):
    """
    将输入的十六进制编码的字符串进行解码。
    """
    try:
        # 将十六进制字符串转换回字节
        decoded_bytes = bytes.fromhex(input_string)
        # 将字节转换回字符串
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string
    except ValueError as e:
        print("解码失败：", str(e))
        return None

# 提示用户输入十六进制编码后的字符串
encoded_input = input("请输入十六进制编码后的字符串：")
decoded_string = hex_decode(encoded_input)

if decoded_string:
    print("解码后的明文字符串:", decoded_string)
