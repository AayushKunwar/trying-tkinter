import tkinter as tk
from tkinter import Label, ttk

window = tk.Tk()
window.geometry("600x400")
window.title("hide widgets")


def toggle_label_place():
    global label_visible

    if label_visible:
        label.place_forget()
        label_visible = False
    else:
        label_visible = True
        label.place(relx=0.5, rely=0.5, anchor="center")


button = ttk.Button(window, text="toggle label", command=toggle_label_place)
button.place(x=10, y=10)

label_visible = True
label = ttk.Label(window, text="foo")
label.place(relx=0.5, rely=0.5, anchor="center")

window.mainloop()
