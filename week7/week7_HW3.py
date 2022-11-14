
#EXERCISE 3


class Squares:

    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2


square1 = Squares(6)
print(f"area of the square with side {square1.side} is:", square1.calculate_area())

square2 = Squares(5)
print(f"area of the square with side {square2.side} is:", square2.calculate_area())
