from urllib.parse import unquote

def url_decode(input_string):
    """
    对输入的URL编码的字符串进行解码。
    """
    decoded_string = unquote(input_string)
    return decoded_string

# 提示用户输入编码后的字符串
encoded_input = input("请输入编码后的字符串：")
decoded_string = url_decode(encoded_input)

print("解码后的字符串:", decoded_string)