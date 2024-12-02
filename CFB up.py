from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from binascii import hexlify

def cfb_encrypt(key, iv, plaintext):
    """
    使用AES-CFB算法对明文进行加密。
    """
    # 创建AES加密对象，使用CFB模式
    cipher = AES.new(key, AES.MODE_CFB, iv)
    # 对明文进行填充，然后加密
    padded_plaintext = pad(plaintext.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    # 返回加密后的密文的十六进制表示
    return hexlify(ciphertext).decode('utf-8')

# 用户输入明文
plaintext = input("请输入明文（原始字符串）：")

# 生成随机密钥和IV（都是16字节）
key = get_random_bytes(16)
iv = get_random_bytes(AES.block_size)

# 进行CFB加密
ciphertext_hex = cfb_encrypt(key, iv, plaintext)

print("加密后的密文（十六进制）:", ciphertext_hex)
print("使用的密钥（十六进制）:", hexlify(key).decode())
print("使用的IV（十六进制）:", hexlify(iv).decode())