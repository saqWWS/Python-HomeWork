import abc
import math


class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        ...


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Square(Shape):
    def __init__(self, length: float):
        self.length = length

    def area(self):
        return self.length * self.length


circle = Circle(4)
print(f"Circle area is : {circle.area()}")

square = Square(4)
print(f"Square area: {square.area()}")


# GOOD VERSION


class Shape:
    """
    When we want to add a new action, we have to change our current class,
    which is not so efficient, and over time it can get overloaded and produce bad code,
    and now we have another class that will inherit from our super class,
    which in turn is abstract, will allow you to implement more functionality without
    touching the inner classes, a new method in a new class
    """

    def __init__(self, type_of_operation: str, number):
        self.type_of_operation = type_of_operation
        self.number = number

    def area(self):
        if self.type_of_operation == "circle":
            return math.pi * self.number ** 2
        elif self.type_of_operation == "square":
            return self.number * self.number


circle = Shape("circle", 11)
print(f"Circle area: {circle.area()}")

square = Shape("square", 3)
print(f"Square area: {square.area()}")

# BAD VERSION
