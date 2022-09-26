from re import findall
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        a = [int(x) for x in input().split()]
        # min1, min2, min3 = 10 ** 8 + 1, 10 ** 8 + 1, 10 ** 8 + 1
        # for i in range(n):
        #     if as[i] < min1:
        #         min3 = min2
        #         min2 = min1
        #         min1 = a[i]
        #     elif a[i] < min2:
        #         min3 = min2
        #         min2 = a[i]
        #     elif a[i] < min3:
        #         min3 = a[i]
        # print(min1 + min2 + min3)
        t -= 1
    