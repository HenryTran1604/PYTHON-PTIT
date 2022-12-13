import math


def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    n = int(input())
    s = set()
    a = [0]
    for x in list(map(int, input().split())):
        if x not in s:
            a.append(x)
            s.add(x)
    for i in range(1, len(a)):
        a[i] += a[i - 1]
    pos = -1
    for i in range(1, len(a) - 1):
        if isPrime(a[i] - a[0]) and isPrime(a[-1] - a[i]):
            pos = i - 1
            break
    if pos == -1:
        print('NOT FOUND')
    else:
        print(pos)
