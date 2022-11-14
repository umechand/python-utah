# Week 8
# Exercise 1.1


class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name:", self.name)
        print("Cuisine type:", self.cuisine_type)

    def open_restaurant(self):
        print(self.name + " is open for business")


restaurant1 = Restaurant("paradise ", "Tacobells")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()


class Ice_Cream_Stand(Restaurant):
    def __init__(self, name, cuisine_type, flavors):
        Restaurant.__init__(self, name, cuisine_type)
        self.flavors = flavors

    def get_flavors(self):
        print(f"The flavors available at this restaurant are: {self.flavors}")


ice_cream = Ice_Cream_Stand("My Ice Cream Shoppe", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry"])
ice_cream.describe_restaurant()
ice_cream.open_restaurant()
ice_cream.get_flavors()

# Exercise 1.2

class User:
    def __init__(self, first_name, last_name, dob, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.age = age
        self.gender = gender

    def describe_user(self):
        print("First_name:", self.first_name)
        print("Last_name:", self.last_name)
        print("Dob:", self.dob)
        print("Age:", self.age)
        print("Gender:", self.gender)

    def greet_user(self):
        print(f"Good morning, {self.first_name} {self.last_name}! How are you?")


print("User1:")
u1 = User("David", "Dot", "12-03-1993", 23, "Male")
u1.describe_user()
u1.greet_user()
print("User2:")
u2 = User("Will", "Smith", "03-06-2007", 14, "Male")
u2.describe_user()
u2.greet_user()
print("User3:")
u3 = User("Lina", "Norwood", 25, "08-08-1997", "Female")
u3.describe_user()
u3.greet_user()


class Admin(User):
    def __init__(self, first_name, last_name, dob, age, gender, admin_id, privileges):
        User.__init__(self, first_name, last_name, dob, age, gender)
        self.admin_id = admin_id
        self.privileges = privileges

    def show_privileges(self):
        print("Admin id:", self.admin_id)
        print("The admin privileges are:", self.privileges)


print("Admin info:")
a1 = Admin("Braddy", "Bells", "13-09-19887", 30, "Male", "U1428821", ["can add pos", "can delete post", "can ban user"])
a1.describe_user()
a1.greet_user()
a1.show_privileges()
