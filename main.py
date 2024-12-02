# 打开文件，指定编码为utf-8
with open('help.txt', 'r', encoding='utf-8') as file:
    # 逐行读取并打印
    for line in file:
        print(line, end='')  # end='' 防止print函数添加额外的换行符