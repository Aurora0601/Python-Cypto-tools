def convert_to_base(number, base):
    """将十进制数字转换为指定进制"""                 #进制转换
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


def convert_any_base_to_any_base(number_str, source_base, target_base):
    """将任意进制的数字转换为任意进制"""
    # 首先将源进制的数字转换为十进制
    decimal_number = convert_from_base(number_str, source_base)
    if decimal_number == "无效的输入":
        return "无效的输入"

    # 然后将十进制数字转换为目标进制
    return convert_to_base(decimal_number, target_base)


# 主函数
if __name__ == "__main__":
    print("进制转换工具")
    print("功能：任意进制转换为任意进制")

    source_base = int(input("请输入源进制数字（2-36）："))
    number_str = input("请输入源进制的数字：")
    target_base = int(input("请输入目标进制（2-36）："))

    result = convert_any_base_to_any_base(number_str, source_base, target_base)
    print(f"{number_str}（{source_base}进制）转换为{target_base}进制是：{result}")
