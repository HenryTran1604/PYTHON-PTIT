import math


def isprime2(n):
    if n < 2:
        return False
    if n < 4:
        return True;
    if n % 2 == 0 or n % 3 == 0:
        return False
    tmp = int(math.sqrt(n))
    for i in range(2, tmp + 1, 5):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def isprime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False;
    return n >= 2


t = int(input())
while t > 0:
    n = int(input())
    cnt = 0
    for i in range(0, n):
        if math.gcd(i, n) == 1:
            cnt += 1
    if isprime2(cnt):
        print("YES")
    else:
        print("NO")
    t -= 1
