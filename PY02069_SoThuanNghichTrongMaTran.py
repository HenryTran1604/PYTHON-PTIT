if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    try:
        maxv = max([a[i][j] for j in range(m) for i in range(n) if str(a[i][j]) == str(a[i][j])[::-1] and a[i][j] > 10])
    except:
        maxv = -1
    res = []
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxv:
                res.append((i, j))
    if len(res) == 0:
        print('NOT FOUND')
    else:
        print(maxv)
        for i in res:
            print(f'Vi tri [{i[0]}][{i[1]}]')