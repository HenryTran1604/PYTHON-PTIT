import math

def check(n):
    while n > 0:
        r = n % 10
        if r == 1 or r == 3 or r == 5 or r == 7 or r == 9:
            return False
        n //= 10
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        for i in range(2, math.isqrt(n) , 2):
            if int(str(i) + str(i)[::-1]) >= n:
                break
            if check(i):
                print(str(i) + str(i)[::-1], end = ' ')
        print()
        t -= 1
