if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = input()
        dau = n[0] + n[1]
        cuoi = n[len(n) - 2] + n[len(n) - 1]
        if dau == cuoi:
            print("YES")
        else:
            print("NO")
        t -= 1
