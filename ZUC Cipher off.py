def zuchongzhi_decrypt(cipher, shift1, shift2):
    # 解密是加密的逆过程，将移位值变为负数（相当于向左移动）
    return zuchongzhi_encrypt(cipher, -shift1, -shift2)
#祖冲之密码解密

# 注意：这里的zuchongzhi_encrypt函数与encrypt.py中的相同，但为了保持脚本的独立性，
# 你需要在decrypt.py中也定义它，或者将其放在一个共享的模块中并导入。
# 但为了简化示例，这里我们直接复制了函数定义。
# 在实际应用中，应避免代码重复，应通过导入模块来共享函数。

def zuchongzhi_encrypt(text, shift1, shift2):
    result = []
    for i, char in enumerate(text):
        if char.isalpha():
            shift = shift1 if i % 2 == 0 else shift2
            is_upper = char.isupper()
            base = ord('A') if is_upper else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            if not is_upper:
                new_char = new_char.lower()
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)


# 主程序
if __name__ == "__main__":
    # 获取用户输入的密文
    ciphertext = input("请输入要解密的密文：")

    # 获取用户输入的移位值（这些值必须与加密时使用的值相同）
    try:
        shift1 = int(input("请输入加密时偶数位置字母的移位值："))
        shift2 = int(input("请输入加密时奇数位置字母的移位值："))
    except ValueError:
        print("移位值必须是整数。")
        exit(1)

    # 解密密文
    decrypted_text = zuchongzhi_decrypt(ciphertext, shift1, shift2)
    print(f"解密结果: {decrypted_text}")
    # 可以选择将解密结果保存到文件或其他地方
    # with open("decrypted.txt", "w") as f:
    #     f.write(decrypted_text)