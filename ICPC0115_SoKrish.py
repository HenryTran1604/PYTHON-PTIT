from math import factorial


import math

def check(n):
    sum, tmp = 0, n
    while n > 0:
        sum += math.factorial(n % 10)
        n //= 10
    return sum == tmp

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        if check(n):
            print('Yes')
        else:
            print('No')
        t -= 1