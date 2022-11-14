
# Exercise #3: (10 points)
# Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is
# seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a
# maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of
# the total fare.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):

   def fare(self):
        fare_bus = self.capacity * 100
        total_fare = fare_bus + (0.1 * fare_bus)
        return total_fare

bus_obj2 = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", bus_obj2.fare())