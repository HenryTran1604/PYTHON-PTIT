if __name__ == '__main__':
    s = input()
    s = s.lower()
    if s.__contains__('.py'):
        print('yes')
    else:
        print('no')