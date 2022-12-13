if __name__ == '__main__':
    n = int(input())
    d = dict()
    key = ''
    for _ in range(n):
        x = input()
        if len(key) == 0:
            key = x
            d[key] = 0
        elif len(x) == 0:
            key = ''
        else:
            d[key] += 1
    for x in d:
        print(f'{x}: {d[x]}')

