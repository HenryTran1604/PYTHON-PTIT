if __name__ == '__main__':
    prime = [True] * (10 ** 6 + 1)
    prime[0] = prime[1] = False
    for i in range(2, 10**3 + 1):
        if prime[i]:
            for j in range(i*i, 10**6 + 1, i):
                prime[j] = False
    cnt = [0] * (10 ** 6 + 1)
    for i in range(6, 10 ** 6 + 1):
        if (prime[i] and prime[i - 2] and prime[i - 6]) or (prime[i] and prime[i - 4] and prime[i - 6]):
            cnt[i] = cnt[i - 1] + 1
        else:
            cnt[i] = cnt[i - 1]
    t = int(input())
    while t > 0:
        n = int(input())
        print(cnt[n - 1])
        t -= 1