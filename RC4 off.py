from Crypto.Cipher import ARC4

def rc4_decrypt(ciphertext, key):
    """
    使用RC4算法解密密文。

    参数:
    ciphertext -- 要解密的密文，必须是字节类型。
    key       -- RC4解密使用的密钥。

    返回:
    解密后的明文，字节类型。
    """
    cipher = ARC4.new(key)
    return cipher.decrypt(ciphertext)

def decrypt_main():
    # 用户输入密文进行解密
    ciphertext_hex = input("请输入要解密的密文（十六进制）：")
    key_hex = input("请输入密钥（十六进制）：")

    # 将十六进制字符串转换为字节类型
    ciphertext = bytes.fromhex(ciphertext_hex)
    key = bytes.fromhex(key_hex)

    # 解密密文
    try:
        decrypted = rc4_decrypt(ciphertext, key)
        print("解密后的明文:", decrypted.decode('utf-8'))
    except Exception as e:
        print("解密失败：", e)

if __name__ == "__main__":
    decrypt_main()