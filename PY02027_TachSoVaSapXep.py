

if __name__ == '__main__':
    a = []
    t = int(input())
    while t > 0:
        s = input()
        nums = ''
        for x in s:
            if x.isdigit():
                nums += x
            else:
                nums += ' '
        a.extend([int(x) for x in nums.split()])
        t -= 1
    a.sort()
    for x in a:
        print(x)