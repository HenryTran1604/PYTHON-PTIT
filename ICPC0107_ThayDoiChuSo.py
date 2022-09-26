if __name__ == '__main__':
    t = int(input())
    while t > 0:
        p, q = map(str, input().split())
        a = list(map(str, input().split()))
        x1, x2 = '', ''
        if len(a) == 2:
            x1, x2 = a
        else:
            x1 = a[0]
            x2 = input()
        # tong nho nhat
        n1, n2 = x1.replace(q, p), x2.replace(q, p)
        l1, l2 = x1.replace(p, q), x2.replace(p, q)
        res1, res2 = int(n1) + int(n2), int(l1) + int(l2)
        print(min(res1, res2), max(res1, res2))
        t -= 1
