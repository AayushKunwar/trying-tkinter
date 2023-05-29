import tkinter as tk


class Node(tk.Frame):
    line_pos = None
    line_start = None

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
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
        print(self.winfo_x(), self.winfo_y())
        print(self.drag_data)

    def on_drop(self, event):
        self.drag_data = None

    def get_self(self):
        return self

    @staticmethod
    def line_handler(self):
        if Node.line_pos is None:
            Node.line_pos = (self.winfo_x(), self.winfo_y())
            Node.line_start = self
        else:
            line_end = (self.winfo_x(), self.winfo_y())


class Element(Node):
    def __init__(self, master, text, **kwargs):
        super().__init__(master=master, width=100, height=100, **kwargs)

        main_label = tk.Label(master=super().get_self(), text=text)
        main_label.place(x=super().winfo_x() + 40, y=super().winfo_y() + 40)

        input1 = tk.Button(
            master=super().get_self(),
            bg="blue",
            width=1,
            height=1,
            command=lambda: self.line_handler(self),
        )
        input1.place(x=super().winfo_x(), y=super().winfo_y() + 20)


root = tk.Tk()
root.title("what what")
root.geometry("600x400")

label1 = Element(root, text="and", bg="red")
label2 = Element(root, text="what", bg="green")

label1.place(x=10, y=0)
label2.place(x=100, y=100)

root.mainloop()
