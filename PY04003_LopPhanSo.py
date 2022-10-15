import mailbox
import math


class PhanSo:
    def __init__(self, tu, mau):
        self.__tu = tu
        self.__mau = mau
    def toiGian(self):
        gcd = math.gcd(self.__tu, self.__mau)
        self.__tu //= gcd
        self.__mau //= gcd
    def __str__(self):
        return f'{self.__tu}/{self.__mau}'
if __name__ == '__main__':
    a, b = map(int, input().split())
    ps = PhanSo(a, b)
    ps.toiGian()
    print(ps)