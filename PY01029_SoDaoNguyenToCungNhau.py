import math

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        if math.gcd(int(s), int(s[::-1])) == 1:
            print('YES')
        else:
            print('NO')
        t -= 1