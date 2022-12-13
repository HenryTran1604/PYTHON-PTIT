if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    maxv = max([max(a[i]) for i in range(n)])
    minv = min([min(a[i]) for i in range(n)])
    check = True
    res = []
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxv - minv:
                res.append((i, j))
    if len(res) == 0:
        print('NOT FOUND')
    else:
        print(maxv - minv)
        for t in res:
            print(f'Vi tri [{t[0]}][{t[1]}]')
    