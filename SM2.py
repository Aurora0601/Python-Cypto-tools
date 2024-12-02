import random
import math
import os
import binascii
from gmpy2 import powmod, invert, is_prime
import re

# SM3的初始向量
IV = [
    0x7380166F, 0x4914B2B9, 0x172442D7, 0xDA8A0600,
    0xA96F30BC, 0x163138AA, 0xE38DEE4D, 0xB0FB0E4E
]

# 布尔函数FFj
# SM2的曲线参数
p = 0xfffffffeffffffffffffffffffffffffffffffff00000000ffffffffffffffff
a = 0xfffffffeffffffffffffffffffffffffffffffff00000000fffffffffffffffc
b = 0x28e9fa9e9d9f5e344d5a9e4bcf6509a7f39789f515ab8f92ddbcbd414d940e93
gx = 0x32c4ae2c1f1981195f9904466a39c9948fe30bbff2660be1715a4589334c74c7
gy = 0xbc3736a2f4f6779c59bdcee36b692153d0a9877cc62a474002df32e52139f0a0
n = 0xfffffffeffffffffffffffffffffffff7203df6b21c6052b53bbf40939d54123

E_order = n


def FF(X, Y, Z, j):
    if j < 16:
        return X ^ Y ^ Z
    else:
        return (X & Y) | (X & Z) | (Y & Z)


# 置换函数


def P0(X):
    return X ^ LS(X, 9) ^ LS(X, 17)


def P1(X):
    return X ^ LS(X, 15) ^ LS(X, 23)


# 循环左移


def LS(X, n):
    return ((X << n) & 0xFFFFFFFF) | (X >> (32 - n))


# 布尔函数GGj


def GG(X, Y, Z, j):
    if j < 16:
        return X ^ Y ^ Z
    else:
        return (X & Y) | (~X & Z)


# 消息填充函数


def pad_message(message):
    mlen1 = len(message)
    mlen = mlen1
    message += b'\x80'
    mlen += 1
    while mlen % 64 != 56:
        message += b'\x00'
        mlen += 1
    message += (mlen1 * 8).to_bytes(8, 'big')
    return message


# SM3压缩函数


def SM3_CF(V, B, k):
    W = [0] * 68
    W_ = [0] * 64
    for i in range(16):
        W[i] = int.from_bytes(B[i * 4:i * 4 + 4], 'big')
    for i in range(16, 68):
        W[i] = P1(W[i - 16] ^ W[i - 9] ^ LS(W[i - 3], 15)) ^ LS(W[i - 13], 7) ^ W[i - 6]
    for i in range(64):
        W_[i] = W[i] ^ W[i + 4]
    # for i in range(0, len(W), 4):
    # print(' '.join(hex(value) for value in W[i:i+4]))

    A, B, C, D, E, F, G, H = V
    for i in range(64):
        SS1 = LS((LS(A, 12) + E + LS(T(i), i % 32)) & 0xFFFFFFFF, 7)
        SS2 = SS1 ^ LS(A, 12)
        TT1 = (FF(A, B, C, i) + D + SS2 + W_[i]) & 0xFFFFFFFF
        TT2 = (GG(E, F, G, i) + H + SS1 + W[i]) & 0xFFFFFFFF
        D = C
        C = LS(B, 9)
        B = A
        A = TT1
        H = G
        G = LS(F, 19)
        F = E
        E = P0(TT2)
        # print(
        #     f"Step {i+1} - A: {A:08X}, B: {B:08X}, C: {C:08X}, D: {D:08X}, E: {E:08X}, F: {F:08X}, G: {G:08X}, H: {H:08X}")
    return A, B, C, D, E, F, G, H


# T函数


def T(j):
    if j < 16:
        return 0x79CC4519
    else:
        return 0x7A879D8A


# SM3哈希函数


def string_to_ascii(s):
    return [ord(c) for c in s]


def or_16(A, B):
    A = int(A, 16)
    B = int(B, 16)
    C = A ^ B
    C = '{:08x}'.format(C)
    return C


# SM3哈希函数


# # 示例
# message = 'abc'
# hash_value = SM3(message)
# formatted_hex_string2 = re.sub(r'(.{8})', r'\1 ', hash_value)
# print("Hash Value:", formatted_hex_string2)


def sm3_hash(message):
    return SM3(message)


# def modinv(a, m):
#     # 使用扩展欧几里得算法来计算模逆
#     def extended_gcd(a, b):
#         if a == 0:
#             return b, 0, 1
#         else:
#             gcd, x, y = extended_gcd(b % a, a)
#             return gcd, y - (b // a) * x, x

#     gcd, x, _ = extended_gcd(a, m)
#     if gcd != 1:
#         raise ValueError('模逆不存在')
#     else:
#         return x % m
def modinv(a, m):
    def extended_gcd(a, b):
        x0, x1, y0, y1 = 1, 0, 0, 1
        while b != 0:
            q, a, b = a // b, b, a % b
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return a, x0, y0

    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError('模逆不存在')
    else:
        return x % m


def add(x1, y1, x2, y2, a, p):
    # a是曲线参数，p是选取的素数
    if x1 == x2 and y1 != y2:
        return 0, 0
    # 互为逆元，为无穷远点，舍弃
    if x1 == x2 and y1 == y2:
        l = (3 * x1 * x1 + a) * modinv(2 * y1, p)
    else:
        l = (y2 - y1) * modinv(x2 - x1, p)
    x3 = l * l - x1 - x2
    y3 = l * (x1 - x3) - y1
    return x3 % p, y3 % p


def mul(x1, y1, k, a, p):
    # a是曲线参数，p是选取的素数
    if k == 0:
        return 0, 0
    if k == 1:
        return x1, y1
    if k % 2 == 0:
        x2, y2 = mul(x1, y1, k // 2, a, p)
        return add(x2, y2, x2, y2, a, p)
    else:
        x2, y2 = mul(x1, y1, (k - 1) // 2, a, p)
        return add(x2, y2, x1, y1, a, p)


# 将读入的字符以ascii值转换为8位的比特串，并且返回比特串的长度


def string_to_binary_number(input_string):
    # 初始化一个空字符串来存储二进制表示
    binary_string = ''

    # 遍历输入字符串中的每个字符
    for char in input_string:
        # 获取字符的ASCII值
        ascii_value = ord(char)
        # 将ASCII值转换为8位的二进制字符串，并添加到binary_string中
        binary_string += format(ascii_value, '08b')

    # 将二进制字符串转换为整数
    binary_number = int(binary_string, 2)

    return binary_number, len(binary_string)


# def SM3(message_bytes):
#     # ascii_values = string_to_ascii(message)
#     # message_bytes = bytes(ascii_values)
#     padded_message = pad_message(message_bytes)
#     result = ''
#     for i in IV:
#         result += '{:08x}'.format(i)
#     V = IV.copy()
#     for i in range(len(padded_message) // 64):
#         B = padded_message[i*64:(i+1)*64]
#         V = SM3_CF(V, B, i)
#         hex_string1 = binascii.hexlify(B).decode()

#         formatted_hex_string1 = re.sub(r'(.{8})', r'\1 ', hex_string1)
#         print(
#             f"Extended Message at Step {i+1}: {formatted_hex_string1}")
#         all = ''
#         for iii in V:
#             all += '{:08x}'.format(iii)
#         result = or_16(all, result)

#     # return result
#     result_bytes = bytes.fromhex(result)
#     return int.from_bytes(result_bytes, byteorder='big')


# def SM3(message_bytes):
#     padded_message = pad_message(message_bytes)
#     V = IV.copy()
#     for i in range(len(padded_message) // 64):
#         B = padded_message[i*64:(i+1)*64]
#         V = SM3_CF(V, B, i)
#         hex_string1 = binascii.hexlify(B).decode()
#         formatted_hex_string1 = re.sub(r'(.{8})', r'\1 ', hex_string1)
#         print(f"Extended Message at Step {i+1}: {formatted_hex_string1}")

#     result = ''.join('{:08x}'.format(v) for v in V)
#     result_bytes = bytes.fromhex(result)
#     return result_bytes

def SM3(message_bytes):
    # ascii_values = string_to_ascii(message)
    # message_bytes = bytes(ascii_values)
    padded_message = pad_message(message_bytes)
    result = ''
    for i in IV:
        result += '{:08x}'.format(i)
    V = IV.copy()
    for i in range(len(padded_message) // 64):
        B = padded_message[i * 64:(i + 1) * 64]
        V = SM3_CF(V, B, i)
        hex_string1 = binascii.hexlify(B).decode()

        formatted_hex_string1 = re.sub(r'(.{8})', r'\1 ', hex_string1)
        # print(
        # f"Extended Message at Step {i+1}: {formatted_hex_string1}")
        all = ''
        for iii in V:
            all += '{:08x}'.format(iii)
        result = or_16(all, result)

    return bytes.fromhex(result)


# def KDF(Z, klen):
#     ct = 1
#     v = 256  # SM3 输出是256位
#     Ha = b""
#     for i in range((klen + v - 1) // v):  # 向上取整 (klen / v)
#         hash_input = Z + ct.to_bytes(4, byteorder='big')
#         Ha += SM3(hash_input.to_hex()).to_bytes(32,
#                                                 byteorder='big')  # SM3 hash to bytes
#         ct += 1
#     return Ha[:klen // 8]  # 只取前 klen 位


def KDF(Z, klen):
    ct = 1
    v = 256  # SM3 输出是256位
    Ha = b""
    for i in range((klen + v - 1) // v):  # 向上取整 (klen / v)
        hash_input = Z + ct.to_bytes(4, byteorder='big')
        Ha += SM3(hash_input)
        ct += 1
    return Ha[:klen // 8]  # 只取前 klen 位


def is_all_zeros(bitstring):
    # 检查是否是全0序列
    return all(b == 0 for b in bitstring)


def format_hex_with_spaces(hex_str):
    # 每8个字符插入一个空格
    return ' '.join(hex_str[i:i + 8] for i in range(0, len(hex_str), 8))


def keys():
    d = random.SystemRandom().randrange(1, n - 1)  # 私钥
    # print(f"私钥为：{hex(d)}")
    xp, yp = mul(gx, gy, d, a, p)
    return d, xp, yp


def enc():
    while 1:
        # 公钥加密
        d = 0xc9b4281d041bf8c51a1d275209f92eba127a439fc20b0b0cbf41d3afbaf17209
        # d, xp, yp = keys()
        xp, yp = mul(gx, gy, d, a, p)
        print(f"私钥为：{hex(d)}")
        print(f"公钥横坐标为：{hex(xp)}")
        print(f"公钥纵坐标为：{hex(yp)}")
        # print(hex(xp))
        # print(hex(yp))

        # xp=0x9993c9fb227dc53bfa8cdf2724e148147ed00c29c2dfc6537bc12caab946365e
        # yp=0xd65eba5e9965e0a4d62328d787d2e4cb72d3b954ace3f2b1232e858924d481a2

        # 获取明文，转换为二进制比特串
        input_string = input("请输入明文\n")
        message, klen = string_to_binary_number(input_string)
        message1 = bin(message)
        message1 = message1[2:]
        print(f"明文比特串为：{message1}\n")

        # k = random.SystemRandom().randrange(1, n-1)
        k = 0xe1bf10a1ff46073ec16d1eddb6bf5a9c79b58b236d979355b18b1858c255eb75
        print(f"随机数k为：{hex(k)}\n")
        x1, y1 = mul(gx, gy, k, a, p)
        C1 = x1.to_bytes(32, byteorder='big') + y1.to_bytes(32, byteorder='big')
        # 将数据类型转化为比特串
        # x11 = bin(x1)
        # x11 = x11[2:]
        print(f"C1的x坐标为:{hex(x1)}\n")
        # y11 = bin(y1)
        # y11 = y11[2:]
        print(f"C1的y坐标为:{hex(y1)}\n")
        # 计算余因子
        h = E_order // n
        xs, ys = mul(gx, gy, h, a, p)
        if xs == 0 and ys == 0:
            raise ValueError("解密失败，S是无穷远点")
        # 验证失败，报错退出
        # 成功则进入加密部分
        # 计算
        x2, y2 = mul(xp, yp, k, a, p)
        # x22 = bin(x2)
        # y22 = bin(y2)
        # x22 = x22[2:]
        # y22 = y22[2:]
        x2_bytes = x2.to_bytes(32, byteorder='big')
        y2_bytes = y2.to_bytes(32, byteorder='big')
        print(f"C2的x坐标为:{hex(x2)}\n")
        print(f"C2的y坐标为:{hex(y2)}\n")
        Z = x2_bytes + y2_bytes

        # 调用 KDF 函数
        t = KDF(Z, klen)

        # 检查 t 是否为全0比特串
        if is_all_zeros(t):
            print("t 是全0比特串，需要回退并重新执行步骤。\n")
            continue
        else:
            print(f"t = {t.hex()}")
        M_bytes = int.to_bytes(message, klen // 8, byteorder='big')

        print(f"M_bytes={format_hex_with_spaces(M_bytes.hex())}\n")
        C2 = bytes(a ^ b for a, b in zip(M_bytes, t))
        C3_input = x2_bytes + M_bytes + y2_bytes
        C3 = sm3_hash(C3_input)

        # print(f"C2 = {C2.hex()}")
        # print(f"C3 = {C3.hex()}")
        C1_hex = C1.hex()
        C2_hex = C2.hex()
        C3_hex = C3.hex()
        # print(len(C1_hex))
        # print(len(C2_hex))
        # print(len(C3_hex))
        # 打印格式化后的16进制字符串
        print(f"C1 = {format_hex_with_spaces(C1_hex)}")
        print(f"C2 = {format_hex_with_spaces(C2_hex)}")
        print(f"C3 = {format_hex_with_spaces(C3_hex)}")

        C = C1_hex + C2_hex + C3_hex
        print(len(C))
        print(f"C = {format_hex_with_spaces(C)}")
        break


# 密文C   297f0d23 11858162 7d49846a 5fa4511c 13ba67d6 f9493c9f 9f897f61 dc258def f2ba9f9a 693dd185 33b93495 e9a2da9f 7ec7961a d7ca947f 4ea9e81d 47bfaf3a a12eb6d1 4e6e9d3f 23472a1a 33f13ca1 646c75f9
try:
    enc()
except ValueError as e:
    print(e)