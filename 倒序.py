def reverse_string(input_str):
    """将输入的字符串倒序"""
    return input_str[::-1]

# 主函数
if __name__ == "__main__":
    user_input = input("请输入一个字符串：")
    reversed_str = reverse_string(user_input)
    print("倒序后的字符串是：", reversed_str)