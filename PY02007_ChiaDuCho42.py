if __name__ == '__main__':
    l = 10
    f = [0] * 42
    while l > 0:
        a = list(map(int, input().split()))
        l -= len(a)
        for i in range(len(a)):
            f[a[i] % 42] = 1
    print(len([x for x in f if x == 1]))
