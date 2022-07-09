from tkinter import *
from tkinter.filedialog import askopenfilename
from controller.parsing.obj import ObjDescriptor
from model.structures.geometric_structures import Structure
from controller.parsing.cache_interface import add_instruction_from, graphs
from controller.parsing.text import Parser
from view.paint_interface import paint_graph


class FileMenu:

    file_path: str

    def __init__(self, root, canvas):
        self.menu = Menu(root)
        root.config(menu=self.menu)

        self.canvas = canvas

        self.file_menu = Menu(self.menu, tearoff=False)
        self.file_menu.add_command(
            label='Open',
            command=self.add_vertices_to_cache
        )

        self.menu.add_cascade(
            label='File',
            menu=self.file_menu
        )

        self.operations_menu = Menu(self.menu, tearoff=False)
        self.operations_menu.add_command(label='Prompt')
        self.operations_menu.add_command(label='Created structures')

        self.menu.add_cascade(
            label='Operations',
            menu=self.operations_menu
        )

    def obj_vertices(self):
        """:returns a dict with the vertices declared inside an .obj file."""
        self.file_path = askopenfilename()
        digest = ObjDescriptor.digest(self.file_path)['vertices']
        structure: Structure = ObjDescriptor.structure_from(digest)
        return structure

    def add_vertices_to_cache(self):
        vertices = self.obj_vertices()
        add_instruction = add_instruction_from(vertices)
        Parser.parse([add_instruction])

        for graph in graphs():
            paint_graph(graph, self.canvas)

