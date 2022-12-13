if __name__ == '__main__':
    s = input()
    cnt = 0
    while len(s) > 1:
        tong = 0
        for x in s:
            tong += ord(x) - ord('0')
        s = str(tong)
        cnt += 1
    print(cnt)