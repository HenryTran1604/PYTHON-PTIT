import math


def isprime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    n, x = map(int, input().split())
    a = [0]
    for i in range(2, 10001):
        if isprime(i):
            a.append(i)
    for i in range(n + 1):
        print(x + a[i], end = ' ')
        x += a[i]

