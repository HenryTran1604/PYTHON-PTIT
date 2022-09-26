from operator import le
import math

def isprime(n):
    for i in range(2, math.isqrt(n)):
        if n % i == 0:
            return False
    return True

def check(s):
    cntprime = 0
    if not isprime(len(s)):
        return False
    for i in range(len(s)):
        if s[i] == '2' or s[i] == '3' or s[i] == '5' or s[i] == '7':
            cntprime += 1
    return cntprime > len(s) - cntprime

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        if check(s):
            print('YES')
        else:
            print('NO')
        t -= 1
