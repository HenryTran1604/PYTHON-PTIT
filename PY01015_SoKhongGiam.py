def check(s):
    for i in range(1, len(s)):
        if s[i] < s[i-1]:
            return False;
    return True


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        if check(s):
            print("YES")
        else:
            print("NO")
        t -= 1