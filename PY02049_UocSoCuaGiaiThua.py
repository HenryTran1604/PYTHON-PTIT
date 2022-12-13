t = int(input())
while t > 0:
    n, p = map(int, input().split())
    cnt, x = 0, p
    while x <= n:
        cnt += n // x
        x *= p
    print(cnt)
    t -= 1
