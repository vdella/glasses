import tkinter as tk
from controller.parsing.text import Parser
from view.paint_interface import paint_graph
from view.paint_interface import draw_horizontal, draw_vertical
from controller.parsing.cache_interface import graphs


class TextFrame:

    def __init__(self, mainframe, canvas, created_objs_frame):
        self.frame = tk.Text(mainframe, bg='#eeeee4', highlightcolor='#10435b', foreground='#010406')
        self.frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas: tk.Canvas = canvas
        self.created_objs_frame = created_objs_frame
        self.button = tk.Button(self.frame, text='Enter', width=10, height=1, command=self.eat,
                                background='#010406', foreground='#eeeee4')
        self.button.pack(side=tk.BOTTOM)

    def eat(self) -> list:
        """Sends the read user input to be properly parsed inside
        the parsing module and deletes what was written in the text box."""
        entries = self.frame.get('1.0', 'end-1c').split('\n')
        Parser.parse(entries)  # TODO refactor method.

        self.canvas.delete('all')
        draw_horizontal(self.canvas)
        draw_vertical(self.canvas)

        structures = graphs()

        for graph in structures:
            print('A')
            paint_graph(graph, self.canvas)

        self.created_objs_frame.show_structures()
        self.frame.delete('1.0', 'end-1c')

        return Parser.parse(entries)
