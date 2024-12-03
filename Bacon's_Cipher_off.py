# 培根密码解密字典
bacon_dict = {v: k for k, v in BACON_CIPHER.items()}

# 解密函数
def decrypt_bacon(ciphertext):
    plaintext = ''
    # 将密文按照5个字符分组
    for i in range(0, len(ciphertext), 5):
        substring = ciphertext[i:i + 5]
        # 查找每个分组对应的字母
        if substring in bacon_dict:
            plaintext += bacon_dict[substring]
        else:
            plaintext += '?'  # 非有效编码用问号代替
    return plaintext

def decrypt_main():
    ciphertext = input("请输入培根密码加密的密文：")
    decrypted_text = decrypt_bacon(ciphertext)
    print("解密后的明文是：", decrypted_text)

if __name__ == "__main__":
    decrypt_main()
