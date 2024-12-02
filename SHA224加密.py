import hashlib


def sha224_hash(input_string):
    """对输入的字符串进行SHA-224哈希"""
    # 创建一个sha224哈希对象（注意：在Python的hashlib中，sha224实际上是基于sha256的）
    sha224 = hashlib.sha224()

    # 更新哈希对象的内容，必须编码为字节
    sha224.update(input_string.encode('utf-8'))

    # 获取十六进制格式的哈希值字符串
    hex_digest = sha224.hexdigest()

    return hex_digest


def main():
    # 提示用户输入要哈希的字符串
    input_string = input("请输入要哈希的字符串: ")

    # 对字符串进行SHA-224哈希
    hashed_string = sha224_hash(input_string)

    # 输出哈希后的字符串
    print("SHA-224哈希后的字符串:", hashed_string)


if __name__ == "__main__":
    main()