def decrypt_pair(matrix, a, b):
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)
    if row_a is None or row_b is None or col_a is None or col_b is None:
        raise ValueError(f"字符 '{a}' 或 '{b}' 不在矩阵中")
    if row_a == row_b:
        return matrix[row_a][(col_a - 1) % 5] + matrix[row_b][(col_b - 1) % 5]
    elif col_a == col_b:
        return matrix[(row_a - 1) % 5][col_a] + matrix[(row_b - 1) % 5][col_b]
    else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]

def playfair_decrypt(ciphertext, key):
    matrix = create_playfair_matrix(key)
    ciphertext = preprocess_text(ciphertext, key)  # 确保密文也经过预处理
    plaintext = ""
    i = 0
    while i < len(ciphertext) - 1:
        pair = ciphertext[i:i+2]
        decrypted_pair = decrypt_pair(matrix, pair[0], pair[1])
        plaintext += decrypted_pair
        i += 2
    if len(ciphertext) % 2 == 1:  # 处理奇数长度的密文
        plaintext += decrypt_pair(matrix, ciphertext[-1], 'X')[0]
    return plaintext

def decrypt_main():
    key = input("请输入密钥（不超过25个字符，不包含J，大写字母）：")
    ciphertext = input("请输入要解密的密文：")
    plaintext = playfair_decrypt(ciphertext, key)
    print("解密后的明文是：", plaintext)

if __name__ == "__main__":
    decrypt_main()