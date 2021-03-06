import tkinter as tk
from model.structures.ledger import StructureLedger
from model.structures.geometric_structures import Structure
from constants import X_MAX, Y_MAX


class CreatedObjectsFrame:

    def __init__(self, mainframe):
        self.frame = tk.Frame(mainframe)
        self.text = tk.Text(self.frame, state=tk.DISABLED, bg='black', fg='white', width=X_MAX, height=Y_MAX)
        self.frame.pack()
        self.text.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def show_structures(self):
        """Deletes textbox content
        and writes coordinates of all points.
        Needed in order to show newly added coordinates."""

        self.text['state'] = tk.NORMAL

        self.text.delete('1.0', tk.END)

        for p in StructureLedger().elements:
            p: Structure
            self.text.insert(tk.INSERT, '{}\n'.format(str(p)))

        self.text['state'] = tk.DISABLED
