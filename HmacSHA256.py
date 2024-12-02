import hmac
import hashlib


def hmac_sha256(key, message):
    """对输入的密钥和消息进行HMAC-SHA256加密"""
    # 创建一个新的hmac对象，指定使用sha256作为哈希函数
    hmac_obj = hmac.new(key.encode('utf-8'), digestmod=hashlib.sha256)

    # 更新hmac对象的内容，消息也必须编码为字节
    hmac_obj.update(message.encode('utf-8'))

    # 获取十六进制格式的HMAC值字符串
    hex_digest = hmac_obj.hexdigest()

    return hex_digest


def main():
    # 提示用户输入密钥
    key = input("请输入密钥: ")

    # 提示用户输入要加密的消息
    message = input("请输入要加密的消息: ")

    # 对密钥和消息进行HMAC-SHA256加密
    encrypted_message = hmac_sha256(key, message)

    # 输出加密后的消息（HMAC值）
    print("HMAC-SHA256加密后的消息:", encrypted_message)


if __name__ == "__main__":
    main()