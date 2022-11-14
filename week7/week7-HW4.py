
#Exercise4

import datetime

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age


person = Person(

    "Jane",

    "Doe",

    datetime.date(1992, 3, 12), # year, month, day

    "No. 12 Short Street, Greenville",

    "555 456 0987",

    "jane.doe@example.com"

)

print(person.name)
print(person.email)
print(person.age())
print(dir(person))
print(dir(Person))

# Question 1
print(person.__str__())
print(str(person))
# Both _str_ and str() function returns the same output, i.e., the string representation of the instance."""

# Question 2
print(type(person))
# <class '_main_.Person'>

# Question 3
print(type(Person))
# <class 'type'>

# Question 4
print(vars(person))