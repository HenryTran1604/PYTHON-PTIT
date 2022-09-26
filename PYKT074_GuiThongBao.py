if __name__ == '__main__':
    t = int(input())
    while t > 0:
        mess = input()
        res = mess[:100]
        tmp1, tmp2 = res.split(), mess.split()
        if tmp1[-1] == tmp2[len(tmp1) - 1]:
            print(res)
        else:
            pos = 99
            while res[pos] != ' ':
                pos -= 1
            print(res[:pos])

        t -= 1
