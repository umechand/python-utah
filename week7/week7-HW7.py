
#EXERCISE 7

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        a = self.length * self.breadth
        return round(a, 2)


length = int(input("pls enter the  length of rectangle:"))
breadth = int(input("pls enter the breadth of rectangle:"))

r = Rectangle(length, breadth)
print("length of rectangle is:", r.length)
print("breadth of rectangle is:", r.breadth)
print("area of rectangle is:", r.calculate_area())

