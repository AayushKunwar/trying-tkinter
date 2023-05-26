# Import the library
import tkinter as tk

# Create an instance of tkinter
win = tk.Tk()

# Window size
win.geometry("700x300")


# Method to draw line between two consecutive points
def draw_line(e):
    x, y = e.x, e.y
    if canvas.old_coords:
        x1, y1 = canvas.old_coords
        canvas.create_line(x, y, x1, y1, width=5)
    canvas.old_coords = x, y


canvas = tk.Canvas(win, width=700, height=300)
canvas.pack()
canvas.old_coords = None

# Bind the left button the mouse.
win.bind("<ButtonPress-1>", draw_line)

win.mainloop()
