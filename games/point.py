class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other_point):
        return Point(x=self.x + other_point.x, y=self.y + other_point.y)

    def distance_to(self, other_point):
        delta_x = self.x - other_point.x
        delta_y = self.y - other_point.y

        return (delta_x ** 2 + delta_y ** 2) ** (1/2)

    def distance_to_origin(self):
        return self.distance_to(Point(0, 0))


p1 = Point(1, 2)
p2 = Point(2, 4)
p3 = Point(5, 1)
p4 = Point(10, 10)

p = p1.add(p2.add(p3))
print(f'Point p: {p4}')
print(f'Distance of p to {p4}: {p.distance_to(p4)}')
print(f'Distance of p to origin: {p.distance_to_origin()}')
