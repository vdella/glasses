from parsing.cache_interface import module_functions


class Parser:

    def parse(self, entries) -> ():
        """Digests user input and draws a graph according
        to given coordinates."""

        digest_cached = self._digest(entries)

        for line in digest_cached:
            operation = line[0]
            operands: tuple = tuple([_format(x) for x in line[1:]])

            module_functions[operation](operands)

    @staticmethod
    def _digest(entries):
        """Digests a line of user input into
        individual parts, separated by blank spaces."""

        for i in range(len(entries)):
            cache_entry = entries[i].split()
            entries[i] = cache_entry
        return entries


def _format(written_point: str) -> tuple:
    """Formats a string cartesian coordinate into a
    point tuple."""
    x_begin_index = written_point.index('(') + 1
    x_end_index = written_point.index(',')

    y_begin_index = written_point.index(',') + 1
    y_end_index = written_point.index(')')

    x, y = float(written_point[x_begin_index: x_end_index]), float(written_point[y_begin_index: y_end_index])

    return x, y
