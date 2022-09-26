import math


def check(n):
    while n > 0:
        r = n % 10
        if r != 0 and r != 2 and r != 4 and r != 6 and r != 8:
            return False
        n //= 10
    return True


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        i = 2
        while True:
            if int(str(i) + str(i)[::-1]) >= n:
                break
            if check(i):
                print(i, str(i)[::-1], sep = '', end = ' ')
            i += 1
        print()
        t -= 1