if __name__ == '__main__':
    n, m = map(int, input().split())
    a = sorted(set(map(int, input().split())))
    b = sorted(set(map(int, input().split())))
    if a == b:
        print('YES')
    else:
        print('NO')