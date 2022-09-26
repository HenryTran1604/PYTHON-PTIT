if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        a = [0] * 1001
        for i in range(n):
            a[int(input())] += 1
        maxval = 0
        for i in range(1, 1001):
            if a[maxval] < a[i]:
                maxval = i
        print(maxval)
        t -= 1
