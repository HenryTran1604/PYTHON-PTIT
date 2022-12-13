if __name__ == '__main__':
    s = input()
    l = len(s) if len(s) % 2 == 0 else len(s) - 1
    se = set()
    for i in range(0, l, 2):
        se.add(int(s[i:i+2]))
    for x in sorted(se):
        print(x, end=' ')