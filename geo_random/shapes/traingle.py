from math import sqrt
from itertools import combinations
from geo_random.shapes.base import BaseShape, Line, Point
from geo_random.exceptions import InvalidSquareException


class TriangleShape(BaseShape):
    max_points = 3

    def __init__(self, points=None):
        super().__init__(points)
        self.build_lines()

    def add_point(self, point):
        super().add_point(point)
        self.build_lines()

    def is_valid(self):
        super().is_valid()
        combined = combinations(self.points, 2)

        for val in combined:
            p1, p2 = val[0], val[1]

            if p1.x == p2.x and p1.y == p2.y:
                raise InvalidSquareException('Points P1{} and P2{} are similar'.format(p1, p2))

        return True

    def get_square(self):
        self.build_lines()
        p = sum([l.distance for l in self.lines])

        a, b, c = self.lines[0].distance, self.lines[1].distance, self.lines[2].distance
        result = sqrt(p * (p - a) * (p - b) * (p - c))

        return result

    def build_lines(self):
        if len(self.points) != self.max_points:
            return

        line_points = combinations(self.points, 2)

        self.lines = list()
        for points in line_points:
            line = Line(*points)
            self.lines.append(line)
