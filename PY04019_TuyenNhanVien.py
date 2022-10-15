class ThiSinh:
    def __init__(self, id, hoTen, diemLyThuyet, diemThucHanh):
        self.ma = 'TS0' + str(id)
        self.hoTen = hoTen
        self.diemLyThuyet = diemLyThuyet
        if diemLyThuyet > 10:
            self.diemLyThuyet = diemLyThuyet / 10
        self.diemThucHanh = diemThucHanh
        if diemThucHanh > 10:
            self.diemThucHanh = diemThucHanh / 10
    def diemTB(self):
        return (self.diemLyThuyet + self.diemThucHanh) /2
    def xepLoai(self):
        if self.diemTB() < 5:
            return 'TRUOT'
        if self.diemTB() < 8:
            return 'CAN NHAC'
        if self.diemTB() <= 9.5:
            return 'DAT'
        return 'XUAT SAC'
    def __str__(self):
        return self.ma + ' ' + self.hoTen + ' ' + '%.2f' % self.diemTB() + ' ' + self.xepLoai()

if __name__ == '__main__':
    a = []
    n = int(input())
    for i in range(n):
        a.append(ThiSinh(i + 1, input(), float(input()), float(input())))
    a.sort(key = lambda x : -x.diemTB())
    for x in a:
        print(x)

