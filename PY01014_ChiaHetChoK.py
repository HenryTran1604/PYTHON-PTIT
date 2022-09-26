if __name__ == '__main__':
    a, k, n = map(int, input().split())
    if a >= n or k == 0:
        print(-1)
    else:
        check = False;
        start = (a//k + 1)*k - a
        for i in range(start, n - a + 1, k):
            print(i, end = ' ')
            check = True
        if not check:
            print(-1)

