n, k = 4, 2
c, a = [0] * 30, []
def out():
    for i in range(1, k + 1):
        print(a[c[i] - 1], end = ' ')
    print()
def Try(i):
    for j in range(c[i - 1] + 1, n - k + i + 1):
        c[i] = j
        if i == k:
            out()
        else:
            Try(i + 1)

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = sorted(set(input().split()))
    n = len(a)
    Try(1)

