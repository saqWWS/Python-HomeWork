from numbers import Real


class Rectangle:
    def __init__(self, width: 'Real', height: 'Real'):
        self.area = width
        self.perimeter = height

    @property
    def area(self):
        area = self.__width * self.__height
        return f"Are is : {area}"

    @area.setter
    def area(self, value):
        if value < 0:
            raise ValueError("Mast be positive number:!")
        self.__width = value

    @property
    def perimeter(self):
        perimeter = 2 * (self.__width * self.__height)
        return f"Perimeter is : {perimeter}"

    @perimeter.setter
    def perimeter(self, value):
        if value < 0:
            raise ValueError("Mast be positive number:!")
        self.__height = value


rectangle = Rectangle(4, 5)
rectangle.area = 4
rectangle.perimeter = 4

print(rectangle.area)
print(rectangle.perimeter)
