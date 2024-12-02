from Crypto.Cipher import Blowfish
from Crypto.Hash import CMAC
from binascii import hexlify, unhexlify
import os

def blowfish_cmac_encode(key, message):
    """
    使用Blowfish-CMAC算法对消息进行编码。
    """
    # 创建一个新的CMAC对象
    cmac = CMAC.new(key, ciphermod=Blowfish)
    # 更新消息
    cmac.update(message)
    # 计算并返回CMAC
    return hexlify(cmac.digest()).decode()

# 生成随机密钥（16字节）
key = os.urandom(16)

# 提示用户输入明文
user_input = input("请输入明文（原始字符串）：")
message = user_input.encode('utf-8')

# 进行Blowfish-CMAC编码
encoded_mac = blowfish_cmac_encode(key, message)

print("Blowfish-CMAC编码后的结果:", encoded_mac)
print("使用的密钥（十六进制）:", hexlify(key).decode())