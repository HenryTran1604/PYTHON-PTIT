if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    if n > m:
        cnt = n - m
        for i in range(n):
            if i % 2 == 0 and i//2 < cnt:
                continue
            for j in range(m):
                print(a[i][j], end=' ')
            print()
    else:
        cnt = m - n
        for i in range(n):
            for j in range(m):
                if j % 2 == 1 and (j - 1) // 2 < cnt:
                    continue
                print(a[i][j], end=' ')
            print()

    