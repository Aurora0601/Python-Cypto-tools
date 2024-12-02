import numpy as np
#仿射密码解密
# 扩展欧几里得算法计算模逆
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  # 如果没有找到模逆，返回None

# 将字母转换为数字（A=0, B=1, ..., Z=25）
def letter_to_num(letter):
    return ord(letter.upper()) - ord('A')

# 将数字转换为字母（0=A, 1=B, ..., 25=Z）
def num_to_letter(num):
    return chr(num + ord('A'))

# 解密函数
def decrypt_affine(ciphertext, a, b):
    mod = 26
    a_inv = mod_inverse(a, mod)
    if a_inv is None:
        raise ValueError("密钥a没有模26的乘法逆元")
    num_ciphertext = [letter_to_num(char) for char in ciphertext]
    decrypted_num = [(a_inv * (num - b)) % mod for num in num_ciphertext]
    decrypted_text = ''.join(num_to_letter(num) for num in decrypted_num)
    return decrypted_text

def decrypt_main():
    a = 5  # 密钥a，必须与26互质
    b = 8  # 密钥b
    ciphertext = input("请输入要解密的密文（只包含字母A-Z）：").upper()
    plaintext = decrypt_affine(ciphertext, a, b)
    print("解密后的明文是：", plaintext)

if __name__ == "__main__":
    decrypt_main()