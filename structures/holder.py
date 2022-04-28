from dataclasses import dataclass


@dataclass
class PointHolder:
    points = set()

    def push(self, point):
        return self.points.add(point)

    def pop(self):
        return self.points.pop()
