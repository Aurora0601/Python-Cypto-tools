# 摩斯密码字典
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}

# 将摩斯密码转换为字母的逆字典
MORSE_CODE_DICT_INV = {v: k for k, v in MORSE_CODE_DICT.items()}


# 摩斯密码编码函数
def encode_morse(text):
    text = text.upper()
    return '   '.join(MORSE_CODE_DICT.get(char, '') for char in text)


# 摩斯密码解码函数
def decode_morse(morse_code):
    words = morse_code.split('   ')
    decoded_words = []
    for word in words:
        decoded_word = ''.join(MORSE_CODE_DICT_INV.get(letter, '?') for letter in word.split())
        decoded_words.append(decoded_word)
    return ' '.join(decoded_words)


# 主函数
def main():
    print("请选择操作：")
    print("1. 摩斯密码编码")
    print("2. 摩斯密码解码")

    choice = input("请输入你的选择（1/2）：")

    if choice == '1':
        text_to_encode = input("请输入要编码的文本（大写英文）: ")
        encoded_text = encode_morse(text_to_encode)
        print("摩斯密码编码后文本:", encoded_text)
    elif choice == '2':
        morse_code_input = input("请输入摩斯密码：")
        decoded_message = decode_morse(morse_code_input)
        print("Decoded message:", decoded_message)
    else:
        print("无效的选择，请输入 1 或 2。")


if __name__ == "__main__":
    main()