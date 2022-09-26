def Try(s, l, cnta, cntb, cntc):
    if(len(s) == l):
        if cnta > 0 and cnta <= cntb and cntb <= cntc:
            print(s)
        return
    Try(s + 'A', l, cnta + 1, cntb, cntc)
    Try(s + 'B', l, cnta, cntb + 1, cntc)
    Try(s + 'C', l, cnta, cntb, cntc + 1)
    


if __name__ == '__main__':
    n = int(input())
    for i in range(3, n + 1):
        Try('', i, 0, 0, 0)