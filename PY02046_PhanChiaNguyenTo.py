import math


def isprime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    for i in range(1, len(b)):
        b[i] += b[i - 1]
    check = False
    for i in range(len(b)):
        if isprime(b[i]) and isprime(b[-1] - b[i]):
            check = True
            print(i)
            break
    if not check:
        print('NOT FOUND')
    