class Student:

    def __init__(self, name, roll_number):
        self.__name = name
        self.__roll_number = roll_number
        self.__grades = []

    def add_grades(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)

    def calculate_grade(self):
        if len(self.__grades) == 0:
            return 0
        return sum(self.__grades) / len(self.__grades)

    def display_details(self):
        print("Student name is:", self.__name)
        print("Roll number:", self.__roll_number)
        print("List of grades student:", self.__grades)
        print(f"Average grade, {self.calculate_grade():.2f}")


student_1 = Student("Mark", 9)
student_1.add_grades(68)
student_1.add_grades(90)
student_1.add_grades(78)
student_1.add_grades(101)
student_1.add_grades(92)

student_1.display_details()

student_2 = Student("Iulia", 32)
student_2.add_grades(78)
student_2.add_grades(86)
student_2.add_grades(54)

student_2.display_details()
