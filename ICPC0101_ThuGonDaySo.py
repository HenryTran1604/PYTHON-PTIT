if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    st = list()
    for i in range(n):
        if len(st) == 0:
            st.append(a[i])
        else:
            top = st[-1]
            if (top + a[i]) % 2 == 0:
                del st[-1]
            else:
                st.append(a[i])
    print(len(st))