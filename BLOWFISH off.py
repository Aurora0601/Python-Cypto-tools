from Crypto.Cipher import Blowfish
from Crypto.Hash import CMAC
from binascii import unhexlify, hexlify

def blowfish_cmac_decode(key, message, mac_hex):
    """
    使用Blowfish-CMAC算法验证消息。
    """
    # 将十六进制的MAC转换为字节
    mac = unhexlify(mac_hex)
    # 创建一个新的CMAC对象
    cmac = CMAC.new(key, ciphermod=Blowfish)
    # 更新消息
    cmac.update(message)
    # 计算CMAC
    calculated_mac = cmac.digest()
    # 比较计算出的CMAC和提供的CMAC
    return mac == calculated_mac

# 提示用户输入明文
user_input = input("请输入明文（原始字符串）：")
message = user_input.encode('utf-8')

# 用户输入密钥和MAC（这里假设密钥长度适合Blowfish，通常是16字节，MAC是十六进制）
key_input = input("请输入密钥（十六进制）：")
mac_input = input("请输入Blowfish-CMAC编码后的MAC（十六进制）：")

# 检查密钥长度是否为偶数
if len(key_input) % 2 != 0:
    print("密钥长度为奇数，自动在前面添加一个零。")
    key_input = '0' + key_input

try:
    key = unhexlify(key_input)
except (ValueError, binascii.Error) as e:
    print("密钥格式错误：", str(e))
    exit()

mac_hex = mac_input

# 进行Blowfish-CMAC解码（验证）
is_valid = blowfish_cmac_decode(key, message, mac_hex)

print("验证结果:", "有效" if is_valid else "无效")