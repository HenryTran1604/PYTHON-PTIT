class KhachHang:
    def __init__(self, id, hoTen, chiSoDau, chiSoCuoi):
        self.ma = 'KH%02d' % id
        self.hoTen = hoTen
        self.chiSoDau = chiSoDau
        self.chiSoCuoi = chiSoCuoi
    def tongTien(self):
        s = self.chiSoCuoi - self.chiSoDau
        if s <= 50:
            return s * 100 * 1.02
        if s <= 100:
            return (5000 + (s - 50) * 150) * 1.03
        return (12500 + (s - 100) * 200) * 1.05
    def __str__(self):
        return self.ma + " " + self.hoTen + " " + str(round(self.tongTien()))
    
if __name__ == '__main__':
    a = []
    n = int(input())
    for i in range(n):
        a.append(KhachHang(i + 1, input(), int(input()), int(input())))

    a.sort(key = lambda x : -x.tongTien())
    for x in a:
        print(x)
