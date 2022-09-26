if __name__ == '__main__':
    s1 = set(map(str, input().lower().split()))
    s2 = set(map(str, input().lower().split()))
    inter = sorted(s1.intersection(s2))
    uni = sorted(s1.union(s2))
    for x in uni:
        print(x, end = ' ')
    print()
    for x in inter:
        print(x, end = ' ')