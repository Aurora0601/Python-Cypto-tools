def encrypt_vigenere(plaintext, key):
    """加密函数，使用费娜姆密码加密明文"""
    ciphertext = []
    plaintext = plaintext.upper()
    key = key.upper()
    length_of_key = len(key)
    for i in range(len(plaintext)):
        key_index = i % length_of_key
        shift = ord(key[key_index]) - ord('A')
        encrypted_char = chr((ord(plaintext[i]) - ord('A') + shift) % 26 + ord('A'))
        ciphertext.append(encrypted_char)
    return ''.join(ciphertext)

def decrypt_vigenere(ciphertext, key):
    """解密函数，使用费娜姆密码解密密文"""
    decrypted_text = []
    ciphertext = ciphertext.upper()
    key = key.upper()
    key_length = len(key)
    for i in range(len(ciphertext)):
        shift = ord(key[i % key_length]) - ord('A')
        decrypted_char = chr((ord(ciphertext[i]) - ord('A') - shift) % 26 + ord('A'))
        decrypted_text.append(decrypted_char)
    return ''.join(decrypted_text)

# 主函数
if __name__ == "__main__":
    key = input("请输入密钥（任意长度，只包含字母A-Z）：")
    choice = input("请选择操作（加密请输入'E'，解密请输入'D'）：").upper()

    if choice == 'E':
        plaintext = input("请输入明文（只包含字母A-Z）：")
        ciphertext = encrypt_vigenere(plaintext, key)
        print("加密后的密文是：", ciphertext)
    elif choice == 'D':
        ciphertext = input("请输入要解密的密文（只包含字母A-Z）：")
        decrypted_text = decrypt_vigenere(ciphertext, key)
        print("解密后的明文是：", decrypted_text)
    else:
        print("无效的选择")