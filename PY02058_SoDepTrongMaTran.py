if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    maxv, minv = -1, 10 ** 4 + 1
    for i in range(n):
        maxv = max(maxv, max(a[i]))
        minv = min(minv, min(a[i]))
    res = []
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxv - minv:
                res.append((i, j))
    if len(res) == 0:
        print('NOT FOUND')
    else:
        print(maxv - minv)
        for i in res:
            print(f'Vi tri [{i[0]}][{i[1]}]')
