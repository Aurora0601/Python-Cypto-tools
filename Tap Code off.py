def create_tap_code_dict():
    """创建敲击密码字典"""
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 去掉字母 C
    tap_code_dict = {}
    for i, letter in enumerate(alphabet):
        row = i // 5 + 1
        col = i % 5 + 1
        tap_code_dict[letter] = (row, col)
    return tap_code_dict


def decrypt_tap_code(ciphertext):
    """将敲击密码解密为明文"""
    tap_code_dict = create_tap_code_dict()
    reverse_tap_code_dict = {v: k for k, v in tap_code_dict.items()}
    plaintext = []

    # 将输入的敲击密码分成数字对
    numbers = list(map(int, ciphertext.split()))

    for i in range(0, len(numbers), 2):
        row = numbers[i]
        col = numbers[i + 1]
        plaintext.append(reverse_tap_code_dict[(row, col)])

    return ''.join(plaintext)


if __name__ == "__main__":
    ciphertext = input("请输入敲击密码进行解密：")
    decrypted = decrypt_tap_code(ciphertext)
    print("解密后的明文:", decrypted)