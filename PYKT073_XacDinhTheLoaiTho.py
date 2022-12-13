if __name__ == '__main__':
    n = int(input())
    lucBat = False
    lenTuTuyet = 0
    baiTho = []
    for i in range(n):
        s = input().split()
        if len(s) == 7:
            lenTuTuyet += 1
            if lucBat:
                baiTho.append(1)
            lucBat = False
        elif len(s) == 6:
            while lenTuTuyet and lenTuTuyet % 4 == 0:
                baiTho.append(2)
                lenTuTuyet -= 4
            lenTuTuyet = 0
            lucBat = True
    if lucBat: baiTho.append(1)
    while lenTuTuyet and lenTuTuyet % 4 == 0:
        baiTho.append(2)
        lenTuTuyet -= 4
    print(len(baiTho))
    for x in baiTho:
        print(x)