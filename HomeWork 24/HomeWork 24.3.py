class Person:
    name = None
    age = None

    def display_details(self):
        print(f"Name is: {self.name}")
        print(f"Age: {self.age}")

    def greet(self):
        print(f"Hello Everyone! {self.name}")


first_name = input("Write your Name:\t")
how_age = int(input("Write a your age:\t"))

person_1 = Person()
person_1.name, person_1.age = first_name, how_age
person_1.display_details()
person_1.greet()
