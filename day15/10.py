import os
# property.delete装饰器

class Square:
    def __init__(self, width: float):
        self.__width = width
        self.__area = None
    
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value: float):
        if value < 0:
            raise ValueError("width must be positive")
        self.__width = value
    
    @property
    def area(self):
        if self.__area is None:
            self.__area = self.__width * self.__width
        return self.__area
    
    @area.deleter
    def area(self):
        print("Deleting area property")
        self.__area = None  # 清除缓存

def main():
    square = Square(5)
    print(square.area)
    square.width = 6
    del square.area  # 删除area缓存
    print(square.area)

if __name__ == '__main__':
    main()