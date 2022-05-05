from dataclasses import dataclass


@dataclass
class Holder:
    elements = set()

    def push(self, point):
        return self.elements.add(point)

    def remove(self, point):
        self.elements.remove(point)


point_cache = Holder()
line_cache = Holder()
polygon_cache = Holder()
