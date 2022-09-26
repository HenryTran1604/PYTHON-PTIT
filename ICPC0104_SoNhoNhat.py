if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        num, res = 0, 10**18
        check = False
        for i in range(len(s)):
            if s[i].isdigit():
                num = 10 * num + int(s[i])
                check = True
            else:
                if check:
                    res = min(res, num)
                check = False
                num = 0
        print(res)
        t -= 1