# 将摩斯密码转换为字母的逆字典
MORSE_CODE_DICT_INV = {v: k for k, v in MORSE_CODE_DICT.items()}

# 摩斯密码解码函数
def decode_morse(morse_code):
    words = morse_code.split('   ')
    decoded_words = []
    for word in words:
        decoded_word = ''.join(MORSE_CODE_DICT_INV.get(letter, '?') for letter in word.split())
        decoded_words.append(decoded_word)
    return ' '.join(decoded_words)

def decode_main():
    morse_code_input = input("请输入摩斯密码：")
    decoded_message = decode_morse(morse_code_input)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    decode_main()
