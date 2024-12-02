import hashlib


def md5_hash(data):
    """
    计算给定数据的MD5哈希值。

    参数:
    data -- 要计算哈希值的数据，可以是字符串或字节类型。

    返回:
    MD5哈希值，十六进制字符串。
    """
    if isinstance(data, str):
        data = data.encode('utf-8')  # 将字符串转换为字节类型
    hash_object = hashlib.md5(data)
    return hash_object.hexdigest()


# 用户输入明文
plaintext = input("请输入明文：")

# 计算MD5哈希值
md5_result = md5_hash(plaintext)

# 显示MD5哈希值
print("MD5哈希值（十六进制）:", md5_result)