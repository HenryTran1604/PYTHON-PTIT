if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = input()
        char1, char2 = n[0], n[1]
        check = True
        if char1 == char2:
            check = False
        for i in range(2, len(n)):
            if i % 2 == 0:
                if n[i] != char1:
                    check = False
                    break
            else:
                if n[i] != char2:
                    check = False
                    break
        if check:
            print("YES")
        else:
            print("NO")
        t -= 1