
import datetime

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email
        self.age, self._age_last_recalculated = self.recalculate_age()
        print("Age is:", self.age, "and recalculated date is:", self._age_last_recalculated)

    def recalculate_age(self):
        today = datetime.date.today()
        print("Today is:", today)
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        self.age = age
        self._age_last_recalculated = today
        return self.age, self._age_last_recalculated

    def person_age(self):
        if datetime.date.today() > self._age_last_recalculated:
            self.age, self._age_last_recalculated = self.recalculate_age()
            print("Now age is:", self.age)
        return self.age


person = Person("Jane", "Doe", datetime.date(1992, 3, 12), "No. 12 Short Street, Greenville", "555 456 0987", "jane.doe@example.com")

print(person.name)
print(person.email)
print(person.person_age())