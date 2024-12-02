import hashlib


def md5_encrypt(input_string):
    """对输入的字符串进行MD5加密"""
    # 创建一个md5哈希对象
    md5_hash = hashlib.md5()

    # 更新哈希对象的内容，必须编码为字节
    md5_hash.update(input_string.encode('utf-8'))

    # 获取十六进制格式的哈希值字符串
    hex_digest = md5_hash.hexdigest()

    return hex_digest


def main():
    # 提示用户输入要加密的字符串
    input_string = input("请输入要加密的字符串: ")

    # 对字符串进行MD5加密
    encrypted_string = md5_encrypt(input_string)

    # 输出加密后的字符串
    print("MD5加密后的字符串:", encrypted_string)


if __name__ == "__main__":
    main()