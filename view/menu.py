from tkinter import *
from tkinter.filedialog import askopenfilename

import constants
from controller.parsing.obj import ObjDescriptor
from model.structures.geometric_structures import Structure
from controller.parsing.cache_interface import add_instruction_from, graphs
from controller.parsing.text import Parser
from view.paint_interface import paint_graph


class FileMenu:

    file_path: str

    def __init__(self, root, menu_frames: tuple):
        self.root = root
        self.menu = Menu(self.root)
        root.config(menu=self.menu)

        self.prompt_frame, self.canvas_frame, self.created_objects_frame = menu_frames

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
        self.operations_menu.add_command(
            label='Prompt',
            command=self.show_prompt)
        self.operations_menu.add_command(
            label='Created structures',
            command=self.show_created_objects
        )
        self.operations_menu.add_command(
            label='Canvas',
            command=self.show_canvas
        )

        self.menu.add_cascade(
            label='Operations',
            menu=self.operations_menu
        )

        self.show_canvas()

    def show_prompt(self):
        self.prompt_frame.frame.configure(width=constants.X_MAX, height=constants.Y_MAX)
        self.prompt_frame.frame.pack()

        self.canvas_frame.canvas.pack_forget()
        self.created_objects_frame.frame.pack_forget()

    def show_created_objects(self):
        self.created_objects_frame.frame.configure(width=constants.X_MAX, height=constants.Y_MAX)
        self.created_objects_frame.frame.pack()

        self.canvas_frame.canvas.pack_forget()
        self.prompt_frame.frame.pack_forget()

    def show_canvas(self):
        self.canvas_frame.canvas.configure(width=constants.X_MAX, height=constants.Y_MAX)
        self.canvas_frame.canvas.pack()

        self.prompt_frame.frame.pack_forget()
        self.created_objects_frame.frame.pack_forget()

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
            paint_graph(graph, self.canvas_frame.canvas_frame)
