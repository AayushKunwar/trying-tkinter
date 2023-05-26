import tkinter as tk


def draw_line(event):
    global line
    if line is None:
        line = canvas.create_line(event.x, event.y, event.x, event.y, fill="black")
    else:
        canvas.coords(line, event.x, event.y, line[2], line[3])


root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

button1 = tk.Button(
    root, text="Button 1", command=lambda: draw_line(root.winfo_pointer())
)
button1.pack()

button2 = tk.Button(
    root, text="Button 2", command=lambda: draw_line(root.winfo_pointer())
)
button2.pack()

line = None

root.mainloop()
