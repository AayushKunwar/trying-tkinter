import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("place")
window.geometry("400x600")

label1 = ttk.Label(window, text="label 1", background="red")
label2 = ttk.Label(window, text="label 2", background="blue")

# absolute positioning
label1.place(x=100, y=200, width=200, height=50)
label2.place(relx=0.2, rely=0.3, relwidth=0.4, relheight=0.5)

window.mainloop()
