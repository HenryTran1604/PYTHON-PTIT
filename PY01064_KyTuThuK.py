if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n, k = map(int, input().split())
        if k % 2 == 1:
            print('A')
        else:
            cnt = 0
            while k % 2 == 0:
                k >>= 1
                cnt += 1
            print(chr(65 + cnt))
        t -= 1