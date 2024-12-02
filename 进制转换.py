def convert_to_base(number, base):
    """将十进制数字转换为指定进制"""
    if base < 2 or base > 36:
        return "不支持的进制数，请输入2-36之间的数"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while number > 0:
        result = digits[number % base] + result
        number //= base

    return result if result else "0"


def convert_from_base(number_str, base):
    """将指定进制的数字转换为十进制"""
    try:
        return int(number_str, base)
    except ValueError:
        return "无效的输入"


# 主函数
if __name__ == "__main__":
    print("进制转换工具")
    print("1. 十进制转其他进制")
    print("2. 其他进制转十进制")

    choice = input("请选择转换类型（1或2）：")

    if choice == "1":
        decimal_number = int(input("请输入十进制数字："))
        target_base = int(input("请输入目标进制（2-36）："))
        result = convert_to_base(decimal_number, target_base)
        print(f"{decimal_number}（十进制）转换为{target_base}进制是：{result}")
    elif choice == "2":
        number_str = input("请输入其他进制的数字：")
        number_base = int(input("请输入该数字的进制（2-36）："))
        result = convert_from_base(number_str, number_base)
        print(f"{number_str}（{number_base}进制）转换为十进制是：{result}")
    else:
        print("无效的选择")