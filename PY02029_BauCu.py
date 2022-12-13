if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    f = [0] * (m + 1)
    cnt, curr = 0, 0
    for x in a:
        f[x] += 1
    se = set(f)
    if len(se) == 2: # 0 va 1 so
        print('NONE')
    else:
        maxpos1, maxpos2 = 0, 0
        for i in range(1, m + 1):
            if f[maxpos1] < f[i]:
                maxpos1 = i
        for i in range(1, m + 1):
            if f[i] != f[maxpos1] and f[i] > f[maxpos2]:
                maxpos2 = i
        print(maxpos2)