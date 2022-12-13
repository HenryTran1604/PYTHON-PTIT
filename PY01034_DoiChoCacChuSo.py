if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = list(input())
        check = False
        st, R = [], [-1] * len(s)
        f = [-1] * 10
        pos = -1
        for i in range(len(s) - 1, -1, -1):
            for j in range(int(s[i]) - 1, -1, -1):
                if f[j] != -1:
                    pos = i
                    R[pos] = f[j]
                    break
            if pos != -1:
                break
            f[int(s[i])] = i
        if pos == -1:
            print(-1)
        else:
            s[pos], s[R[pos]] = s[R[pos]], s[pos]
            if s[0] == '0':
                print(-1)
            else:
                for x in s:
                    print(x, end='')
                print()
# 34512234567
