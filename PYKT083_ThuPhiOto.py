def mucGia(s, n):
    if s == 'Xe_con':
        if n == '5':
            return 10000
        return 15000
    if s == 'Xe_tai':
        return 20000
    if s == 'Xe_khach':
        if n == '29':
            return 50000
        return 70000

if __name__ == '__main__':
    n = int(input())
    d = dict()
    for _ in range(n):
        a = input().split()
        if a[3] == 'IN':
            if a[4] in d:
                d[a[4]] += mucGia(a[1], a[2])
            else:
                d[a[4]] = mucGia(a[1], a[2])
    for key in d:
        print(f'{key}: {d[key]}')
