def check(s):
    check = 1
    for i in range(1, len(s)):
        if ord(s[i]) < ord(s[i - 1]):
            check -= 1
        elif ord(s[i]) > ord(s[i - 1]):
            if check < 0:
                return False
        else:
            return False
    return check != 1

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        if check(s):
            print("YES")
        else:
            print("NO")
        t -= 1
