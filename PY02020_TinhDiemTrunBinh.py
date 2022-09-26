if __name__ == '__main__':
    n = int(input())
    a = list(map(float, input().split()))
    maxval, minval, cnt, sum = max(a), min(a), 0, 0.0
    for i in range(n):
        if maxval != a[i] and minval != a[i]:
            sum += a[i]
            cnt += 1
    print('%.2f' % (sum / cnt))