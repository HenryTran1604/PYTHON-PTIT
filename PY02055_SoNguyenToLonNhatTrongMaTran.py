import math


def isprime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    maxPrime = -1
    for i in range(n):
        for j in range(m):
            if a[i][j] > maxPrime and isprime(a[i][j]):
                maxPrime = a[i][j]
    if maxPrime == -1:
        print('NOT FOUND')
    else:
        print(maxPrime)
        for i in range(n):
            for j in range(m):
                if a[i][j] == maxPrime:
                    print(f'Vi tri [{i}][{j}]')
    