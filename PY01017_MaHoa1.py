if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        s = s + ' '
        cnt = 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                cnt += 1
            else:
                print(cnt, s[i], sep='', end='')
                cnt = 1
        print()
        t -= 1
