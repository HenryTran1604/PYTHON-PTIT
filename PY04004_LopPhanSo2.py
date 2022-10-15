import math


class PhanSo:
    def __init__(self, tu, mau):
        self.__tu = tu
        self.__mau = mau
    def toiGian(self):
        gcd = math.gcd(self.__tu, self.__mau)
        self.__tu //= gcd
        self.__mau //= gcd
    def __add__(self, other):
        tu = self.__tu * other.__mau + self.__mau * other.__tu
        mau = self.__mau * other.__mau
        res = PhanSo(tu, mau)
        res.toiGian()
        return res
    def __str__(self):
        return f'{self.__tu}/{self.__mau}'
if __name__ == '__main__':
    a, b, c, d = map(int, input().split())
    ps1, ps2 = PhanSo(a, b), PhanSo(c, d)
    ps = ps1 + ps2
    print(ps)
