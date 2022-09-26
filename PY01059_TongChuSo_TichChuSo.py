if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        sum, mul = 0, 1
        check = True
        for i in range(len(s)):
            if i % 2 == 0:
                sum += int(s[i])
            else:
                if s[i] != '0':
                    mul *= int(s[i])
                    check = False
        if check:
            mul = 0
        print(sum, mul)
        t -= 1
