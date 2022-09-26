if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n, m = map(int, input().split())
        h = [[0 for _ in range(m)] for _ in range(n)]
        k = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(n):
            h[i] = list(map(int, input().split()))
        for i in range(3):
            k[i] = list(map(int, input().split()))
        res = [[0 for _ in range(n - 2)] for _ in range(m - 2)]
        ans = 0
        for i in range(n - 2):
            for j in range(m - 2):
                for p in range(3):
                    for q in range(3):
                        res[i][j] += h[i + p][j + q] * k[p][q]
                ans += res[i][j]
        print(res)
        t -= 1
