import tkinter as tk
from parsing.parser import Parser
from ui.paint_interface import paint_graph


class TextFrame:

    def __init__(self, mainframe, canvas, created_objs_frame):
        self.frame = tk.Text(mainframe, bg='#eeeee4', highlightcolor='#10435b', foreground='#010406')
        self.frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas = canvas
        self.created_objs_frame = created_objs_frame
        self.button = tk.Button(self.frame, text='Enter', width=10, height=1, command=self.parse,
                                background='#010406', foreground='#eeeee4')
        self.button.pack(side=tk.BOTTOM)

    def parse(self):
        """Sends the read user input to be properly parsed inside
        the parsing module and deletes what was written in the text box."""
        parser = Parser()
        parser.cache = self.frame.get('1.0', 'end-1c').split('\n')
        edges = parser.parse()
        paint_graph(edges, self.canvas)
        self.created_objs_frame.show_coordinates()
        self.frame.delete('1.0', 'end-1c')
