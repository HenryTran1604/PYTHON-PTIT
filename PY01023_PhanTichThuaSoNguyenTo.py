import math


def phantich(n):
    if n == 1:
        print(1)
        return
    print('1', end = '')
    cnt = 0
    while n % 2 == 0:
        cnt += 1
        n >>= 1
    if cnt != 0:
        print(' * 2^', cnt, sep = '', end = ' ')
    for i in range(3, math.isqrt(n) + 1, 2):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n //= i
        if cnt != 0:
            print(' * ' , i, '^', cnt, sep = '', end = ' ')
    if n > 1:
        print(' * ', n, '^', 1, sep = '', end = '')
    print()

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        phantich(n)
        t -= 1