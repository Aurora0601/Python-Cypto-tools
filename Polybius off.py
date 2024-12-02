def create_polybius_square():
    """创建 Polybius 方阵"""
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' 被省略
    square = {}

    for i, letter in enumerate(alphabet):
        row = i // 5 + 1
        col = i % 5 + 1
        square[letter] = (row, col)

    return square

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

def decrypt_main():
    ciphertext = input("请输入密文进行解密：")
    decrypted = decrypt_polybius(ciphertext)
    print("解密后的明文:", decrypted)

if __name__ == "__main__":
    decrypt_main()