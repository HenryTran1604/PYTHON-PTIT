import re
if __name__ == '__main__':
    n = int(input())
    d = dict()
    while n > 0:
        s = input().lower()
        tmp = ''
        for x in s + ' ':
            if x.isalpha() or x.isdigit():
                tmp += x
            elif len(tmp):
                if tmp in d:
                    d[tmp] += 1
                else:
                    d[tmp] = 1
                tmp = ''
        n -= 1
    a = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    for x in a:
        print(x[0], x[1])