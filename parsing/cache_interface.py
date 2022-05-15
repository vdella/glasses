from structures.globals import structure_cache


def _add(structure):
    structure_cache.add(structure)


def _remove(structure):
    structure_cache.remove(structure)


def _translate(structure):
    pass


def _scale(structure):
    pass


def _rotate(structure):
    pass


module_functions = {'add': _add,
                    'rm': _remove,
                    'tl': _translate,
                    'sc': _scale,
                    'rt': _rotate}
