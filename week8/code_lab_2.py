# Week 8
# Code along 2

# composition lab

class Student:
    def __init__(self):
        self.classes = []

    def enroll(self, course):
        self.classes.append(course)

    def schedule(self):
        return self.classes


class Teacher:
    def __init__(self):
        self.courses_taught = []

    def assign_teaching(self, course):
        self.courses_taught.append(course)

    def schedule(self):
        return self.courses_taught


class Person:
    def __init__(self, first_name, last_name, UNID, student=None, teacher=None):
        self._first_name = first_name
        self._last_name = last_name
        self.student = student
        self.teacher = teacher
        self.UNID = UNID

    def enroll(self, course):
        self.student.enroll(course)

    def assign_teaching(self, course):
        self.teacher.assign_teaching(course)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value


person = Person("John", "Smith", "u1428821", Student(), Teacher())
person.enroll("Python")
person.enroll("Economics")
person.assign_teaching("Communications")
person.assign_teaching("Java")
print(person.student.schedule())
print(person.teacher.schedule())

person.last_name = "indla"
person.first_name = "umesh"
print(person.last_name)
