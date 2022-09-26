if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        if len(s) == 1:
            print(s)
        else:
            res = ''
            carry = 0
            for i in range(len(s) - 1, 0, -1):
                if int(s[i]) + carry >= 5:
                    carry = 1
                else:
                    carry = 0
                res += '0'
            if int(s[0]) + carry == 10:
                res += '01'
            else:
                res += str(int(s[0]) + carry)
            print(res[::-1])
        t -= 1
