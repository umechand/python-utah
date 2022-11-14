# Week8
# HW8
import math

print("Exercise 1")


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


class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, "Confundo", "Confundus Charm")

    def get_description(self):
        return "Causes the victim to become confused and befuddled."


def study_spell(spell):
    print(spell)


spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())


"""1.) What are the parent and child classes here?
Ans: Parent class is the Spell class whereas the child classes are Accio and Confundo.

2.) What does the code print out?
Ans: The code prints out the following lines:
Accio
Summoning Charm Accio
No description
Confundus Charm Confundo
Causes the victim to become confused and befuddled.

3.) Which get description method is called when ‘study spell(Confundo())’ is executed? Why?
Ans: The get_description() method which is defined in the Confundo class is called because this get_description()
method overrides the get_description() method present in the parent class.

4.)What do we need to do so that ‘print Accio()’ will print the appropriate description
(‘This charm summons an object to the caster, potentially over a significant distance’)?
 Write down the code that we need to add and/or change.
Ans: To print the appropriate description when 'print(Accio()) is called, we need to define a get_description() method
in Accio class which will override the get_description() method of the parent class. The updated codepiece is:


 class Accio(Spell):
    def _init_(self):
        Spell._init_(self, "Accio", "Summoning Charm")
    def get_description(self):
        return "This charm summons an object to the caster, potentially over a significant distance"

So the updated code is below:
"""


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

    # Added override method here
    def get_description(self):
        return "This charm summons an object to the caster, potentially over a significant distance"


class Confundo(Spell):

    def __init__(self):
        Spell.__init__(self, "Confundo", "Confundus Charm")

    def get_description(self):
        return "Causes the victim to become confused and befuddled."


def study_spell(spell):
    print(spell)


spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())

print("\nExercise 2")


class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        Vehicle.__init__(self, name, max_speed, mileage)

    def vehicle_details(self):
        print(f"Vehicle Name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage}")


bus = Bus("School Volve", 180, 12)
bus.vehicle_details()

print("\nExercise 3")


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def __init__(self,  name, mileage, capacity):
        Vehicle.__init__(self, name, mileage, capacity)

    def vehicle_details(self):
        print(f"Vehicle Name: {self.name} Mileage: {self.mileage} Capacity: {self.capacity}")

    def fare(self):
        total_fare = self.capacity * 100
        final_amount = total_fare + 0.1 * total_fare
        return final_amount


School_bus = Bus("School Volvo", 12, 50)
School_bus.vehicle_details()
print("Total Bus fare is:", School_bus.fare())


print("\nExercise 4")


class Numbers:
    # TODO: create a class attribute called MULTIPLIER

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.multiplier = 5

    def add(self):
        return self.x + self.y

    def multiply(self, a):
        return self.multiplier * a

    @staticmethod
    def subtract(b, c):
        return b - c

    @property
    def value(self):
        return self.x, self.y

    @value.setter
    def value(self, val1):
        self.x = val1

    @value.deleter
    def value(self):
        print(self.y, "is deleted.")
        del self.y


# test the class.
num = Numbers(5, 6)
print(num.add())
print(num.multiply(2))
print(num.subtract(4, 4))
num.x = 8
num.y = 7
del num.y

print("x:", num.x)
#print("y:", num.y)


# test the class.
num = Numbers(5, 6)
print(num.add())
print(num.multiply(2))
print(num.subtract(4, 4))


print("\nExercise#5")

# PART -1
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
    # TODO: create a new variable called items and set it equal to _items.
    # TODO: set the private variable _items to a new list, this will make _items empty again.
    # TODO: return the new items variable.

    def count(self):
        return len(self._items)
        # TODO: Create a return statement to return the length of the items.


class DictBox(Box):
    def __init__(self):
        self._items = {}

    def add(self, *items):
        self._items.update(dict((i, i) for i in items))

    def empty(self):
        items = list(self._items.values())
        self._items = {}
        return items
    # TODO: create a new variable and set it equal to the dictionary values. (A new list, not a new dictionary using self._items.values())
    # TODO: set the private variable _items to a new dictionary to make it empty.
    # TODO: return the new variable.

    def count(self):
        return len(self._items)

# TODO: Create a return statement to return the length of the items.

# PART-2


print("PART - 2")


def repack_boxes(*boxes):
    items = []

    # get all the items from each box, save it to a new variable called items, then empty the boxes.
    for box in boxes:
        items.extend(box.empty())

    # now we have all of the items in each box inside one list, traverse the list of items.

    div = len(items) / len(boxes)
    start = 0
    end = math.floor(div)
    total_boxes = len(boxes)
    box_num = 1

    # for each box passed in, add an item to box, remove the item from the item list as its added to the box.
    # if we pass in 3 boxes to this function, that means we'll add 3 items to the boxes and remove those items
    # from the list on each pass within the for loop.
    for box in boxes:
        try:
            if box_num < total_boxes:
                box.add(*items[start:end])
                start = end
                end = end + math.floor(div)
                box_num = box_num + 1
            else:
                end = end + 1
                box.add(*items[start:end])
        # TODO: for each box in boxes: box.add(items.pop())
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
