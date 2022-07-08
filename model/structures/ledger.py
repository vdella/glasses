from model.structures.patterns.singleton import Singleton


class StructureLedger(metaclass=Singleton):

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
