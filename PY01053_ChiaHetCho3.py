if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        sum = 0
        for i in range(len(s)):
            sum += int(s[i])
        if sum % 3 == 0:
            print('YES')
        else:
            print('NO')
        t -= 1
