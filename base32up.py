import base64

def base32_encode(data):
    """将字节数据编码为Base32字符串（带填充字符'='）。"""
    encoded_bytes = base64.b32encode(data)
    encoded_str = encoded_bytes.decode('utf-8').upper()  # 转换为大写
    return encoded_str

def encode_main():
    plaintext = input("请输入明文: ")
    data_bytes = plaintext.encode('utf-8')
    encoded_data = base32_encode(data_bytes)
    print(f"加密后的Base32字符串: {encoded_data}")

if __name__ == "__main__":
    encode_main()