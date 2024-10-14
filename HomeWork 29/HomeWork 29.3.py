import abc


class Bird(abc.ABC):
    def __init__(self, food: str, name):
        self.name = name
        self.food = food

    def fly(self):
        ...

    def eat(self):
        ...


class Phoenix(Bird):
    def __init__(self, name: str, food: str):
        super().__init__(name, food)
        self.name = name
        self.food = food

    def fly(self):
        return f" {self.name} can flay"

    def eat(self):
        return f" {self.name} eats {self.food}.\n"


class Hummingbird(Bird):
    def __init__(self, name: str, food: str):
        super().__init__(name, food)
        self.name = name
        self.food = food

    def fly(self):
        return f" {self.name} can flay."

    def eat(self):
        return f" {self.name} eats {self.food}."


phoenix = Phoenix("Phoenix", "fruit")

print(phoenix.fly())
print(phoenix.eat())

hummingbird = Hummingbird("Hummingbird", "spider")

print(hummingbird.fly())
print(hummingbird.eat())


# GOOD VERSION

class Animal(abc.ABC):
    """
    In this way, we break the law, if the offspring should imitate the behaviour of the parent,
    we cannot say that the phoenix and the tiger have the same behaviour,
    the phoenix can fly, but the tiger does not have this ability, they can run.
    but not all fly. the pattern is very simply painted, but simpler for further in-depth studies.
    """

    def __init__(self, name: str, food: str):
        self.name = name
        self.food = food

    def fly(self):
        ...

    def eat(self):
        ...

    def run(self):
        ...


class Phoenix(Animal):
    def __init__(self, name: str, food: str):
        super().__init__(name, food)
        self.name = name
        self.food = food

    def fly(self):
        return f" {self.name} can flay."

    def run(self):
        return f" {self.name} can run."

    def eat(self):
        return f" {self.name} eats {self.food}.\n"


class Tiger(Animal):
    def __init__(self, name: str, food: str):
        super().__init__(name, food)
        self.name = name
        self.food = food

    """Tiger can't fly"""

    def run(self):
        return f" {self.name} can run."

    def eat(self):
        return f" {self.name} eats {self.food}.\n"


phoenix = Phoenix("Phoenix", "fruit")

print(phoenix.fly())
print(phoenix.run())
print(phoenix.eat())

tiger = Tiger("Pantera", "meat")

print(tiger.run())
print(tiger.eat())

# BAD VERSION
