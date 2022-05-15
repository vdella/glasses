from parsing.cache_interface import module_functions
from structures.geometric_structures import Structure


class Parser:

    cache = list()

    def parse(self) -> list:
        """Digests user input and draws a graph according
        to given coordinates."""

        self.digest_entry()

        results = list()

        for line in self.cache:
            operation = line[0]
            operands: tuple = tuple([_format(x) for x in line[1:]])

            module_functions[operation](Structure(operands))

            edges: dict = graph_from(operands)
            results.append(edges)
        return results

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
