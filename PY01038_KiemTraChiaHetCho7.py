if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        limit = 1000
        res = -1
        while limit > 0:
            if n % 7 == 0:
                res = n;
                break
            n = n + int(str(n)[::-1])
            limit -= 1
        print(res)
        t -= 1