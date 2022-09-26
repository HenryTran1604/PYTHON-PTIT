if __name__ == '__main__':
    n = int(input())
    se = set()
    while n > 0:
        se.add(input())
        n -= 1
    print(len(se))
