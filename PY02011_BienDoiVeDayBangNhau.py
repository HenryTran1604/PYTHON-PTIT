if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    minStep, choseValue = 10 ** 9, -1
    for i in range(n):
        step = 0
        for j in range(n):
            step += abs(a[j] - a[i])
        if step < minStep:
            minStep = step
            choseValue = a[i]
    print(minStep, choseValue)