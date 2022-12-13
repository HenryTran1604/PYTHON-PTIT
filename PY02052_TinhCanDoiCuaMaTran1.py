if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    chenhLech = 0
    for i in range(n):
        for j in range(n):
            if j > i:
                chenhLech += a[i][j]
            elif i > j:
                chenhLech -= a[i][j]
    chenhLech = abs(chenhLech)
    k = int(input())
    if chenhLech <= k:
        print('YES')
    else:
        print('NO')
    print(chenhLech)