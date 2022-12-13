def chuanHoa(s):
    a = s.split()
    return ' '.join(a)

class ThiSinh:
    def __init__(self, i, hoTen, diemThi, danToc, khuVuc):
        self.maThiSinh = 'TS%02d'%i
        self.hoTen = chuanHoa(hoTen).title()
        self.diemThi = diemThi
        self.danToc = danToc
        self.khuVuc = khuVuc
    def diemUuTien(self):
        tong = 0
        if self.khuVuc == '1':
            tong += 1.5
        elif self.khuVuc == '2':
            tong += 1
        if self.danToc != 'Kinh':
            tong += 1.5
        return tong
    def tongDiem(self):
        return self.diemThi + self.diemUuTien()
    def trangThai(self):
        if self.tongDiem() >= 20.5:
            return 'Do'
        return 'Truot'
    def __str__(self):
        return self.maThiSinh + " " + self.hoTen + ' ' + '%.1f' % self.tongDiem() + ' ' + self.trangThai()

if __name__ == '__main__':
    a = []
    n = int(input())
    for i in range(1, n + 1):
        a.append(ThiSinh(i, input(), float(input()), input(), input()))
    a.sort(key=lambda x : (-x.tongDiem(), x.maThiSinh))
    for x in a:
        print(x)