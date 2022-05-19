from structures.globals import structure_cache
from structures.geometric_structures import Structure
from operations.homogene_coordinates import translate2d, scale2d, rotate2d


def graphs():
    """Generates a polygon-graph from a tuple of point coordinates.
    Each point is directed to its successor; the last points
    to the first."""
    result = list()

    for struct in structure_cache:
        graph = dict()

        first = struct.points[0]
        last = struct.points[-1]
        graph[last] = first

        for i in range(len(struct.points) - 1):
            graph[struct.points[i]] = struct.points[i + 1]

        result.append(graph)

    return result


def _add(*args):
    structure_cache.add(Structure(args[0]))


def _remove(*args):
    structure_cache.remove(Structure(args[0]))


def _translate(*args):
    operands, distance = args[0][:-1], args[0][-1]

    _remove(operands)
    update = tuple([translate2d(point, distance) for point in operands])
    _add(update)

    return update


def _scale(*args):
    operands, distance = args[0][:-1], args[0][-1]

    _remove(operands)
    update = tuple([scale2d(point, distance) for point in operands])
    _add(update)

    return update


def _rotate(*args):
    operands, distance = args[0][:-1], args[0][-1]

    _remove(operands)
    update = tuple([rotate2d(point, distance) for point in operands])
    _add(update)

    return update


module_functions = {'add': _add,
                    'rm': _remove,
                    'tl': _translate,
                    'sc': _scale,
                    'rt': _rotate}
