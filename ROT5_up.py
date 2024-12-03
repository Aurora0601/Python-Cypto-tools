def rot5_encode(char):
    if 'a' <= char <= 'z':  # 小写字母
        return chr((ord(char) - ord('a') + 5) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':  # 大写字母
        return chr((ord(char) - ord('A') + 5) % 26 + ord('A'))
    else:
        return char  # 非字母字符不变

def rot5_encode_message(plaintext):
    return ''.join(rot5_encode(char) for char in plaintext)

# 用户输入明文
plaintext = input("请输入明文: ")

# 编码
encoded_text = rot5_encode_message(plaintext)
print("编码后的文本:", encoded_text)
