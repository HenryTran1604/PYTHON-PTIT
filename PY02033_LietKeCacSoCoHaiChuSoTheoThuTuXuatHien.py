if __name__ == '__main__':
    s = input()
    l = len(s) if len(s) % 2 == 0 else len(s) - 1
    a, se = [], set()
    for i in range(0, l, 2):
        x = int(s[i:i+2])
        if x not in se:
            a.append(x)
            se.add(x)
    for x in a:
        print(x, end=' ')