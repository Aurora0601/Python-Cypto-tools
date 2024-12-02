from string import ascii_lowercase, ascii_uppercase


# 埃特巴什码加密和解密函数
def atbash_cipher(text):
    # 创建字母表和其反向字母表的映射
    lower_map = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])
    upper_map = str.maketrans(ascii_uppercase, ascii_uppercase[::-1])

    # 转换文本
    text = text.translate(lower_map).translate(upper_map)

    return text


# 主函数
if __name__ == "__main__":
    # 用户输入明文或密文
    input_text = input("请输入要加密/解密的文本：")
    # 加密/解密
    output_text = atbash_cipher(input_text)

    # 输出结果
    print("埃特巴什码加解密结果：", output_text)