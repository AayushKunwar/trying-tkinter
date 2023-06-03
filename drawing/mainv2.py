import tkinter as tk
from tkinter import ttk


class Component(ttk.Label):
    def __init__(self, master, **kwargs):
        self.master = master
        self.make_component(**kwargs)
        self.bind("<ButtonPress-1>", self.on_drag_start)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_drag_stop)
        button1 = ttk.Button(master=self, text="B")
        button1.place(x=0, y=0)

    def on_drag_start(self, event):
        self.active = self

    def on_drag(self, event):
        self.active.place(x=event.x, y=event.y)

    def on_drag_stop(self, event):
        self.active = None

    def make_component(self, **kwargs):
        super().__init__(master=self.master, anchor="center", **kwargs)
        self.place(
            x=10,
            y=10,
            width=150,
            height=100,
        )


class MainCanvas(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        comp1 = Component(master=self, text="foobar")
        comp2 = Component(master=self, text="foobar")


root = tk.Tk()
root.geometry("800x600")
root.title("what wha")

canvas = MainCanvas(root, background="grey", height=500, width=600)
canvas.pack()


root.mainloop()
