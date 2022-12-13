if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        a = []
        for i in range(n):
            a.append(int(input()))
        minv, maxv = 10 ** 100 + 1, -1
        for x in a:
            minv = min(minv, x)
            maxv = max(maxv, x)
        if minv == maxv:
            print("BANG NHAU")
        else:
            print(minv, maxv)