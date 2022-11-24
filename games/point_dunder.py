class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """ Returns a string representation of the point. """
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        """ Returns a new point that is the sum this point and the other. """
        return Point(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other_point):
        """ Returns the distance between this and the other point. """
        delta_x = self.x - other_point.x
        delta_y = self.y - other_point.y

        return (delta_x ** 2 + delta_y ** 2) ** (1/2)
    
    def __float__(self):
        """ Returns the distance between this and the origin. """
        return self.__sub__(Point(0, 0))
    
    def __lt__(self, other):
        """ Returns if this point is closer to the origin. """
        return float(self) < float(other)

p1 = Point(0, 1)
p2 = Point(3, 5)
p3 = Point(5, 1)
p4 = Point(10, 10)

points = [p1, p2, p3, p4]

s = sum(points, start=Point(0,0))

print(f'Point p: {p1}')
print(f'Sum of all points: {s}')
print(f'Distance of p1 and p2 is: {p1 - p2}')

print(f'Distance of p1 from origin is: {float(p1)}')

closest_point = min(points)
print(f'Closest point is: {closest_point}')