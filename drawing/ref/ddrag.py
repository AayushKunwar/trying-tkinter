from tkinter import Tk, Label, Button


class DraggableWidget(Label):
    def __init__(self, master, text, **kwargs):
        super().__init__(master, text=text, **kwargs)
        self.bind("<Button-1>", self.on_start_drag)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_drop)
        self.drag_data = None

    def on_start_drag(self, event):
        self.drag_data = {"x": event.x, "y": event.y}

    def on_drag(self, event):
        self.place(
            x=self.winfo_x() + (event.x - self.drag_data["x"]),
            y=self.winfo_y() + (event.y - self.drag_data["y"]),
        )

    def on_drop(self, event):
        self.drag_data = None


root = Tk()
root.title("Drag and Drop Example")
widget1 = DraggableWidget(root, text="Widget 1", bg="lightblue")
widget2 = DraggableWidget(root, text="Widget 2", bg="lightgreen")

widget1.place(x=50, y=50)
widget2.place(x=150, y=50)

root.mainloop()
