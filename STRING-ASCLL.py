def string_to_ascii(input_string):
    """将字符串转换为ASCII码列表"""
    return [ord(char) for char in input_string]
#字符串转ASCLL码
def convert_string_to_ascii_list():
    # 提示用户输入字符串
    input_string = input("请输入字符串: ")
    # 转换为ASCII码列表
    result_ascii_list = string_to_ascii(input_string)
    print("转换后的ASCII码列表:", result_ascii_list)

if __name__ == "__main__":
    convert_string_to_ascii_list()