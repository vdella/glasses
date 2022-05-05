from tkinter import *
from ui.canvas_frame import CanvasFrame
from ui.text_frame import TextFrame
from ui.created_objects_frame import CreatedObjectsFrame
from ui.side_frame import SideFrame
from ui.root_window import root


class Application:

    width, height = root.winfo_screenwidth(), root.winfo_screenheight()

    def __init__(self):
        self.root = root

        self.right_side_frame = SideFrame(self.root, RIGHT, self.width, self.height)
        self.canvas_frame = CanvasFrame(self.right_side_frame.frame, self.width, self.height)

        self.left_side_frame = SideFrame(self.root, LEFT, self.width, self.height)
        self.text_frame = TextFrame(self.left_side_frame.frame, self.canvas_frame.canvas, None)
        self.object_frame = CreatedObjectsFrame(self.left_side_frame.frame)
        self.text_frame.created_objs_frame = self.object_frame

        self.root.mainloop()
