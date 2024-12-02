def create_polybius_square():
    """创建 Polybius 方阵"""
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' 被省略
    square = {}

    for i, letter in enumerate(alphabet):
        row = i // 5 + 1
        col = i % 5 + 1
        square[letter] = (row, col)

    return square


def encrypt_polybius(plaintext):
    """使用 Polybius 密码加密明文"""
    square = create_polybius_square()
    ciphertext = []
    plaintext = plaintext.upper().replace("J", "I")  # 将 J 视作 I

    for char in plaintext:
        if char in square:
            row, col = square[char]
            ciphertext.append(f"{row}{col}")  # 无空格连接数字

    return ' '.join(ciphertext)


def decrypt_polybius(ciphertext):
    """使用 Polybius 密码解密密文"""
    square = create_polybius_square()
    reverse_square = {v: k for k, v in square.items()}
    plaintext = []

    # 将输入的密文分成数字对
    numbers = ciphertext.split()

    for num in numbers:
        row = int(num[0])
        col = int(num[1])
        plaintext.append(reverse_square[(row, col)])

    return ''.join(plaintext)


# 示例使用
if __name__ == "__main__":
    plaintext = input("请输入明文：")
    encrypted = encrypt_polybius(plaintext)
    print("加密后的密文:", encrypted)

    ciphertext = input("请输入密文进行解密：")
    decrypted = decrypt_polybius(ciphertext)
    print("解密后的明文:", decrypted)
