def count(arr, n):
    cnt = 0
    for i in range(n - 1):
        s = set()
        for j in range(i + 1, n):
            if -(arr[i] + arr[j]) in s:
                cnt += 1
            s.add(arr[j])
    return cnt


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        a = list(map(int, input().split()))
        print(count(a, n))
        t -= 1
