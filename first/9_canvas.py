import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("500x500")
window.title("canvas")

# canvas
canvas = tk.Canvas(window, bg="white")
canvas.pack()

# canvas.create_rectangle((50, 20, 100, 200), fill="red", width=10, dash=(1, 2))
# width -> of border
# dash ->(length of dash,width of dash) has more patterns
# outline -> colour of border
# canvas.create_line((200, 0, 300, 150), fill="blue")
# canvas.create_oval((0, 0, 100, 300), fill="green")
# .create_polygon
# .create_arc -> part of circle, has attributes-> start, extent, style=tk.ARC, outline
# style = PIESLICE (default), CHORD, ARC

# canvas.create_text((100, 200), text="This is some text", fill="green",width=10)

# can show widget inside canvas
# canvas.create_window(
# (50, 100), window=ttk.Label(window, text="this is text in a canvas")
# )

# Exercise
# use event binding to create a basic paint app


def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval(
        (
            x - brush_size / 2,
            y - brush_size / 2,
            x + brush_size / 2,
            y + brush_size / 2,
        ),
        fill="black",
    )


def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4

    brush_size = max(min(brush_size, 50), 0)


brush_size = 4
# canvas.bind("<Motion>", draw_on_canvas)
canvas.bind("<B1-Motion>", draw_on_canvas)
# canvas.bind("<Button-1>", draw_on_canvas)
canvas.bind("<MouseWheel>", brush_size_adjust)

window.mainloop()
