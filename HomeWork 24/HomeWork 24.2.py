class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name is: {self.name}")
        print(f"Age is: {self.age}")


first_name = input("Write your Name:\t")
how_age = int(input("Write a your age:\t"))

person_1 = Person(first_name, how_age)
person_1.display_details()
