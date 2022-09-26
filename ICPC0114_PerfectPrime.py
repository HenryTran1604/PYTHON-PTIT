import math

def isprime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    tmp = math.isqrt(n)
    for i in range(5, tmp + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def check(n):
    sum, tmp = 0, n
    while n > 0:
        r = n % 10
        if r != 2 and r != 3 and r != 5 and r != 7:
            return False
        sum += r
        n //= 10
    return isprime(sum) and isprime(tmp) and isprime(int(str(tmp)[::-1]))

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        if check(n):
            print('Yes')
        else:
            print('No')
        t -= 1