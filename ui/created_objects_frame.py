import tkinter as tk
from structures.globals import structure_cache
from structures.geometric_structures import Structure


class CreatedObjectsFrame:

    def __init__(self, mainframe):
        self.frame = tk.Frame(mainframe)
        self.text = tk.Text(self.frame, state=tk.DISABLED, bg='#010406', fg='#eeeee4')
        self.frame.pack()
        self.text.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def show_structures(self):
        """Deletes textbox content
        and writes coordinates of all points.
        Needed in order to show newly added coordinates."""

        self.text['state'] = tk.NORMAL

        self.text.delete('1.0', tk.END)

        for p in structure_cache:
            p: Structure
            self.text.insert(tk.INSERT, '{}\n'.format(str(p)))

        self.text['state'] = tk.DISABLED
