n = 0
def Try(s, cnt2, cnt3, cnt5, cnt7):
    if len(s) == n:
        if(s[-1] != '2' and cnt2 and cnt3 and cnt5 and cnt7):
            print(s)
        return
    Try(s + '2', cnt2 + 1, cnt3, cnt5, cnt7)
    Try(s + '3', cnt2, cnt3 + 1, cnt5, cnt7)
    Try(s + '5', cnt2, cnt3, cnt5 + 1, cnt7)
    Try(s + '7', cnt2, cnt3, cnt5, cnt7 + 1)
if __name__ == '__main__':
    tmp = int(input())
    for i in range(4, tmp + 1):
        n = i
        Try('', 0, 0, 0, 0)