from model.structures.geometric_structures import Structure
from path import resources_dir


class ObjDescriptor:

    @staticmethod
    def digest(obj_file) -> dict:
        """Parses an .obj file and reads its vertices, textures and faces values.
        :returns a dict with 'vertices', 'textures' and 'faces'."""

        content = ObjDescriptor.__raw_content(obj_file)

        vertices = list()
        textures = list()
        faces = list()

        for line in content:
            if line.startswith('v'):
                point = [float(x) for x in line.split()[1:]]  # Skips 'v' at the beginning of line.

                if len(point) == 3:  # Checks if it doesn't have w at the end. Defaults to 1.
                    point.append(1)

                vertices.append(point)

            elif line.startswith('vp'):
                textures.append([float(x) for x in line.split()[1:]])
            elif line.startswith('f'):
                # Faces can be written with coordinates between slashes in order to indicate other properties.

                for face in line.split()[1:]:  # Skips 'f' at the beginning of line.
                    triple = list()

                    for f in face.split('/'):  # Splits by slashes...
                        triple.append(f) if f != '' else triple.append(0)  # And appends 0 if an empty string is found.

                    faces.append(triple)

        return {'vertices': vertices, 'textures': textures, 'faces': faces}

    @staticmethod
    def structure_from(vertices: list):
        raw = list()

        for point in vertices:
            x = point[0]
            y = point[1]
            raw.append((x, y))

        digest = tuple(raw)
        return Structure(digest)

    @staticmethod
    def generate_obj_from(struct: Structure):
        points = struct.world_coordinates_points
        content = ['v {} {} 0\n'.format(points[0], points[1]) for _ in points]  # Needs to have (x, y, z) to be correct.

        with open(resources_dir / 'generated.obj', 'w+') as f:
            f.write('g Object001\n\n')  # Points the object file group at its header.
            for line in content:
                f.write(line)
        return f

    @staticmethod
    def __raw_content(filename) -> list:
        """:returns the :param file content without blank spaces and empty strings."""
        content = list()
        with open(resources_dir / filename) as f:
            for line in f:
                digest = line.replace('\n', '')  # Trims line breaks...

                if digest != '':  # And ignores empty strings.
                    content.append(digest)
        return content


if __name__ == '__main__':
    a = ObjDescriptor.digest('cube.obj')
    print(ObjDescriptor.structure_from(a['vertices']))
    ObjDescriptor.generate_obj_from(Structure((0, 0),))
