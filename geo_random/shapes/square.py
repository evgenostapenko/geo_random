from math import pi
from itertools import combinations
from geo_random.shapes.base import BaseShape, Line, Point
from geo_random.exceptions import InvalidSquareException


class SquareShape(BaseShape):
    max_points = 4

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
        l1, l2 = self.lines[0], self.lines[1]
        return l1.distance * l2.distance

    def build_lines(self):
        if len(self.points) != self.max_points:
            return

        tmp_dict = dict()

        for point in self.points:
            if point.x in tmp_dict:
                tmp_dict[point.x].append(point)
            else:
                tmp_dict[point.x] = [point]

        for val in tmp_dict.values():
            if len(val) > 2 or len(val) == 1:
                raise InvalidSquareException('Can not build lines')

        self.lines = list()
        for _, points in tmp_dict.items():
            line = Line(*points)
            self.lines.append(line)
