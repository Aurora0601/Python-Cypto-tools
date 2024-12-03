import hmac
import hashlib
from binascii import hexlify, unhexlify
import os

def calculate_hmac(key, message):
    """
    使用HMAC和SHA-256算法计算消息的MAC。
    """
    # 初始化HMAC
    mac = hmac.new(key, digestmod=hashlib.sha256)
    # 更新数据
    mac.update(message)
    # 返回十六进制的MAC
    return hexlify(mac.digest()).decode()

# 生成随机密钥（16字节）
key = os.urandom(16)
key_hex = hexlify(key).decode()  # 将密钥转换为十六进制字符串以便显示或存储

# 提示用户输入明文
user_input = input("请输入明文（原始字符串）：")
message = user_input.encode('utf-8')

# 计算MAC
calculated_mac = calculate_hmac(key, message)
print("计算出的MAC（十六进制）：", calculated_mac)

# 假设我们要验证这个MAC，我们可以重新输入明文（在实际应用中，这通常是从其他地方获取的）
# 并使用一个之前存储或接收的密钥和MAC来进行验证

# 模拟重新输入明文（在实际应用中，这应该是从其他地方获取的相同明文）
user_input_for_verification = input("请输入用于验证的明文（应该与之前的明文相同）：")
message_for_verification = user_input_for_verification.encode('utf-8')

# 假设我们有一个之前计算并存储的MAC（在这个例子中，我们实际上刚刚计算过它）
# 但在实际应用中，这通常是从其他地方获取的
input_mac_hex = input("请输入要验证的MAC（十六进制字符串）：")  # 在实际应用中，这应该是之前存储或接收的MAC

# 将输入的MAC从十六进制字符串转换为字节串
input_mac = unhexlify(input_mac_hex.encode('utf-8'))

# 重新计算MAC以进行验证
calculated_mac_for_verification = calculate_hmac(key, message_for_verification)
calculated_mac_bytes_for_verification = unhexlify(calculated_mac_for_verification.encode('utf-8'))

# 使用 hmac.compare_digest 安全地比较两个MAC
if hmac.compare_digest(calculated_mac_bytes_for_verification, input_mac):
    print("MAC验证成功，数据未被篡改。")
else:
    print("MAC验证失败，数据可能已被篡改。")

# 输出密钥的十六进制表示（仅用于演示或调试，不要在生产环境中这样做）
print("使用的密钥（十六进制）：", key_hex)
