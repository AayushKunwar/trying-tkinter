import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title("pack and frames")
window.geometry("400x600")

"""
basically use frames as div from css

"""
"""
Grid method
can be used to overlap widgets
space widget can occupy

"""
# define a grid
# column index 0, weight=size = 1
window.columnconfigure(0, weight=1)
# column index 1
window.columnconfigure(1, weight=1)
# this can also work, window.columnconfigure((0,1,2),weight=1, uniform="a")
window.rowconfigure(0, weight=1)

# label1.grid(row=0, column=0, sticky="nsew")
"""
use sticky to make widgets stick to the sides
north east west south
"""
"""
when using empty cells in grid, tkinter messes it up
use uniform="a" in columnconfigure
"""

window.mainloop()
