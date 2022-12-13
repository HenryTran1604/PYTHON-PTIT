import math


def isprime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    n = int(input())
    maxv = 0
    a = list(map(int, input().split()))
    for x in a:
        i, j = 0, 0
        while not isprime(x + i):
            i += 1
        while not isprime(x - j):
            j += 1
        maxv = max(maxv, min(i, j))
    print(maxv)
