import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Pack")
window.geometry("400x600")

"""
pack is for top to button
important args
    side = left, right, top, button
    expand = True, False (width widget can occupy)
    fill = x,y,both, none (width widget will occupy)

side: direction of widget stacking
"""

# widgets
label1 = ttk.Label(window, text="first label", background="red")
label2 = ttk.Label(window, text="second label", background="blue")
label3 = ttk.Label(window, text="third label", background="green")
label4 = ttk.Label(window, text="fourth label", background="yellow")

label1.pack(side="top", expand=True, fill="both", padx=20, pady=20)
label2.pack(side="left", expand=True, fill="both")
label3.pack(side="top", expand=True, fill="both")
label4.pack(side="top", expand=True, fill="both")
"""two types of space
can occupy, or what it will occupy
if packed top to buttom, expand means widget expands sideways (whitespace only)
fill means the widget will occupy the available space
"""
"""
padding
    padx, pady means adding whitespace around widget (margin from css)
    ipadx, ipady means padding like from css (not really needed, use expand, fill)
"""

window.mainloop()
