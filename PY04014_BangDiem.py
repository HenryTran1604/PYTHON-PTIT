import math


class HocSinh:
    def __init__(self, id, hoTen, d):
        self.ma = 'HS%02d' % id
        self.hoTen = hoTen
        self.d = d
    def diemTB(self):
        tong = sum(self.d) + self.d[0] + self.d[1]
        return tong / 12
    def xepHang(self):
        if self.diemTB() >= 9:
            return 'XUAT SAC'
        if self.diemTB() >= 8:
            return 'GIOI'
        if self.diemTB() >= 7:
            return 'KHA'
        if self.diemTB() >= 5:
            return 'TB'
        return 'YEU'
    def __str__(self):
        return self.ma + ' ' + self.hoTen + ' ' + str(round((self.diemTB() * 10.0) / 10.0, 1)) + ' ' + self.xepHang()
    
if __name__ == '__main__':
    l = []
    n = int(input())
    for i in range(n):
        l.append(HocSinh(i + 1, input(), [float(x) for x in input().split()]))
    l.sort(key = lambda x : -x.diemTB())
    for hs in l:
        print(hs)
