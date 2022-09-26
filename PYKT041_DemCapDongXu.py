if __name__ == '__main__':
    n = int(input())
    a = [['.' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        a[i] = list(input())
    # count row
    cnt = 0
    for i in range(n):
        d = a[i].count('C')
        cnt += d * (d - 1) // 2
    for j in range(n):
        d = 0
        for i in range(n):
            if a[i][j] == 'C':
                d += 1
        cnt += d * (d - 1) // 2
    print(cnt)
