from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# 加密函数
def encrypt_aes(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ct_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return ct_bytes.hex()

# 解密函数
def decrypt_aes(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    pt = unpad(cipher.decrypt(bytes.fromhex(ciphertext)), AES.block_size)
    return pt.decode()

# 主函数
if __name__ == "__main__":
    key = get_random_bytes(16)  # AES需要一个16字节的密钥
    plaintext = input("请输入明文：")
    ciphertext = encrypt_aes(plaintext, key)
    print("加密后的密文是：", ciphertext)

    decrypted_text = decrypt_aes(ciphertext, key)
    print("解密后的明文是：", decrypted_text)