def zuchongzhi_encrypt(text, shift1, shift2):         #祖冲之密码加密
    result = []
    for i, char in enumerate(text):
        if char.isalpha():  # 检查字符是否是字母
            # 确定使用哪个移位值
            shift = shift1 if i % 2 == 0 else shift2
            # 确定字母是大写还是小写
            is_upper = char.isupper()
            # 找到字母在字母表中的位置（0-25）
            base = ord('A') if is_upper else ord('a')
            # 计算新字母的位置并转换为字符
            new_char = chr((ord(char) - base + shift) % 26 + base)
            # 保持字母的大小写不变
            if not is_upper:
                new_char = new_char.lower()
            result.append(new_char)
        else:
            # 非字母字符保持不变
            result.append(char)
    return ''.join(result)


# 主程序
if __name__ == "__main__":
    # 获取用户输入的明文
    plaintext = input("请输入要加密的明文：")

    # 获取用户输入的移位值
    try:
        shift1 = int(input("请输入偶数位置字母的移位值："))
        shift2 = int(input("请输入奇数位置字母的移位值："))
    except ValueError:
        print("移位值必须是整数。")
        exit(1)

    # 加密明文
    encrypted_text = zuchongzhi_encrypt(plaintext, shift1, shift2)
    print(f"加密结果: {encrypted_text}")
    # 可以选择将加密结果保存到文件或其他地方
    # with open("encrypted.txt", "w") as f:
    #     f.write(encrypted_text)