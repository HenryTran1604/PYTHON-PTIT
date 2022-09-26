if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort()
        b.sort()
        check = True
        for i in range(n):
            if a[i] > b[i]:
                check = False
                break
        if check:
            print('YES')
        else:
            print('NO')
        t -= 1
