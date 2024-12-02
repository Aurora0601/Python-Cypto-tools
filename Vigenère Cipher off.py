import string

def repeat_key(key, text):
    """重复密钥直到它与文本长度相同"""
    return (key * (len(text) // len(key))) + key[:len(text) % len(key)]
#维吉尼亚解密
def vigenere_decrypt(text, key):
    """解密函数"""
    key = repeat_key(key, text).upper()
    text = text.upper()
    decrypted_text = ''
    for i in range(len(text)):
        if text[i] in string.ascii_uppercase:
            decrypted_text += chr((ord(text[i]) - ord(key[i]) + 26) % 26 + ord('A'))
        else:
            decrypted_text += text[i]
    return decrypted_text

def main():
    secret_key = input("请输入密钥（只包含字母，与加密时相同）：")
    cipher_text_input = input("请输入密文：")
    plain_text_decrypted = vigenere_decrypt(cipher_text_input, secret_key)
    print(f'解密后得到的明文是：{plain_text_decrypted}')

if __name__ == '__main__':
    main()