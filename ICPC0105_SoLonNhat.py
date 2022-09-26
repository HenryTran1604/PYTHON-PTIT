if __name__ == '__main__':
    t = int(input())
    while t  > 0:
        s = input()
        num, res = 0, 0
        for i in range(len(s)):
            if s[i].isdigit():
                num = 10 * num + int(s[i])
            else:
                num = 0
            res = max(num, res)
        print(res)
        t -= 1