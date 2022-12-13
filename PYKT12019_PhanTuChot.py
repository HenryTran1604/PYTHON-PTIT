if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        a = list(map(int, input().split()))
        l, r = [0] * n, [0] * n
        l[0], r[n - 1] = a[0], a[n - 1]
        min1 = a[n - 1]
        for i in range(1, n):
            l[i] = max(l[i - 1], a[i])
        for i in range(n - 2, -1, -1):
            if min1 == a[i]:
                r[i] = -1
            else:
                min1 = min(min1, a[i])
                r[i] = min1
            
        cnt = 0
        for i in range(n):
            if l[i] == r[i]:
                cnt += 1
        print(cnt)
        t -= 1

