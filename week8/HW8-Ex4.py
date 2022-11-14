
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
