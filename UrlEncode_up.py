from urllib.parse import quote

def url_encode(input_string):
    """
    对输入的字符串进行URL编码。
    """
    encoded_string = quote(input_string, safe='/:')
    return encoded_string

# 提示用户输入明文
user_input = input("请输入明文（原始字符串）：")
encoded_string = url_encode(user_input)

print("编码后的字符串:", encoded_string)
