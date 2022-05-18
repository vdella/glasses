class Structure:

    def __init__(self, points, label=''):
        self.points = points
        self.label = label

    def __str__(self):
        written = str(self.points)
        if len(self.points) == 1:
            struct_type = 'Point'
            written = written.replace(',)', ')')
        elif len(self.points) == 2:
            struct_type = 'Line'
        else:
            struct_type = 'Polygon'
        return '{} : {}'.format(struct_type, written) \
            if self.label == '' \
            else '{} : {} : {}'.format(self.label, struct_type, written)
