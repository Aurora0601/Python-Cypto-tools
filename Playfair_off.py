def decrypt_zigzag(ciphertext, num_rows):
    """使用曲路密码解密密文"""
    if num_rows <= 1:
        return ciphertext

    # 计算每行的字符数（长度）
    n = len(ciphertext)
    row_lengths = [0] * num_rows
    # 临时变量，用于模拟加密过程以计算每行长度
    current_row = 0
    going_down = False

    # 计算每行应该有多少个字符
    for i in range(n):
        row_lengths[current_row] += 1
        # 根据当前行决定下一步的方向
        if current_row == 0:
            going_down = True
        elif current_row == num_rows - 1:
            going_down = False

        current_row += 1 if going_down else -1

    # 根据计算出的长度从密文中分割出每行的内容
    index = 0
    rows = [''] * num_rows
    for i in range(num_rows):
        rows[i] = ciphertext[index:index + row_lengths[i]]
        index += row_lengths[i]

    # 按照曲路排列重建明文
    result = []
    current_row = 0
    going_down = False
    for _ in range(n):  # 使用 _ 因为我们不需要循环变量，只关心循环次数
        result.append(rows[current_row][0])
        rows[current_row] = rows[current_row][1:]  # 移除已添加的字符
        # 根据当前行决定下一步的方向
        if current_row == 0:
            going_down = True
        elif current_row == num_rows - 1:
            going_down = False

        current_row += 1 if going_down else -1

    return ''.join(result)


if __name__ == "__main__":
    ciphertext = input("请输入密文进行解密：")
    num_rows = int(input("请输入行数（与加密时相同）："))
    decrypted = decrypt_zigzag(ciphertext, num_rows)
    print("解密后的明文:", decrypted)
