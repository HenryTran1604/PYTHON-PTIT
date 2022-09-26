if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        if s[0] == s[-1]:
            print('YES')
        else:
            print('NO')
        t -= 1