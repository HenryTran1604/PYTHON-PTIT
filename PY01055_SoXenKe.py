def check(s):
    if len(s) % 2 == 0 or s[0] == s[1]:
        return False
    for i in range(0, len(s), 2):
        if s[i] != s[0]:
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