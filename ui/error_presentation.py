from tkinter import messagebox


class ErrorBox:

    def __init__(self):
        messagebox.showerror('Unknown operation found', 'Try adding or removing coordinates.')
