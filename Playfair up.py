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
        # 根据当前行决定下一步的方向
        if current_row == 0:
            going_down = True
        elif current_row == num_rows - 1:
            going_down = False

        current_row += 1 if going_down else -1

    # 将所有行连接在一起形成密文
    return ''.join(rows)


if __name__ == "__main__":
    plaintext = input("请输入明文：")
    num_rows = int(input("请输入行数："))
    encrypted = encrypt_zigzag(plaintext, num_rows)
    print("加密后的密文:", encrypted)