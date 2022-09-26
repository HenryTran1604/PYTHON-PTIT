import math


def solve(s):
    sum = 0
    tmp = 1
    for i in range(len(s) - 1, -1, -1):
        sum += int(s[i])*tmp
        tmp *= 2
    if sum >= 10:
        return chr(sum%10 + ord('A'))
    return sum


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        coso = int(input())
        k = int(math.log2(coso))
        s = input()
        while len(s) % k != 0:
            s = '0' + s
        for i in range(0, len(s), k):
            print(solve(s[i:i+k]), end = '')
        print()
        t -= 1
