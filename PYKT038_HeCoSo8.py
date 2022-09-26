def convert(s):
    b = 1
    res = 0
    for i in range(2, -1, -1):
        res += int(s[i]) * b
        b *= 2
    return res

if __name__ == '__main__':
    s = input()
    while len(s) % 3 != 0:
        s = '0' + s
    for i in range(0, len(s), 3):
        print(convert(s[i:i+3]), end = '')