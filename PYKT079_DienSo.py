if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        s = set(map(int, input().split()))
        minval, maxval = min(s), max(s)
        print(maxval - minval + 1 - len(s))
        t -= 1