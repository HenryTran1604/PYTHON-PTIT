import math


def isprime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    p = []
    for i in range(n):
        if isprime(a[i]):
            p.append(a[i])
    p.sort()
    id = 0
    for i in range(n):
        if a[i] in p:
            print(p[id], end=' ')
            id += 1
        else:
            print(a[i], end=' ')