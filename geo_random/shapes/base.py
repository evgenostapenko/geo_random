from math import sqrt
from geo_random.exceptions import InvalidLineException, MaxPointCountExceeded, BaseShapeException


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({};{})'.format(self.x, self.y)


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.is_valid()

    def is_valid(self):
        if self.p1.x == self.p2.x and self.p1.y == self.p2.y:
            raise InvalidLineException('P1{} and P2{} are identical'.format(self.p1, self.p2))

    def get_distance(self):
        x = self.p1.x - self.p2.x
        y = self.p1.y - self.p2.y
        result = sqrt(x ** 2 + y ** 2)

        return result

    @property
    def distance(self):
        return self.get_distance()


class BaseShape:
    max_points = 0

    def __init__(self, points=None):
        self.points = points or list()
        self.lines = list()
        self.is_valid()

    def __str__(self):
        return ', '.join(self.points)

    def add_point(self, point):
        self.points.append(point)

        try:
            self.is_valid()
        except BaseShapeException as e:
            self.points.remove(point)
            raise e

    def is_valid(self):
        if len(self.points) > self.max_points:
            raise MaxPointCountExceeded('Allowed {} but got {}'.format(self.max_points, len(self.points)))

        return True

    def get_square(self):
        raise NotImplementedError()

    def build_lines(self):
        raise NotImplementedError()
