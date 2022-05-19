class Structure:

    def __init__(self, points):
        self.points: tuple = points

    def __str__(self):
        written = str(self.points)
        if len(self) == 1:
            struct_type = 'Point'
            written = written.replace(',)', ')')
        elif len(self.points) == 2:
            struct_type = 'Line'
        else:
            struct_type = 'Polygon'
        return '{} : {}'.format(struct_type, written)

    def __eq__(self, other):
        if isinstance(other, Structure):
            return True if self.points == other.points else False

    def __hash__(self):
        return hash(self.points)

    def __len__(self):
        return len(self.points)


if __name__ == '__main__':
    print(Structure(((0, 0),),))
