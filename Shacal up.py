import hmac
import hashlib
from binascii import hexlify, unhexlify
import os

def cmac(key, data):
    """
    使用HMAC和SHA-256算法模拟CMAC。
    """
    # 初始化HMAC
    mac = hmac.new(key, digestmod=hashlib.sha256)
    # 更新数据
    mac.update(data)
    # 返回十六进制的MAC
    return hexlify(mac.digest()).decode()

# 生成随机密钥（16字节）
key = os.urandom(16)

# 提示用户输入明文
user_input = input("请输入明文（原始字符串）：")
message = user_input.encode('utf-8')

# 进行CMAC编码
encoded_mac = cmac(key, message)

print("CMAC编码后的结果:", encoded_mac)
print("使用的密钥（十六进制）:", hexlify(key).decode())