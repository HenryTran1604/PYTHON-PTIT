d = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    cnt = 0
    vis = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i][j] == -1:
                for k in range(8):
                    x, y = i + d[k][0], j + d[k][1]
                    if x >= 0 and x < n and y >= 0 and y < m and not vis[x][y]:
                        cnt += a[x][y]
                        vis[x][y] = True
    print(cnt)
