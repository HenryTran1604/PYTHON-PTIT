def isValid(s):
    if(len(s.split('.')) != 4):
        return False
    try:
        for x in s.split('.'):
            d = int(x)
            if d > 255 or d < 0:
                return False
    except:
        return False
    return True

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        if(isValid(input())):
            print('YES')
        else:
            print('NO')
    