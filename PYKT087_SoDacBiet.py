from lzma import MODE_FAST


if __name__ == '__main__':
    t = int(input())
    MOD = 10 ** 9 + 7
    while t > 0:
        n, k = map(int, input().split())
        res, tmp = 0, 1
        while k > 0:
            if k & 1 == 1:
                res = (res + tmp) % MOD
            tmp = (tmp * n) % MOD
            k >>= 1
        print(res)
        t -= 1