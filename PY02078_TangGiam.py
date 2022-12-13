if __name__ == '__main__':
    t = int(input())
    while t > 0:
        a, b = [], []
        n = int(input())
        for _ in range(n):
            x, y = map(float, input().split())
            a.append(x)
            b.append(y)
        l, ans = [1] * n, 0
        for i in range(n):
            for j in range(0, i):
                if a[j] < a[i] and b[j] > b[i]:
                    l[i] = max(l[i], l[j] + 1)
            ans = max(ans, l[i])
        print(ans)
        t -= 1