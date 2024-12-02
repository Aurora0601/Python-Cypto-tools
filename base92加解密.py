import string

BASE92_CHARS = string.ascii_letters + string.digits + ".,:;+=?!@#$%^&*()[]{}<>/|\\"


def base92_encode(num):
    if num == 0:
        return BASE92_CHARS[0]
    result = ""
    while num > 0:
        num, remainder = divmod(num, 92)
        result += BASE92_CHARS[remainder]
    return result[::-1]


def base92_decode(encoded_str):
    num = 0
    for char in encoded_str:
        num = num * 92 + BASE92_CHARS.index(char)
    return num


def main():
    print("请选择操作：")
    print("1. 加密")
    print("2. 解密")
    choice = input("请输入你的选择（1或2）：")

    if choice == "1":
        plaintext = input("请输入明文: ")
        encoded_text = base92_encode(int.from_bytes(plaintext.encode(), byteorder='big'))
        print("加密后的文本: ", encoded_text)
    elif choice == "2":
        encoded_text = input("请输入要解密的文本: ")
        decoded_text = base92_decode(encoded_text)
        decoded_str = decoded_text.to_bytes((decoded_text.bit_length() + 7) // 8, byteorder='big').decode()
        print("解密后的文本: ", decoded_str)
    else:
        print("无效的选择，请重新输入。")


if __name__ == "__main__":
    main()