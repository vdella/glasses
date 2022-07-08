from tkinter import *
from view.canvas_frame import CanvasFrame
from view.text_frame import TextFrame
from view.created_objects_frame import CreatedObjectsFrame
from view.side_frame import SideFrame
from view.root_window import root
from view.paint_interface import draw_horizontal, draw_vertical
from view.menu import FileMenu


class Application:

    width, height = root.winfo_screenwidth(), root.winfo_screenheight()

    def __init__(self):
        self.root = root

        self.right_side_frame = SideFrame(self.root, RIGHT, self.width, self.height)
        self.canvas_frame = CanvasFrame(self.right_side_frame.frame)
        self.canvas_frame.canvas['width'] = self.width / 2
        self.canvas_frame.canvas['height'] = self.height

        self.file_menu = FileMenu(self.root, self.canvas_frame.canvas)

        draw_horizontal(self.canvas_frame.canvas)
        draw_vertical(self.canvas_frame.canvas)

        self.left_side_frame = SideFrame(self.root, LEFT, self.width / 2, self.height / 2)
        self.text_frame = TextFrame(self.left_side_frame.frame, self.canvas_frame.canvas, None)
        self.object_frame = CreatedObjectsFrame(self.left_side_frame.frame)
        self.text_frame.created_objs_frame = self.object_frame

        self.root.mainloop()


if __name__ == '__main__':
    Application()
