from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

# DES解密函数
def des_decrypt(ciphertext, key):
    """
    使用DES算法解密密文。

    参数:
    ciphertext -- 要解密的密文，必须是字节类型。
    key       -- DES解密使用的密钥，长度为8字节。

    返回:
    解密后的明文，字节类型。
    """
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    unpadded_text = unpad(decrypted, DES.block_size)
    return unpadded_text

def decrypt_main():
    # 用户输入密文和密钥
    ciphertext_hex = input("请输入要解密的密文（十六进制）：")
    key_hex = input("请输入密钥（十六进制）：")

    # 将十六进制字符串转换为字节类型
    ciphertext = bytes.fromhex(ciphertext_hex)
    key = bytes.fromhex(key_hex)

    # 解密密文
    decrypted = des_decrypt(ciphertext, key)

    # 显示解密后的明文
    print("解密后的明文:", decrypted.decode('utf-8'))

if __name__ == "__main__":
    decrypt_main()