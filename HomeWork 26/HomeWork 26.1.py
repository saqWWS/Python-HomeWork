class Person:

    def __init__(self, age: int) -> None:
        self.age_is = age

    @property
    def age_is(self):
        return self.__age

    @age_is.setter
    def age_is(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must ba positive integer")
        self.__age = value


alice = Person(23)
print(alice.age_is)
