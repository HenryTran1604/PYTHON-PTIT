if __name__ == '__main__':
    s = input()
    s = s.replace('688', ' ')
    s = s.replace('68', ' ')
    s = s.replace('6', ' ')
    if s != ' ' * len(s):
        print('NO')
    else:
        print('YES')