def binarysearch(a, x):
    l, r = 0, len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return m + 1
        if a[m] > x:
            r = m - 1
        else:
            l = m + 1
    return 0


a, b = [], []
s = set()
a.append(1)
b.append(1)
s.add(1)
maxval = 1
while maxval != 10 ** 18:
    top = a.pop(0)
    maxval = max(maxval, 2*top, 3*top, 5*top)
    if 2 * top not in s:
        a.append(2*top)
        a.append(2 * top)
        b.append(2 * top)
        s.add(2 * top)
    if 3 * top not in s:
        a.append(3 * top)
        b.append(3 * top)
        s.add(3 * top)
    if 5 * top not in s:
        a.append(5 * top)
        b.append(5 * top)
        s.add(5 * top)
b.sort()
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        if n not in s:
            print('Not in sequence')
        else:
            print(binarysearch(b, n))
        t -= 1
