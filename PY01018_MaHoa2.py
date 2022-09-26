if __name__ == '__main__':
    P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    while True:
        try:
            k, s= input().split()
            k = int(k)
            res = str()
            for i in range(len(s)):
                res += P[(P.index(s[i]) + k) % 28]
            print(res[::-1])
        except:
            break
