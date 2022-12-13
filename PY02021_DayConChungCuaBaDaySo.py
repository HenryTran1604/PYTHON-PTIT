if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n, m, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))
        res = []
        i1, i2, i3 = 0, 0, 0
        while i1 < n and i2 < m and i3 < k:
            if a[i1] == b[i2] and b[i2] == c[i3]:
                res.append(a[i1])
                i1 += 1
                i2 += 1
                i3 += 1
            elif a[i1] < b[i2] or a[i1] < c[i3]:
                i1 += 1
            elif b[i2] < a[i1] or b[i2] < c[i3]:
                i2 += 1
            else:
                i3 += 1
        if len(res):
            for x in res:
                print(x, end=' ')
            print()
        else:
            print('NO')
        t -= 1