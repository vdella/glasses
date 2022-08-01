from model.structures.patterns.singleton import Singleton


class StructureLedger(metaclass=Singleton):
    """As a StructureLedger containing all created structures will be needed,
    a Singleton pattern was used in order to avoid object duplication."""

    def __init__(self):
        self.elements = set()

    def add(self, structure):
        self.elements |= {structure}

    def remove(self, structure):
        self.elements -= {structure}


if __name__ == '__main__':
    s = StructureLedger()
    print(s.add(0))
    a = StructureLedger()
    print(a.elements)
