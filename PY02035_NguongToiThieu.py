if __name__ == '__main__':
    s = input()
    k = int(input())
    d = dict()
    for i in range(0, len(s) - 1, 2):
        tmp = s[i : i + 2]
        if tmp in d:
            d[tmp] += 1
        else:
            d[tmp] = 1
    a = sorted(d)
    check = False
    for x in a:
        if d[x] >= k:
            check = True
            print(x, d[x])
    if not check:
        print('NOT FOUND')