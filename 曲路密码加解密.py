def encrypt_zigzag(plaintext, num_rows):
    """使用曲路密码加密明文"""
    if num_rows <= 1:
        return plaintext

    # 创建一个列表来存储每行的字符
    rows = [''] * num_rows
    current_row = 0
    going_down = False

    # 遍历每个字符，将其放入相应的行中
    for char in plaintext:
        rows[current_row] += char
        if current_row == 0:
            going_down = True
        elif current_row == num_rows - 1:
            going_down = False

        current_row += 1 if going_down else -1

    # 将所有行连接在一起
    return ''.join(rows)


def decrypt_zigzag(ciphertext, num_rows):
    """使用曲路密码解密密文"""
    if num_rows <= 1:
        return ciphertext

    # 计算每行的字符数
    n = len(ciphertext)
    rows = [''] * num_rows
    current_row = 0
    going_down = False
    row_lengths = [0] * num_rows

    # 计算每行应该有多少个字符
    for i in range(n):
        row_lengths[current_row] += 1
        if current_row == 0:
            going_down = True
        elif current_row == num_rows - 1:
            going_down = False

        current_row += 1 if going_down else -1

    # 填充行
    index = 0
    for i in range(num_rows):
        rows[i] = ciphertext[index:index + row_lengths[i]]
        index += row_lengths[i]

    # 按照曲路排列重建明文
    result = []
    current_row = 0
    going_down = False
    for i in range(n):
        result.append(rows[current_row][0])
        rows[current_row] = rows[current_row][1:]  # 移除已添加的字符
        if current_row == 0:
            going_down = True
        elif current_row == num_rows - 1:
            going_down = False

        current_row += 1 if going_down else -1

    return ''.join(result)


# 示例使用
if __name__ == "__main__":
    plaintext = input("请输入明文：")
    num_rows = int(input("请输入行数："))
    encrypted = encrypt_zigzag(plaintext, num_rows)
    print("加密后的密文:", encrypted)

    ciphertext = input("请输入密文进行解密：")
    decrypted = decrypt_zigzag(ciphertext, num_rows)
    print("解密后的明文:", decrypted)
