from sys import stdin


if __name__ == '__main__':
    d = []
    for line in stdin:
        d += list(map(int, input().split()))
    n = d[0]
    a = d[1:]
    x, sz = max(a), 1
    curSz = 0
    for i in range(n):
        if a[i] == x:
            curSz += 1
            sz = max(sz, curSz)
        else:
            curSz = 0
    print(sz)