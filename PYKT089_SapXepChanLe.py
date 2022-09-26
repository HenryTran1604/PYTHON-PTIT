if __name__ == '__main__':
    n = int(input())
    a = list()
    while len(a) != n:
        a += list(map(int, input().split()))
    b = sorted([x for x in a if x % 2 == 0])
    c = sorted([x for x in a if x % 2 != 0], reverse = True)
    i1, i2 = 0, 0
    for x in a:
        if x % 2 == 0:
            print(b[i1], end = ' ')
            i1 += 1
        else:
            print(c[i2], end = ' ')
            i2 += 1