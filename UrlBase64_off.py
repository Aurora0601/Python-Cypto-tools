import base64

def url_base64_decode(input_string):
    """
    将输入的URL安全的Base64编码的字符串进行解码。
    """
    try:
        # 将字符串转换为字节，然后进行Base64解码
        decoded_bytes = base64.urlsafe_b64decode(input_string)
        # 将字节转换回字符串
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string
    except Exception as e:
        print("解码失败：", str(e))
        return None

# 提示用户输入URL安全的Base64编码后的字符串
encoded_input = input("请输入URL安全的Base64编码后的字符串：")
decoded_string = url_base64_decode(encoded_input)

if decoded_string:
    print("解码后的明文字符串:", decoded_string)
