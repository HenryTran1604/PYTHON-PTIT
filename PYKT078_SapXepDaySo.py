if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        maxv, pos = -10**10, -1
        for i in range(n):
            if maxv < a[i]:
                maxv = a[i]
                pos = i
        a.insert(pos, m)
        for x in a:
            if x < 0:
                print(x, end=' ')
        for x in a:
            if x >= 0:
                print(x, end=' ')
        print()
        t -= 1