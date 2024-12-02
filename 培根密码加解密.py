# 培根密码加密字典
BACON_CIPHER = {
    'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB',
    'E': 'AABAA', 'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB',
    'I': 'ABAAA', 'J': 'ABAAB', 'K': 'ABABA', 'L': 'ABABB',
    'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA', 'P': 'ABBBB',
    'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB',
    'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB',
    'Y': 'BBAAA', 'Z': 'BBAAB'
}

# 培根密码解密字典
bacon_dict = {v: k for k, v in BACON_CIPHER.items()}

# 加密函数
def bacon_encrypt(plaintext):
    encrypted_text = ''
    for char in plaintext.upper():  # 将文本转换为大写
        if char in BACON_CIPHER:
            encrypted_text += BACON_CIPHER[char]
        else:
            encrypted_text += '?'  # 非字母字符用问号代替
    return encrypted_text

# 解密函数
def decrypt_bacon(ciphertext):
    plaintext = ''
    # 将密文按照5个字符分组
    for i in range(0, len(ciphertext), 5):
        substring = ciphertext[i:i + 5]
        # 查找每个分组对应的字母
        if substring in bacon_dict:
            plaintext += bacon_dict[substring]
        else:
            plaintext += '?'  # 非有效编码用问号代替
    return plaintext

# 主函数
if __name__ == "__main__":
    choice = input("请选择操作（加密请输入'E'，解密请输入'D'）：").upper()
    if choice == 'E':
        plaintext = input("请输入要加密的明文：")
        encrypted = bacon_encrypt(plaintext)
        print("加密后的密文是：", encrypted)
    elif choice == 'D':
        ciphertext = input("请输入培根密码加密的密文：")
        decrypted_text = decrypt_bacon(ciphertext)
        print("解密后的明文是：", decrypted_text)
    else:
        print("无效的操作选项。请重新运行程序并选择'E'进行加密或'D'进行解密。")