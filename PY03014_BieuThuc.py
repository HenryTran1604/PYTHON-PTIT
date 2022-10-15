if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        st, d = [], 1
        for x in s:
            if x == '(':
                print(d, end = ' ')
                st.append(d)
                d += 1
            elif x == ')':
                print(st[-1], end = ' ')
                st.pop()
        print()
        t -= 1