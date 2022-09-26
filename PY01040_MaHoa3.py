def convert(s):
    sum = 0
    for x in s:
        sum += ord(x) - 65
    res = ''
    for x in s:
        res += chr(65 + (ord(x) - 65 + sum) % 26)
    return res

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        p1, p2 = s[ : len(s) // 2], s[len(s) // 2 : ]
        p1, p2 = convert(p1), convert(p2)
        res = ''
        for i in range(len(p1)):
            res += chr(65 + (ord(p1[i]) + ord(p2[i]) - 130) % 26)
        print(res)
        t -= 1
