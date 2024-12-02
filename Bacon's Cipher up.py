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

# 加密函数
def bacon_encrypt(plaintext):
    encrypted_text = ''
    for char in plaintext.upper():  # 将文本转换为大写
        if char in BACON_CIPHER:
            encrypted_text += BACON_CIPHER[char]
        else:
            encrypted_text += '?'  # 非字母字符用问号代替
    return encrypted_text

def encrypt_main():
    plaintext = input("请输入要加密的明文：")
    encrypted = bacon_encrypt(plaintext)
    print("加密后的密文是：", encrypted)

if __name__ == "__main__":
    encrypt_main()