import tkinter as tk
from structures.globals import structure_cache


class CreatedObjectsFrame:

    def __init__(self, mainframe):
        self.frame = tk.Frame(mainframe)
        self.text = tk.Text(self.frame, state=tk.DISABLED, bg='#010406', fg='#eeeee4')
        self.frame.pack()
        self.text.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def show_coordinates(self):
        """Deletes textbox content
        and writes coordinates of all points.
        Needed in order to show newly added coordinates."""

        self.text['state'] = tk.NORMAL

        self.text.delete('1.0', tk.END)

        for p in structure_cache:
            points = p.points
            coordinate_str: str = str(points)
            if len(points) == 2:
                structure = 'Line'
            elif len(points) > 2:
                structure = 'Polygon'
            else:
                coordinate_str = str(points).replace(',)', ')')
                structure = 'Point'
            self.text.insert(tk.INSERT, '{} : {}\n'.format(structure, coordinate_str))

        self.text['state'] = tk.DISABLED
