if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = list(input())
        check = False
        st, R = [], [0] * len(s)
        for i in range(len(s) - 1, -1, -1):
            while len(st) and s[st[-1]] >= s[i]:
                st.pop()
            if len(st) == 0:
                R[i] = -1
            else:
                pos = st[-1]
                if not (i == 0 and s[pos] == '0'):
                    print(i, pos)
                    s[i], s[pos] = s[pos], s[i]
                    check = True
                    break
            st.append(i)
        print(s, check)
# 34512234567
