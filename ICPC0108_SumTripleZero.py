def count(arr, n):
    cnt = 0
    s = set()
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            tmp = a[i] + a[j]



if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        a = list(map(int, input().split()))
        print(count(a, n))
        t -= 1
