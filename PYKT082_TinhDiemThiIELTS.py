def calc(n):
    if n >= 39:
        return 9
    if n >= 37:
        return 8.5
    if n >= 35:
        return 8
    if n >= 33:
        return 7.5
    if n >= 30:
        return 7
    if n >= 27:
        return 6.5
    if n >= 23:
        return 6
    if n >= 20:
        return 5.5
    if n >= 16:
        return 5
    if n >= 13:
        return 4.5
    if n >= 10:
        return 4
    if n >= 7:
        return 3.5
    if n >= 5:
        return 3
    if n >= 3:
        return 2.5
       

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        a, b, c, d = map(float, input().split())
        s = (calc(a) + calc(b) + c + d) / 4
        if s - int(s) >= 0.75:
            s = int(s) + 1
        elif s - int(s) >= 0.25:
            s = int(s) + 0.5
        else:
            s = int(s)
        print('%.1f' % s)
        t -= 1