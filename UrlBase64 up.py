import base64

def url_base64_encode(input_string):
    """
    将输入的字符串进行URL安全的Base64编码。
    """
    # 将字符串转换为字节，然后进行Base64编码
    encoded_bytes = base64.urlsafe_b64encode(input_string.encode('utf-8'))
    # 将字节转换回字符串
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string

# 提示用户输入明文
user_input = input("请输入明文（原始字符串）：")
encoded_string = url_base64_encode(user_input)

print("URL安全的Base64编码后的字符串:", encoded_string)