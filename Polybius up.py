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

def encrypt_main():
    plaintext = input("请输入明文：")
    encrypted = encrypt_polybius(plaintext)
    print("加密后的密文:", encrypted)

if __name__ == "__main__":
    encrypt_main()