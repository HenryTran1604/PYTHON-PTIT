if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        res = 1
        for i in range(len(s)):
            if s[i] != '0':
                res *= int(s[i])
        print(res)
        t -= 1