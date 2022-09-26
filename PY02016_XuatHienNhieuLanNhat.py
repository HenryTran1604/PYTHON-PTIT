if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        a = list(map(int, input().split()))
        f = [0] * (10 ** 6 + 1)
        res = 0
        for i in range(n):
            f[a[i]] += 1
            if f[a[i]] > f[res] or (f[a[i]] == f[res] and a[i] < res) :
                res = a[i]
        if f[res] > n //2:
            print(res)
        else:
            print('NO')
        t -= 1