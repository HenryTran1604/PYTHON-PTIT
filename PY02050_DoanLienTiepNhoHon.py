

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        a = list(map(int, input().split()))
        l, st = [0] * n, list()
        for i in range(n):
            while len(st) != 0 and a[i] >= a[st[-1]]:
                st.pop()
            if(len(st) == 0):
                l[i] = i + 1
            else:
                l[i] = i - st[-1]
            st.append(i)
        for x in l:
            print(x, end = ' ')
        print()
        t -= 1