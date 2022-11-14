
# Week8
# Exercise2.1

class Learner:
    def __init__(self):
        self.classes = []

    def enrol(self, course):
        self.classes.append(course)


class Teacher:
    def __init__(self):
        self.courses_taught = []

    def assign_teaching(self, course):
        self.courses_taught.append(course)


class Person:
    def __init__(self, name, surname, number, learner=None, teacher=None):
        self.name = name
        self.surname = surname
        self.number = number

        self.learner = learner
        self.teacher = teacher

    def enroll(self, course):
        self.learner.enroll(course)

    def assign_teaching(self, course):
        self.teacher.assign_teaching(course)


jane = Person("Jane", "Smith", "SMTJNX045", Learner(), Teacher())

jane.learner.enrol("python")
jane.teacher.assign_teaching("python")
print(jane.learner.classes)
print(jane.teacher.courses_taught)


 #Exercise2.2


class Person:
    def __init__(self, firstname, lastname):
        self.first_name = firstname
        self.last_name = lastname

    def email(self):
        return '{}.{}@email.com'.format(self.first_name, self.last_name)

    @property
    def fullName(self):
        return self.first_name + " " + self.last_name

    @fullName.setter
    def fullName(self, value):
        self.first_name = value.split(" ")[0]
        self.last_name = value.split(" ")[1]
        print("First_name:", self.first_name)
        print("Last_name:", self.last_name)


a_person = Person("Steve", "Austin")
a_person.fullName = "Thor Odinson"
print(a_person.fullName)
"""The object prints out the new assigned value."""
