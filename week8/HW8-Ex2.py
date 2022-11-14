

#2Exercise #2:

# Using the code below, create a Bus object that will inherit all of the variables and
# methods of the Vehicle class and display it.

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

bus_obj1 = Bus("School Volvo", 180, 12)
print("Vehicle Name:", bus_obj1.name, "Speed:", bus_obj1.max_speed, "Mileage:", bus_obj1.mileage)

