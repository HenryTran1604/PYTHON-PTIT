from decimal import Decimal
import math

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def distance(self, other):
        dis = math.sqrt((self.getX() - other.getX()) ** 2 + (self.getY() - other.getY()) ** 2);
        return '{:.4f}'.format(dis)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1