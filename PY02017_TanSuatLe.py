if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        a = list(map(int, input().split()))
        res = a[0]
        for i in range(1, n):
            res = res ^ a[i]
        print(res)
        t -= 1