import math


def isprime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    d = dict()
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    for x in a:
        if d[x] != 0 and isprime(x):
            print(x, d[x])
            d[x] = 0