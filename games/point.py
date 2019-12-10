"""
1) Create a Point class that has two attributes, x and y. Remember the constructor.
2) Implement an add method that takes another point, adds this one to itself and returns a new Point that is the result
   of the addition.
3) Implement a method, that calculates the distance from itself to another point using Pythagoras. The other point
   should be given as a parameter. Return the calculated distance as a number.
4) Implement a method, that calculates the distance from the point to the origin (0,0). No parameters are needed.
5) Given p1 = Point(1,2), p2 = Point(2,4) and p3 = Point(5,1). Add all points to p. Calculate the distance of p to
   p4 = Point(10,10) and (0,0). (Results should be `3.6` and `10.6` respectively)

INFO: Do not forget the self parameter for any method.
INFO: Everything should be implemented on the class. No standalone functions are needed (or allowed ;) ).
INFO: Raising a number to a power is done using the `**` operator, e.g. 2 ** 3 == 8. If you want to calculate the square
      root, raise the number to 1/2 for now.

BONUS: Together with the tutors. Overload appropriate operators to make your life easier.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other_point):
        return Point(x=self.x + other_point.x, y=self.y + other_point.y)

    def distance_to(self, other_point):
        delta_x = self.x - other_point.x
        delty_y = self.y - other_point.y

        return (delta_x ** 2 + delty_y ** 2) ** (1/2)

    def distance_to_origin(self):
        return self.distance_to(Point(0, 0))

    def __str__(self):
        return f'({self.x},{self.y})'

    def __add__(self, other_point):
        return self.add(other_point)


p1 = Point(1, 2)
p2 = Point(2, 4)
p3 = Point(5, 1)
p4 = Point(10, 10)

p = p1.add(p2.add(p3))
print(f'Point p: {p4}')
print(f'Distance of p to {p4}: {p.distance_to(p4)}')
print(f'Distance of p to origin: {p.distance_to_origin()}')

print('Cooler!')
print('=======')

p = p1 + p2 + p3
print(f'Point p: {p}')
p = sum([p1, p2, p3], Point(0, 0))
print(f'Point p: {p}')
print(f'Distance of p to {p4}: {p.distance_to(p4)}')
print(f'Distance of p to origin: {p.distance_to_origin()}')
