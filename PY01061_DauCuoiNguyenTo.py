import math


def isprime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        if isprime(int(s[:3])) and isprime(int(s[-3:])):
            print('YES')
        else:
            print('NO')
        t -= 1
