class Employer:
    def __init__(self, employee_id, name, salary):
        self.__employee_id = employee_id
        self.__name = name
        self.__salary = salary

    def get_name_id_salary(self):
        print(f" Name is: {self.__name}\n ID: {self.__employee_id}\n Salary is: {self.__salary}")

    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__employee_id = id

    def set_salary(self, positive_int):
        if positive_int < 0:
            raise ValueError("Salary can not be a negative number!")
        self.__salary = positive_int


employer_1 = Employer(32, "Bob", 350000)
employer_1.get_name_id_salary()
print()
employer_1.set_name("Ioana")
employer_1.set_id(17)
employer_1.set_salary(375000)
employer_1.get_name_id_salary()
