#HW8

#Exercise #1
# 1. What are the parent and child classes here?
#Ans: The parent class is Spell. The child classes are Accio and Confundo.

# 2. What does the code print out? (Try figuring it out without running it in Python)
#Ans:
    # Accio
    # Summoning Charm Accio
    # No description
    # Confundus Charm Confundo
    # Causes the victim to become confused and befuddled.

# 3. Which get description method is called when ‘study spell(Confundo())’ is executed? Why?
#Ans:
# The method inside the Confundo class is called because methods in the child class override those in the
# parent class if they happen to exist in both the classes.

# 4. What do we need to do so that ‘print Accio()’ will print the appropriate description
# (‘This charm summons an object to the caster, potentially over a significant distance’)?
# Write down the code that we need to add and/or change.

class Spell:
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + " " + self.incantation + "\n" + self.get_description()

    def get_description(self):
        return "No description"

    def execute(self):
        print(self.incantation)

class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, "Accio", "Summoning Charm")

    def get_description(self):
	    return 'This charm summons an object to the caster, potentially over a significant distance'

    def __str__(self):
        return self.name + " " + self.incantation + "\n" + self.get_description()

class Confundo(Spell):

    def __init__(self):
        Spell.__init__(self, "Confundo", "Confundus Charm")

    def  get_description(self):
        return "Causes the victim to become confused and befuddled."

def study_spell(spell):
        print(spell)

spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())

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


# Exercise #4: (10 points)
# Create a class called Numbers, which has a single class attribute called MULTIPLIER,
# and a constructor which takes the parameters x and y (these should all be numbers).

# 1. Write a method called add which returns the sum of the attributes x and y.
# 2. Write a class method called multiply, which takes a single number parameter aand returns
# the product of a and MULTIPLIER.
# 3. Write a static method called subtract, which takes two number parameters, b and c, and returns b - c.
# 4. Write a method called value which returns a tuple containing the values of x and y.
# Make this method into a property, and write a setter and a deleter for manipulating the values of x and y.

class Numbers:
    MULTIPLIER = 4

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    @classmethod
    def multiply(self, a):
        return self.MULTIPLIER * a

    @staticmethod
    def subtract(b, c):
        return b - c

    @property
    def value(self):
        return (self.x, self.y)

    def setX(self, value):
        self.x = value
    def deleteX(self):
        del self.x

    def setY(self, value):
        self.y = value
    def deleteY(self):
        del self.y

# testing the above class.
num_obj = Numbers(3,7)
print(num_obj.add())
print(num_obj.multiply(3))
print(num_obj.subtract(4, 9))
print(num_obj.value)

num_obj.setX(2)
num_obj.setY(6)
print(num_obj.value)

num_obj.deleteX()
num_obj.deleteY()

# Exercise #5 “Abstract classes” (10 points)
# Part 1:

class Box:
    def add(self, *items):
        raise NotImplementedError()

    def empty(self):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class ListBox(Box):
    def __init__(self):
        self._items = []

    def add(self, *items):
        self._items.extend(items)

    def empty(self):
        items = self._items
        self._items = []
        return items

    def count(self):
        return len(self._items)

class DictBox(Box):
    def __init__(self):
        self._items = {}

    def add(self, *items):
        self._items.update(dict((i.name, i) for i in items))

    def empty(self):
        items = list(self._items.values())
        self._items = {}
        return items

    def count(self):
        return len(self._items)

# Part 2:

def repack_boxes(*boxes):
    items = []

    for box in boxes:
        items.extend(box.empty())

    while items:
        for box in boxes:
            try:
                box.add(items.pop())
            except IndexError:
                break

box1 = ListBox()
for i in range(20):
    item = Item(str(i), i)
    box1.add(item)

box2 = ListBox()
for i in range(9):
    item = Item(str(i), i)
    box2.add(item)

box3 = DictBox()
for i in range(5):
    item = Item(str(i), i)
    box3.add(item)

repack_boxes(box1, box2, box3)

print(box1.count())
print(box2.count())
print(box3.count())
