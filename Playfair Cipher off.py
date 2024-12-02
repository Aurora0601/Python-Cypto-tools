def create_playfair_matrix(key):
    key = key.upper().replace('J', 'I')
    matrix = []
    used = set()
    for char in key:
        if char not in used:
            matrix.append(char)
            used.add(char)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, len(matrix), 5)]

def preprocess_text(text, key):
    text = text.upper().replace('J', 'I')
    processed_text = ""
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            processed_text += text[i] + 'X'
            i += 1
        else:
            processed_text += text[i]
            if i + 1 < len(text):
                processed_text += text[i + 1]
            else:
                processed_text += 'X'
            i += 2
    return processed_text

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == char:
                return i, j
    return None, None

def encrypt_pair(matrix, a, b):
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)
    if row_a is None or row_b is None or col_a is None or col_b is None:
        raise ValueError(f"字符 '{a}' 或 '{b}' 不在矩阵中")
    if row_a == row_b:
        return matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
    elif col_a == col_b:
        return matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
    else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]

def playfair_encrypt(plaintext, key):
    matrix = create_playfair_matrix(key)
    plaintext = preprocess_text(plaintext, key)
    ciphertext = ""
    i = 0
    while i < len(plaintext) - 1:
        pair = plaintext[i:i+2]
        encrypted_pair = encrypt_pair(matrix, pair[0], pair[1])
        ciphertext += encrypted_pair
        i += 2
    if len(plaintext) % 2 == 1:  # 处理奇数长度的文本
        ciphertext += encrypt_pair(matrix, plaintext[-1], 'X')[0]
    return ciphertext

def encrypt_main():
    key = input("请输入密钥（不超过25个字符，不包含J，大写字母）：")
    plaintext = input("请输入要加密的明文：")
    ciphertext = playfair_encrypt(plaintext, key)
    print("加密后的密文是：", ciphertext)

if __name__ == "__main__":
    encrypt_main()