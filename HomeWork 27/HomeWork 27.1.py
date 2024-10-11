class Person:
    __slots__ = ("name", "age", "email")

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"Name is: {self.name} \nAge is: {self.age} \nEmail is: {self.email}"


person_1 = Person("Iulia", 27, "example@perform.com")

print(person_1)
