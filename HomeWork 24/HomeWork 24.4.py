class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def display_details(self):
        print(f"Name is: {self.name}")
        print(f"Age is: {self.get_age()}")

    def greet(self):
        print(f"Hello Everyone! {self.name}")

    def get_age(self):
        return self.__age

    def set_age(self, positive_int):
        if positive_int < 0:
            raise ValueError("Age can not be a negative number!")

        self.__age = positive_int


first_name = input("Write your Name:\t")
how_age = int(input("Write a your age:\t"))

person_1 = Person(first_name, how_age)

person_1.greet()

person_1.get_age()
person_1.set_age(how_age)
person_1.display_details()

