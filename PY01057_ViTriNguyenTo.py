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
        check = True
        for i in range(len(s)):
            id = int(s[i])
            if not (isprime(id)) and id < len(s) and isprime(int(s[id])):
                check = False
                break
        if check:
            print('YES')
        else:
            print('NO')
        t -= 1
