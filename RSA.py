import math
import random
from Crypto.Util.number import inverse, GCD

def prime_test(m, k):
    temp = k
    while temp > 0:
        x = random.randint(2, m - 1)
        if math.gcd(x, m) == 1:
            if pow(x, m - 1, m) == 1:
                temp = temp - 1
                if temp == 0:
                    print('是素数的概率为:{:.5f}%'.format(100 * (1.0 - (1.0 / (2 ** (k - temp))))))
            else:
                print('随机数选择到合数，需重新选择随机数')
                return 0
        else:
            print('随机数选择到合数，需重新选择随机数')
            return 0
    if temp == 0:
        may = 100 * (1.0 - (1.0 / (2 ** k)))
        if may > 99:
            return 1
        else:
            return 0

def select_porq(k):
    x = random.randrange(2**(k-1), 2**k)
    while prime_test(x, 10) == 0:
        x = random.randrange(2**(k-1), 2**k)
    return x

def select_e(fn):
    while 1:
        e = random.randrange(2, fn)
        if GCD(e, fn) == 1:
            return e

def encrypt(m, e, n):
    list = []
    for x in m:
        list.append(pow(ord(x), e, n))
    return list

if __name__ == "__main__":
    print('请输入RSA密钥位数:')
    k = int(input())
    print('请输入需要加密的明文:')
    m = input()
    p = select_porq(k)
    q = select_porq(k)
    n = p * q
    fn = (p - 1) * (q - 1)
    e = select_e(fn)
    d = inverse(e, fn)
    print('p的值:', p)
    print('q的值:', q)
    print('n的值:', n)
    print('fn的值:', fn)
    print('e的值:', e)
    print('d的值:', d)
    cipher = encrypt(m, e, n)
    print('加密后的密文(列表中每一项对应一个字符):', cipher)
