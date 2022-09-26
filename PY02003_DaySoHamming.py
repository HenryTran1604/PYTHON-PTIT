def binarysearch(a, x):
    l, r = 0, len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return m + 1
        elif a[m] > x:
            r = m - 1
        else:
            l = m + 1
    return 0

a = set()
def Try(s):
    a.add(s)
    if 2 * s not in a and 2 * s <= 10 ** 18:
        Try(2 * s)
    if 3 * s not in a and 3 * s <= 10 ** 18:
        Try(3 * s)
    if 5 * s not in a and 5 * s <= 10 ** 18:
        Try(5 * s)


if __name__ == '__main__':
    Try(1)
    s = sorted(a)
    t = int(input())
    while t > 0:
        n = int(input())
        if n not in a:
            print('Not in sequence')
        else:
            print(binarysearch(s, n))
        t -= 1
