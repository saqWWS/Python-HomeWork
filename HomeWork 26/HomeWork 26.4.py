class Descriptor:

    def __get__(self, instance, owner=None):
        return instance.val

    def __set__(self, instance, value):
        if not 0 < value < 100:
            raise ValueError

        instance.val = value


class Student:
    score = Descriptor()


student_1 = Student()
student_2 = Student()

student_1.score = 36
student_2.score = 45

print(f"Student 'Student_1's grade point average is: {student_1.score}")
print(f"Student 'Student_2's grade point average is: {student_2.score}")
