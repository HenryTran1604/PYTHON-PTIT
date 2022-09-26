n, k = 0, 0
c, a = [0] * 1001, [0] * 1001
def out():
    for i in range(1, k + 1):
        print(a[c[i]], end = ' ')
    print()

def Try(i):
    for j in range(c[i-1] + 1, n - k + i):
        c[i] = j
        if i == k:
            out()
        else:
            Try(i + 1)


if __name__ == '__main__':
    n, k = map(int, input().split())
    a = sorted(set(map(int, input().split())))
    a.insert(0, 0)
    n = len(a)
    Try(1)
