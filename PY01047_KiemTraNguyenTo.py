import math


def isprime(n):
    for i in range(2, math.isqrt(n)):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        if len(s) > 4:
            s = s[- 4:]
        if isprime(int(s)):
            print('YES')
        else:
            print('NO')
        t -= 1