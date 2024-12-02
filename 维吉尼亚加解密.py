import string

def repeat_key(key, text):
    """重复密钥直到它与文本长度相同"""
    return (key * (len(text) // len(key))) + key[:len(text) % len(key)]

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

if __name__ == '__main__':
    secret_key = input("请输入密钥（只包含字母）：")
    operation = input("请选择操作（加密请输入'e'，解密请输入'd'）：")

    if operation.lower() == 'e':
        plain_text = input("请输入明文：")
        cipher_text = vigenere_encrypt(plain_text, secret_key)
        print(f'加密后得到的密文是：{cipher_text}')
    elif operation.lower() == 'd':
        cipher_text_input = input("请输入密文：")
        plain_text_decrypted = vigenere_decrypt(cipher_text_input, secret_key)
        print(f'解密后得到的明文是：{plain_text_decrypted}')
    else:
        print("无效的操作选项。请重新运行程序并选择'e'进行加密或'd'进行解密。")