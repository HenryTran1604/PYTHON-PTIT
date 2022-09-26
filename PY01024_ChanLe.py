def check(s):
    sum = int(s[0])
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != 2:
            return False
        sum += int(s[i])
    return sum % 10 == 0

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        if check(s):
            print("YES")
        else:
            print("NO")
        t -= 1
