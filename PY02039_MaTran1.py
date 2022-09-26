if __name__ == '__main__':
    n = int(input())
    a = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    k = int(input())
    sum1 = sum([a[i][j] for j in range(n) for i in range(n) if i < j])
    sum2 = sum([a[i][j] for j in range(n) for i in range(n) if i > j])
    print('YES' if abs(sum1 - sum2) <= k else 'NO', abs(sum1 - sum2), sep = '\n')
