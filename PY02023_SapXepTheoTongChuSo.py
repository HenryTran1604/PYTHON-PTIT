def sumdigit(n):
    sum, tmp = 0, n
    while n > 0:
        sum += n % 10
        n //= 10
    return sum, tmp

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        a = list(map(int, input().split()))
        a.sort(key = sumdigit)
        for i in range(n):
            print(a[i], end = ' ')
        print()
        t -= 1