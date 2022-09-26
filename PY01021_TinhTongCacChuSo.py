if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        tmp = sorted(filter(lambda x : x.isalpha(), s))
        sumdigit = sum([int(x) for x in s if x.isdigit()])
        for x in tmp:
            print(x, end ='')
        print(sumdigit)

        t -= 1