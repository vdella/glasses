from structures.globals import point_cache
from ui.error_presentation import ErrorBox


class Parser:

    cache = list()

    def parse(self) -> dict:
        """Reads user input. 'add' being the operation, generates a polygon
        graph from the desired coordinates. If not, removes the said
        coordinates from cache."""
        self.digest_entry()

        for line in self.cache:
            operation = line[0]
            operands: tuple = tuple([_format(x) for x in line[1:]])

            edges: dict = graph_from(operands)

            if operation == 'add':
                _add(operands)
                return edges
            else:
                ErrorBox()
                return {}

    def digest_entry(self):
        """Digests a line of user input into
        individual parts, separated by blank spaces."""

        for i in range(len(self.cache)):
            cache_entry = self.cache[i].split()
            self.cache[i] = cache_entry
        return self.cache


def _format(written_point: str) -> tuple:
    """Formats a string cartesian coordinate into a
    point tuple."""
    x_begin_index = written_point.index('(') + 1
    x_end_index = written_point.index(',')

    y_begin_index = written_point.index(',') + 1
    y_end_index = written_point.index(')')

    x, y = float(written_point[x_begin_index: x_end_index]), float(written_point[y_begin_index: y_end_index])

    return x, y


def graph_from(points: tuple):
    """Generates a polygon-graph from a tuple of point coordinates.
    Each point is directed to its successor; the last points
    to the first."""
    graph = dict()

    first = points[0]
    last = points[-1]
    graph[last] = first

    for i in range(len(points) - 1):
        graph[points[i]] = points[i + 1]

    return graph


def _add(point):
    point_cache.add(point)


def _remove(point):
    point_cache.remove(point)
