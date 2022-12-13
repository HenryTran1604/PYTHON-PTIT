if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        a = []
        for i in range(n):
            a.append(list(map(float, input().split())))
        for i, x in enumerate(map(float, input().split())):
            a[i].append(x)
        a.sort(key=lambda x : x.count(0))
        # b = list(map(float, input().split()))
        pos = -1
        for i in range(n - 1):
            a.sort(key=lambda x : x.count(0))
            pos += 1
            if a[i][pos] == 0:
                continue
            for row in range(i + 1, n):
                hs = a[row][pos]/a[i][pos]
                for col in range(pos, n + 1):
                    a[row][col] -= hs * a[i][col]
        # print(a)
        res = []
        for i in range(n - 1, -1, -1):
            if a[i][:n].count(0) == n:
                break
            if i == n - 1:
                res.append(a[i][n]/a[i][i])
            else:
                for j in range(n - 1, i, -1):
                    a[i][n] -= a[i][j] * res[n - j - 1]
                res.append(a[i][n] / a[i][i])
        if len(res) != n:
            print(-1)
        else:
            for x in res[::-1]:
                print('%.3f' % x, end = ' ')
            print()
        t -= 1