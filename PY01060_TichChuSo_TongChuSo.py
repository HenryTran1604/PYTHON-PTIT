if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        mul, sum = 1, 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    mul *= int(s[i])
            else:
                sum += int(s[i])
        print(mul, sum)
        t -= 1
