
#Exercise6

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * (self.radius ** 2)
        return round(area, 2)

    def calculate_perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        return round(perimeter, 2)


rad = int(input("Enter the radius:"))
ci = Circle(rad)
print("radius of circle is:", ci.radius)
print("area is:",ci.calculate_area())
print("perimeter is:", ci.calculate_perimeter())

