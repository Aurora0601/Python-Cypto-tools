import string

BASE92_CHARS = string.ascii_letters + string.digits + ".,:;+=?!@#$%^&*()[]{}<>/|\\"

def base92_decode(encoded_str):
    num = 0
    for char in encoded_str:
        num = num * 92 + BASE92_CHARS.index(char)
    return num.to_bytes((num.bit_length() + 7) // 8, byteorder='big').decode()

def decode_main():
    encoded_text = input("请输入要解密的文本: ")
    decoded_str = base92_decode(encoded_text)
    print("解密后的文本: ", decoded_str)

if __name__ == "__main__":
    decode_main()