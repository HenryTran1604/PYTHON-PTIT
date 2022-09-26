if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 1
    a.sort()
    for i in range(1, n):
        if a[i] - a[i - 1] > k:
            ans += 1
    print(ans)