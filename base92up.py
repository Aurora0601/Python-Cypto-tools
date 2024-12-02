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

def encode_main():
    plaintext = input("请输入明文: ")
    encoded_text = base92_encode(int.from_bytes(plaintext.encode(), byteorder='big'))
    print("加密后的文本: ", encoded_text)

if __name__ == "__main__":
    encode_main()