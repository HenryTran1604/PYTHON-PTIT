if __name__ == '__main__':
    t = int(input())
    while t > 0:
        par = input()
        child = input()
        print(par.count(child))
        t -= 1