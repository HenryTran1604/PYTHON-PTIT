if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    f = [0] * 30001
    for x in a:
        f[x] = 1
    for i in range(1, 30001):
        if f[i] == 0:
            print(i)
            break
