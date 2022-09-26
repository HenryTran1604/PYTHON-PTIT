def check(a):
    for i in range(1, 4):
        if a[i] != a[i + 1]:
            return False
    return True

if __name__ == '__main__':
    while True:
        a = list(map(int, input().split()))
        a.insert(0, 0)
        if check(a) and a[1] == 0:
            break
        cnt = 0
        while not check(a):
            tmp = a[1]
            for i in range(1, 4):
                a[i] = abs(a[i] - a[i + 1])
            a[4] = abs(a[4] - tmp)
            cnt += 1
        print(cnt)
    