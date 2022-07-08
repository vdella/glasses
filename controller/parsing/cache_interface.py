from model.structures.ledger import StructureLedger
from model.structures.geometric_structures import Structure
from model.calculations.homogene_coordinates import translate2d, scale2d, rotate2d


def add_instruction_from(obj_parsed_struct: Structure):
    """Parses a structure born from a .obj file and :returns a
    glass 'add' instruction for it."""
    string_repr = str(obj_parsed_struct).split()
    string_repr = string_repr[2:]  # Trims the type of Structure and the following ':'.

    for pos, _ in enumerate(string_repr):
        # The first and the last will have double parenthesis, so we need to take one of them out.
        if pos == 0:
            string_repr[pos] = string_repr[pos].replace('((', '(')
        elif 0 < pos < len(string_repr) - 2:
            string_repr[pos] = string_repr[pos].replace('),', ') ')  # Removes commas between points
        else:
            string_repr[pos] = string_repr[pos].replace('))', ')')

    return 'add ' + ''.join(string_repr)


def graphs():
    """Generates a polygon-graph from a tuple of point coordinates.
    Each point is directed to its successor; the last points
    to the first."""
    result = list()

    for struct in StructureLedger().elements:
        print(struct)
        graph = dict()

        first = struct.world_coordinates_points[0]
        last = struct.world_coordinates_points[-1]
        graph[last] = first

        for i in range(len(struct.world_coordinates_points) - 1):
            graph[struct.world_coordinates_points[i]] = struct.world_coordinates_points[i + 1]

        result.append(graph)

    return result


def _add(*args):
    StructureLedger().add(Structure(args[0]))


def _remove(*args):
    StructureLedger().remove(Structure(args[0]))


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


if __name__ == '__main__':
    s = Structure(((0, 0), (0, 1), (1, 0), (2000, 2000), (40, 40)))
    print(add_instruction_from(s))
