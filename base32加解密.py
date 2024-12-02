import base64


def base32_encode(data):
    """将字节数据编码为Base32字符串（带填充字符'='）。"""
    encoded_bytes = base64.b32encode(data)
    encoded_str = encoded_bytes.decode('utf-8').upper()  # 转换为大写
    return encoded_str


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


def main():
    print("请选择操作:")
    print("1. 加密 (Encode)")
    print("2. 解密 (Decode)")
    choice = input("输入1或2: ")

    if choice == '1':
        # 输入明文并转换为字节数据
        plaintext = input("请输入明文: ")
        data_bytes = plaintext.encode('utf-8')

        # 加密（编码）
        encoded_data = base32_encode(data_bytes)
        print(f"加密后的Base32字符串: {encoded_data}")

    elif choice == '2':
        # 输入Base32编码的字符串
        encoded_input = input("请输入Base32编码的字符串: ")

        # 解密（解码）
        decoded_data = base32_decode(encoded_input)
        if decoded_data:
            print(f"解密后的明文: {decoded_data.decode('utf-8')}")

    else:
        print("无效的选择，请输入1或2。")


if __name__ == "__main__":
    main()