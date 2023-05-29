import tkinter as tk


class Component:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.tag = "component"

    def draw(self):
        self.canvas.create_rectangle(
            self.x,
            self.y,
            self.x + self.width,
            self.y + self.height,
            fill="gray",
            tags=self.tag,
        )


class Button:
    def __init__(self, canvas, x, y, label):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = 30
        self.height = 20
        self.label = label
        self.tag = "button"

    def draw(self):
        self.canvas.create_rectangle(
            self.x,
            self.y,
            self.x + self.width,
            self.y + self.height,
            fill="lightgray",
            tags=self.tag,
        )
        self.canvas.create_text(
            self.x + self.width / 2,
            self.y + self.height / 2,
            text=self.label,
            tags=self.tag,
        )


class Canvas(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, width=400, height=300)
        self.parent = parent
        self.components = []
        self.buttons = self.bind_buttons()
        self.bind("<Button-1>", self.on_canvas_click)

    def add_component(self, component):
        self.components.append(component)
        component.draw()

    def add_button(self, button):
        self.buttons.append(button)
        button.draw()

    def bind_buttons(self):
        buttons = []
        self.tag_bind("button", "<Button-1>", self.on_button_click)
        return buttons

    def on_button_click(self, event):
        button = self.find_closest(event.x, event.y)[0]
        button_index = self.buttons.index(button)
        clicked_button = self.buttons[button_index]
        print("Button clicked:", clicked_button.label)
        # Handle button click event here

    def on_canvas_click(self, event):
        clicked_tags = self.find_withtag("current")
        if component in self.gettags(clicked_tags):
            component = self.find_withtag("current")[0]
            component_index = self.components.index(component)
            clicked_component = self.components[component_index]
            print("Component clicked:", clicked_component)
            # Handle component click event here


# Example usage
root = tk.Tk()
canvas = Canvas(root)
canvas.pack()

gate = Component(canvas, x=100, y=100)
canvas.add_component(gate)

button = Button(canvas, x=120, y=160, label="Click Me")
canvas.add_button(button)

root.mainloop()
