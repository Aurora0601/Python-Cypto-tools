import string

def repeat_key(key, text):
    """重复密钥直到它与文本长度相同"""
    return (key * (len(text) // len(key))) + key[:len(text) % len(key)]
#维吉尼亚加密
def vigenere_encrypt(text, key):
    """加密函数"""
    key = repeat_key(key, text).upper()
    text = text.upper()
    encrypted_text = ''
    for i in range(len(text)):
        if text[i] in string.ascii_uppercase:
            encrypted_text += chr((ord(text[i]) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        else:
            encrypted_text += text[i]
    return encrypted_text

def main():
    secret_key = input("请输入密钥（只包含字母）：")
    plain_text = input("请输入明文：")
    cipher_text = vigenere_encrypt(plain_text, secret_key)
    print(f'加密后得到的密文是：{cipher_text}')

if __name__ == '__main__':
    main()