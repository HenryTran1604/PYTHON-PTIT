import math
from sys import stdin

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def distance(self, other):
        dis = math.sqrt((self.__x - other.__x) ** 2 + (self.__y - other.__y) ** 2)
        return dis
class Triangle:
    def __init__(self, A, B, C):
        self.__A = A
        self.__B = B
        self.__C = C
    def Perimeter(self):
        d1 = self.__A.distance(self.__B)
        d2 = self.__A.distance(self.__C)
        d3 = self.__B.distance(self.__C)
        if d1 + d2 > d3 and d1 + d3 > d2 and d2 + d3 > d1:
            cv = d1 + d2 + d3
            return '{:.3f}'.format(cv)
        return 'INVALID'
if __name__ == '__main__':
    p = []
    for _ in stdin:
        p += map(float, _.split())
    pos = 1
    t = int(p[0])
    while t > 0:
        a, b, c, d, e, f = p[pos : pos+6]
        pos += 6
        tg = Triangle(Point(a, b), Point(c, d), Point(e, f))
        print(tg.Perimeter())
        t -= 1
