import base64

def base32_decode(encoded):
    """将Base32字符串解码为字节数据。"""
    encoded_bytes = encoded.encode('utf-8')
    try:
        decoded_bytes = base64.b32decode(encoded_bytes)
    except base64.binascii.Error:
        # 处理解码错误，可能是因为填充字符不正确或字符串包含无效字符
        print("解码错误：无效的Base32编码字符串")
        return None
    return decoded_bytes

def decode_main():
    encoded_input = input("请输入Base32编码的字符串: ")
    decoded_data = base32_decode(encoded_input)
    if decoded_data:
        print(f"解密后的明文: {decoded_data.decode('utf-8')}")

if __name__ == "__main__":
    decode_main()