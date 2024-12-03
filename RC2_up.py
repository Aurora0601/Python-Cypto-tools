from Crypto.Cipher import ARC2
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from binascii import hexlify

def rc2_encrypt(key, plaintext):
    """
    使用RC2算法对明文进行加密。
    """
    # 创建RC2加密对象，使用ECB模式
    cipher = ARC2.new(key, ARC2.MODE_ECB)
    # 对明文进行填充，然后加密
    padded_plaintext = pad(plaintext.encode('utf-8'), ARC2.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    # 返回加密后的密文的十六进制表示
    return hexlify(ciphertext).decode('utf-8')

# 生成随机密钥（16字节）
key = get_random_bytes(16)

# 提示用户输入明文
plaintext = input("请输入明文（原始字符串）：")

# 进行RC2加密
ciphertext_hex = rc2_encrypt(key, plaintext)

print("加密后的密文（十六进制）:", ciphertext_hex)
print("使用的密钥（十六进制）:", hexlify(key).decode())
