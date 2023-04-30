import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("Tab widget")

# notebook widget
notebook = ttk.Notebook(window)
# each tab is frame inside notebook
# frame ko parent, not so important
# dont pack frames themselves,
# tab 1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text="text in tab1")
label1.pack()

# tab2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text="text in tab2")
label2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()


notebook.add(tab1, text="tab1")
notebook.add(tab2, text="tab2")
notebook.pack()

window.mainloop()
