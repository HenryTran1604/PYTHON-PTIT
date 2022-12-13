if __name__ == '__main__':
    n = int(input())
    b = []
    for _ in range(n):
        b.append(list(map(int, input().split())))
    if n == 2:
        print(f'1 {b[1][0] - 1}')
    else:
        a = []
        currSum = b[n-1][n-2]
        for j in range(n-3, -1, -1):
            colSum = 0
            for i in range(j, n):
                colSum += b[i][j]
            a.append((colSum-currSum)//(n-j-1))
            currSum += a[-1]
        a.insert(0, b[n-2][0] - a[-1])
        a.insert(0, b[n-1][0] - a[-1])
        for x in a[::-1]:
            print(x, end=' ')