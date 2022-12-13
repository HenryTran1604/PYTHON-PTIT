if __name__ == '__main__':
    n = int(input())
    a = []
    while len(a) < n:
        a.extend(list(map(int, input().split())))
    f = [0] * (a[-1] + 1)
    for x in a:
        f[x] = 1
    check = False
    for i in range(1, a[-1]):
        if f[i] == 0:
            check = True
            print(i)
    if not check:
        print('Excellent!')