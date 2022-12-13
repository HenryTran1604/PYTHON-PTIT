if __name__ == '__main__':
    n = int(input())
    a = []
    while len(a) < n:
        a.extend(list(map(int, input().split())))
    even = sorted([x for x in a if x % 2 == 0])
    odd = sorted([x for x in a if x % 2 == 1], reverse=True)
    i1, i2 = 0, 0
    for x in a:
        if x % 2 == 0:
            print(even[i1], end=' ')
            i1 += 1
        else:
            print(odd[i2], end=' ')
            i2 += 1
