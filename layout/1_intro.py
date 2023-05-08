import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("Intro to layout")

# 3 methods
"""
1. Pack 
    top to button, width, direction
2. grid
    2d postioning
    overlapping widgets
3. place
    place in (x,y) position

"""
# widgets
label1 = ttk.Label(window, text="Label1", background="red")
label2 = ttk.Label(window, text="Label2", background="blue")

# label1.pack(side="left", expand=True, fill="y")
# label2.pack(side="left", expand=True, fill="both")

# # for grid
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=2)
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)

# label1.grid(row=0, column=1, sticky="nsew")
# label2.grid(row=1, column=1, columnspan=2, sticky="nsew")

# place
# uses absolute pixel postitions
label1.place(x=100, y=200, width=200, height=100)
# uses float 0 to 1 value
# changes with window size
label2.place(relx=0.1, rely=0.1, anchor="center")

window.mainloop()
