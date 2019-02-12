from math import pi
from geo_random.shapes.base import BaseShape, Line, Point
from geo_random.exceptions import InvalidCircleException


class CircleShape(BaseShape):
    max_points = 2

    def __init__(self, points=None):
        super().__init__(points)
        self.build_lines()

    def add_point(self, point):
        super().add_point(point)
        self.build_lines()

    def is_valid(self):
        super().is_valid()
        if len(self.points) == self.max_points:
            p1, p2 = tuple(self.points)
            if p1.x == p2.x and p1.y == p2.y:
                raise InvalidCircleException('Points P1{} and P2{} are similar'.format(p1, p2))

    def get_square(self):
        self.build_lines()
        line = self.lines[0]
        return pi * line.get_distance()

    def build_lines(self):
        if len(self.points) == self.max_points:
            self.lines = list()
            line = Line(*self.points)
            self.lines.append(line)
