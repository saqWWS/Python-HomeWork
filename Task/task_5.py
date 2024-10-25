import abc


class Courses(abc.ABC):
    def __init__(self, name, instructor, content):
        self.name = name
        self.instructor = instructor
        self.content = content


class Undergraduate(Courses):
    def __init__(self, name, instructor, content=None):
        super().__init__(name, instructor, content)

    def __repr__(self):
        return f"{self.name}"


undergraduate_1 = Undergraduate("Biology", "Bob")
undergraduate_2 = Undergraduate("Chemistry", "Michel")


class Graduate(Courses):
    def __init__(self, name, instructor, content=None):
        super().__init__(name, instructor, content)

    def __repr__(self):
        return f"{self.name}"


graduate_1 = Graduate("English", "Prof1")
graduate_2 = Graduate("Finance", "Prof2")


class Students:
    def __init__(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information
        self.course = []
        self.assignments = []

    def student_info(self):
        return f"Name: {self.name} Cont. info: {self.contact_information}"

    def __repr__(self):
        return f"{self.name}"


student_1 = Students("Ann", "@ann@.ex")
student_2 = Students("Alice", "alice@.ex")
student_3 = Students("Razvan", "raz@.ex")
student_4 = Students("Ioana", "ion@.ex")


class Professors:
    def __init__(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information
        self.courses = []

    def create_course(self, value):
        self.courses.append(value)

    def show_course(self):
        return f" Courses: {self.courses}"

    def __repr__(self):
        return f"{self.name}"


professor_1 = Professors("Bob", "bob@.ex")
professor_2 = Professors("Iulia", "iuli@.ex")
professor_3 = Professors("Robert", "rob@.ex")
professor_4 = Professors("Aizenberg", "berg@.ex")


class University:
    def __init__(self):
        self.new_course = []

    def add_new_course(self, lesson: 'Undergraduate, Graduate', professor: 'Professors', students: [Students]):
        self.new_course.extend([lesson, professor, students])

    def display_courses(self):
        for _ in self.new_course:
            return f" Course name: {self.new_course[0]} \n Professor: {self.new_course[1]} \n Students: {self.new_course}"


university = University()
university.add_new_course(undergraduate_1, professor_4, [student_1, student_2])
print(university.display_courses())
