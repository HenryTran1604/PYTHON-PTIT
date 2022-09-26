def check(d, m):
    if m == 3:
        if d < 21: return 12
        else: return 1
    if m == 4:
        if d < 20: return 1
        else: return 2
    if m == 5:
        if d < 21: return 2
        else: return 3
    if m == 6:
        if d < 21: return 3
        else: return 4
    if m == 7:
        if d < 23: return 4
        else: return 5
    if m == 8:
        if d < 23: return 5
        else: return 6
    if m == 9:
        if d < 23: return 6
        else: return 7
    if m == 10:
        if d < 23: return 7
        else: return 8
    if m == 11:
        if d < 23: return 8
        else: return 9
    if m == 12:
        if d < 22: return 9
        else: return 10
    if m == 1:
        if d < 20: return 10
        else: return 11
    if m == 2:
        if d < 19: return 11
    return 12

if __name__ == '__main__':
    t = int(input())
    cung = {1: 'Bach Duong',
            2: 'Kim Nguu',
            3: 'Song Tu',
            4: 'Cu Giai',
            5: 'Su Tu',
            6: 'Xu Nu',
            7: 'Thien Binh',
            8: 'Thien Yet',
            9: 'Nhan Ma',
            10: 'Ma Ket',
            11: 'Bao Binh',
            12: 'Song Ngu'}
    while t > 0:
        d, m = map(int, input().split())
        print(cung[check(d, m)])

        t -= 1