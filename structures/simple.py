from dataclasses import dataclass


@dataclass(frozen=True)  # To be hashable but immutable.
class Point:
    x: float
    y: float
    z: float = 0

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


@dataclass
class Line:
    src: Point
    dst: Point = Point(0, 0)

    def __str__(self):
        print('src = ({}, {}), dst = ({}, {})'.format(
            self.src.x, self.src.y, self.dst.x, self.dst.y
        ))
