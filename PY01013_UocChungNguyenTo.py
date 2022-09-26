import math


def isprime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False;
    return n > 1
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        a, b = map(int, input().split())
        c = math.gcd(a, b)
        sum = 0
        while c > 0:
            sum += c % 10
            c //= 10
        if isprime(sum):
            print("YES")
        else:
            print("NO")
        t -= 1
