

if __name__ == '__main__':
    s = input()
    n = int(s)
    while n >= 10:
        n1, n2 = int(s[:len(s) // 2]), int(s[len(s)//2:])
        n = n1 + n2
        s = str(n)
        print(s)
