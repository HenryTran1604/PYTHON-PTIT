if __name__ == '__main__':
    prime = [True] * (10 ** 6 + 1)
    prime[0] = prime[1] = False
    for i in range(2, 10**3 + 1):
        if prime[i]:
            for j in range(i*i, 10**6 + 1, i):
                prime[j] = False
    t = int(input())
    while t > 0:
        n = int(input())
        cnt = 0
        p = prime.copy()
        for i in range(13, n, 2):
            rev = int(str(i)[::-1])
            if rev < n and i != rev and p[i] and p[rev]:
                print(i, str(i)[::-1], end = ' ')
                p[i] = p[rev] = False
        print()
        t -= 1