if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    maxv = -1
    for i in range(n):
        for j in range(m):
            if a[i][j] > 10 and a[i][j] == int(str(a[i][j])[::-1]):
                maxv = max(maxv, a[i][j])
    if maxv == -1:
        print('NOT FOUND')
    else:
        print(maxv)
        for i in range(n):
            for j in range(m):
                if a[i][j] == maxv:
                    print(f'Vi tri [{i}][{j}]')
    