from tkinter import *


def create_root():
    root_window = Tk()
    root_window.title('Glasses')
    root_window.geometry("{}x{}".format(root_window.winfo_screenwidth(), root_window.winfo_screenheight()))
    return root_window


root = create_root()
