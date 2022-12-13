if __name__ == '__main__':
    n, m = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    inter = sorted(a.intersection(b))
    aDiffb = sorted(a.difference(b))
    bDiffa = sorted(b.difference(a))
    for x in inter:
        print(x, end=' ')
    print()
    for x in aDiffb:
        print(x, end=' ')
    print()
    for x in bDiffa:
        print(x, end=' ')