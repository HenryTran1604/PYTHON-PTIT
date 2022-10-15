
class ThiSinh:
    def __init__(self, hoTen, ngaySinh, d1, d2, d3):
        self.hoTen = hoTen
        self.ngaySinh = ngaySinh
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
    def tongDiem(self):
        return self.d1 + self.d2 + self.d3
    def __str__(self):
        return self.hoTen + ' ' + self.ngaySinh + ' %.1f' % self.tongDiem()

if __name__ == '__main__':
    ts = ThiSinh(input(), input(), float(input()), float(input()), float(input()))
    print(ts)
