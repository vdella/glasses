class Structure:

    def __init__(self, points: tuple):
        self.world_coordinates_points: tuple = points
        self.projection_coordinates: tuple = points  # Immutable. Don't need to create a copy.

    def __str__(self):
        written = str(self.world_coordinates_points)
        if len(self) == 1:
            struct_type = 'Point'
            written = written.replace(',)', ')')
        elif len(self.world_coordinates_points) == 2:
            struct_type = 'Line'
        else:
            struct_type = 'Polygon'
        return '{} : {}'.format(struct_type, written)

    def __eq__(self, other):
        if isinstance(other, Structure):
            return True if self.world_coordinates_points == other.world_coordinates_points else False

    def __hash__(self):
        return hash(self.world_coordinates_points)

    def __len__(self):
        return len(self.world_coordinates_points)


if __name__ == '__main__':
    print(Structure(((0, 0),),))
