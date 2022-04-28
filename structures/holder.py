from dataclasses import dataclass
from structures.simple import Point


@dataclass
class PointHolder:
    points = set()
    last: Point = Point(0, 0)

    def push(self, point):
        self.last = point
        return self.points.add(self.last)
