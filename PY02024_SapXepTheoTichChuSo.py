def muldigit(n):
    res, tmp = 1, n
    while n > 0:
        res *= n % 10
        n //= 10
    return res, tmp

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        a = list(map(int, input().split()))
        a.sort(key = muldigit)
        for x in a:
            print(x, end = ' ')
        print()
        t -= 1