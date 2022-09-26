if __name__ == '__main__':
    s1 = input()
    s2 = input()
    i = int(input())
    res = s1[:i-1] + s2 + s1[i-1:]
    print(res)
