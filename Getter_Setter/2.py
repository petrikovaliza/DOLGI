class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, width):
        if width >= 0:
            self.__width = width
        else:
            print("Width cannot be negative")

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if height >= 0:
            self.__height = height
        else:
            print("Height cannot be negative")

    def perimeter(self):
        return 2 * (self.get_width() + self.get_height())


r = Rectangle(5, 3)
print(r.perimeter())

r.set_width(10)
r.set_height(4)
print(r.perimeter())

r.set_width(-2)
print(r.perimeter())