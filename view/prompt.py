import tkinter as tk
from controller.parsing.text import Parser
from view.paint_interface import paint_graph
from view.paint_interface import draw_horizontal, draw_vertical
from controller.parsing.cache_interface import graphs
from constants import X_MAX, Y_MAX


class Prompt:

    def __init__(self, mainframe, canvas_frame, created_objs_frame):
        self.frame = tk.Frame(mainframe, width=X_MAX, height=Y_MAX)
        self.text = tk.Text(self.frame, bg='black', fg='white', width=X_MAX,
                            height=37, insertbackground='white')
        self.text.pack(side=tk.TOP, expand=True, fill=tk.Y)
        self.text.focus()

        self.canvas_frame = canvas_frame
        self.created_objs_frame = created_objs_frame
        self.button = tk.Button(self.frame, text='Enter', width=X_MAX, command=self.eat,
                                background='white', foreground='black')
        self.button.pack(side=tk.BOTTOM, fill=tk.BOTH)
        self.frame.pack()

    def eat(self) -> list:
        """Sends the read user input to be properly parsed inside
        the parsing module and deletes what was written in the text box."""
        entries = self.text.get('1.0', 'end-1c').split('\n')
        Parser.parse(entries)  # TODO refactor method.

        self.canvas_frame.canvas.delete('all')
        draw_horizontal(self.canvas_frame.canvas)
        draw_vertical(self.canvas_frame.canvas)

        structures = graphs()

        for graph in structures:
            print('A')
            paint_graph(graph, self.canvas_frame.canvas)

        self.created_objs_frame.show_structures()
        self.text.delete('1.0', 'end-1c')

        return Parser.parse(entries)
