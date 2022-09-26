def check(s):
    rev = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(rev[i]) - ord(rev[i-1])):
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        if check(s):
            print('YES')
        else:
            print('NO')
        t -= 1