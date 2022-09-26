if __name__ == '__main__':
    s = input()
    d = dict()
    for i in range(0, len(s) - 1, 2):
        tmp = s[i : i + 2]
        if tmp in d:
            d[tmp] += 1
        else:
            d[tmp] = 1
    for x in d:
        print(x, d[x])