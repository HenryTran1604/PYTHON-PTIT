if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n, b = map(int, input().split())
        res = str()
        while n > 0:
            r = n % b
            if r < 10:
                res += str(r)
            else:
                r -= 10
                res += chr(ord('A') + r)
            n //= b
        print(res[::-1])
        t -= 1