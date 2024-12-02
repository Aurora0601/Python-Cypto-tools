def create_tap_code_dict():
    """创建敲击密码字典"""
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 去掉字母 C
    tap_code_dict = {}
    for i, letter in enumerate(alphabet):
        row = i // 5 + 1
        col = i % 5 + 1
        tap_code_dict[letter] = (row, col)
    return tap_code_dict


def encrypt_tap_code(plaintext):
    """加密明文为敲击密码"""
    tap_code_dict = create_tap_code_dict()
    ciphertext = []
    plaintext = plaintext.upper().replace("J", "I")  # 将 J 视作 I

    for char in plaintext:
        if char in tap_code_dict:
            row, col = tap_code_dict[char]
            ciphertext.append(f"{row} {col}")

    return ' '.join(ciphertext)


if __name__ == "__main__":
    plaintext = input("请输入明文：")
    encrypted = encrypt_tap_code(plaintext)
    print("加密后的敲击密码:", encrypted)