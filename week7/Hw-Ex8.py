
#EXERCISE 8

import math

class Line:

    def __init__(self, coor1, coor2):
        self.coor1_x = coor1[0]
        self.coor1_y = coor1[1]
        self.coor2_x = coor2[0]
        self.coor2_y = coor2[1]

    def distance(self):
        dist = math.sqrt(((self.coor2_x - self.coor1_x) ** 2) + ((self.coor2_y - self.coor1_y) ** 2))
        return dist

    def slope(self):
        m = (self.coor2_y - self.coor1_y) / (self.coor2_x - self.coor1_x)
        return m


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
print(li.distance())
# 9.433981132056603

print(li.slope())
# 1.6
