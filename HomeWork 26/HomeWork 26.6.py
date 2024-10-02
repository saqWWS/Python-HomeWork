class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def __get__(self, instance, owner):
        return instance.val

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value < 0 or value > 1250:
            raise ValueError("The salary must be an int or float between 0 and 1250.")
        instance.val = value


class Worker:
    emp = Employee(salary=None)


try:
    salary_1 = Worker()
    salary_2 = Worker()
    salary_1.emp = 850
    print(f"Salary is: {salary_1.emp}$")
    salary_2.emp = 1300
    print(f"Salary is: {salary_2.emp}$")

except ValueError as e:
    print(f"Exception caught: {e}")
