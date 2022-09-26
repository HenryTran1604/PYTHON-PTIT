if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        for i in range(0, len(s) - 1, 2):
            a = s[i] * int(s[i + 1])
            print(a, end = '')
        print()
        t -= 1