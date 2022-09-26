if __name__ == '__main__':
    s = input()
    cnt = 0
    res = str()
    for i in range(len(s) - 1, -1, -1):
        if cnt % 3 == 0 and i != len(s) - 1:
            res += ',' + s[i]
        else:
            res += s[i]
        cnt += 1
    print(res[::-1])
