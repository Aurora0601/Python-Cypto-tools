import numpy as np
#仿射密码加密
# 将字母转换为数字（A=0, B=1, ..., Z=25）
def letter_to_num(letter):
    return ord(letter.upper()) - ord('A')

# 将数字转换为字母（0=A, 1=B, ..., 25=Z）
def num_to_letter(num):
    return chr(num + ord('A'))

# 加密函数
def encrypt_affine(plaintext, a, b):
    mod = 26
    num_plaintext = [letter_to_num(char) for char in plaintext]
    encrypted_num = [(a * num + b) % mod for num in num_plaintext]
    encrypted_text = ''.join(num_to_letter(num) for num in encrypted_num)
    return encrypted_text

def encrypt_main():
    a = 5  # 密钥a，必须与26互质
    b = 8  # 密钥b
    plaintext = input("请输入要加密的明文（只包含字母A-Z）：").upper()
    ciphertext = encrypt_affine(plaintext, a, b)
    print("加密后的密文是：", ciphertext)

if __name__ == "__main__":
    encrypt_main()