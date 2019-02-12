import sys
from geo_random.shapes import *


SHAPES = {
    'triangle': TriangleShape,
    'square': SquareShape,
    'circle': CircleShape
}


if __name__ == '__main__':
    shape_type = sys.argv[1]
    points = sys.argv[2:]

    if shape_type not in SHAPES:
        raise Exception('Invalid shape type')

    shape_cls = SHAPES[shape_type]

    def map_pints(p):
        x, y = p.split(',')
        return float(x), float(y)

    points = map(map_pints, points)
    points = [Point(*p) for p in points]

    shape = shape_cls(points=points)
    print(shape.get_square())

