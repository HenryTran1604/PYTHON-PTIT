if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        rev = s[::-1]
        check = True
        for i in range(1, len(s)//2+1):
            if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(rev[i]) - ord(rev[i - 1])):
                check = False
                break;
        if check:
            print("YES")
        else:
            print("NO")
        t -= 1