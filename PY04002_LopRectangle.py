class Rectangle:
    def __init__(self, height, width, color):
        self.__height = height
        self.__width = width
        self.__color = color
    def perimeter(self):
        return 2*(self.__height + self.__width)
    def area(self):
        return self.__height * self.__width
    def color(self):
        return self.__color.title()

arr = input().split() 
if int(arr[0]) > 0 and int(arr[1]) > 0: 
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2]) 
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color())) 
else: 
    print('INVALID')
