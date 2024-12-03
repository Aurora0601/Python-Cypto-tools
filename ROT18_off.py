def royt18_decode(char):
    if 'a' <= char <= 'z':  # 小写字母
        return chr((ord(char) - ord('a') - 18) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':  # 大写字母
        return chr((ord(char) - ord('A') - 18) % 26 + ord('A'))
    else:
        return char  # 非字母字符不变

def royt18_decode_message(ciphertext):
    return ''.join(royt18_decode(char) for char in ciphertext)

# 用户输入密文
ciphertext = input("请输入密文: ")

# 解码
decoded_text = royt18_decode_message(ciphertext)
print("解码后的文本:", decoded_text)
