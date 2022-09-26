import math


def isprime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def check(s):
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
        if (int(s[i]) - i) % 2 == 1:
            return False
    return isprime(sum)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        if check(s):
            print('YES')
        else:
            print('NO')
        t -= 1
